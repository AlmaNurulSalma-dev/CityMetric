"""
CityMetric - Phase 4: Visualization
Generates:
  - Interactive Folium world map (HTML)
  - Plotly charts: radar, scatter, heatmap, bar rankings, box plots (HTML)
  - Static PNGs via matplotlib for reports
"""

import warnings
import json
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

warnings.filterwarnings("ignore")

ROOT     = Path(__file__).resolve().parent.parent
PROC_OUT = ROOT / "data" / "processed"
VIZ_DIR  = ROOT / "output"
VIZ_DIR.mkdir(parents=True, exist_ok=True)

CLUSTER_COLORS = {
    0: "#FFB6D9",
    1: "#C8A2E8",
    2: "#B4D7FF",
    3: "#FFE8B6",
    4: "#B4FFD7",
}
CLUSTER_COLORS_DARK = {
    0: "#E8669A",
    1: "#9B59B6",
    2: "#5B9BD5",
    3: "#E8A020",
    4: "#27AE60",
}

DIMS = [
    "affordability_score", "digital_score", "urban_score",
    "innovation_score", "talent_score", "growth_score",
]
DIM_LABELS = ["Affordability", "Digital", "Urban", "Innovation", "Talent", "Growth"]


# ═══════════════════════════════════════════════════════════════════════════════
# A — FOLIUM INTERACTIVE MAP
# ═══════════════════════════════════════════════════════════════════════════════

def make_folium_map(df):
    print("\n[A] Building interactive Folium map...")
    import folium
    from folium.plugins import HeatMap, Fullscreen, MiniMap

    m = folium.Map(
        location=[20, 10],
        zoom_start=2,
        tiles="CartoDB positron",
        prefer_canvas=True,
    )
    Fullscreen().add_to(m)
    MiniMap(toggle_display=True).add_to(m)

    # ── Cluster marker layer ──────────────────────────────────────────────────
    cluster_layer = folium.FeatureGroup(name="City Clusters", show=True)
    for _, row in df.iterrows():
        c      = int(row["cluster"])
        color  = CLUSTER_COLORS.get(c, "#CCCCCC")
        cname  = row["cluster_name"]
        pop_m  = f"{row['population']/1e6:.1f}M" if pd.notna(row.get("population")) else "N/A"
        radius = 8 + min(row["opportunity_index"] * 1.2, 8)

        popup_html = f"""
        <div style="font-family:sans-serif;min-width:200px">
          <h4 style="margin:0;color:#333">{row['city']}, {row['country']}</h4>
          <hr style="margin:4px 0;border-color:#eee">
          <b>Cluster:</b> {cname}<br>
          <b>Opportunity:</b> {row['opportunity_index']:.2f}/10<br>
          <b>Population:</b> {pop_m}<br>
          <hr style="margin:4px 0;border-color:#eee">
          <table style="font-size:12px;width:100%">
            <tr><td>Affordability</td><td align="right"><b>{row['affordability_score']:.1f}</b></td></tr>
            <tr><td>Digital</td>      <td align="right"><b>{row['digital_score']:.1f}</b></td></tr>
            <tr><td>Urban</td>        <td align="right"><b>{row['urban_score']:.1f}</b></td></tr>
            <tr><td>Innovation</td>   <td align="right"><b>{row['innovation_score']:.1f}</b></td></tr>
            <tr><td>Talent</td>       <td align="right"><b>{row['talent_score']:.1f}</b></td></tr>
            <tr><td>Growth</td>       <td align="right"><b>{row['growth_score']:.1f}</b></td></tr>
          </table>
        </div>"""

        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=radius,
            color=CLUSTER_COLORS_DARK.get(c, "#999"),
            weight=1.5,
            fill=True,
            fill_color=color,
            fill_opacity=0.82,
            popup=folium.Popup(popup_html, max_width=240),
            tooltip=f"{row['city']} — {row['opportunity_index']:.2f}/10",
        ).add_to(cluster_layer)
    cluster_layer.add_to(m)

    # ── Opportunity heatmap layer ──────────────────────────────────────────────
    heat_data = [
        [row["latitude"], row["longitude"], row["opportunity_index"]]
        for _, row in df.iterrows()
    ]
    heat_layer = folium.FeatureGroup(name="Opportunity Heatmap", show=False)
    HeatMap(heat_data, radius=40, blur=25,
            gradient={"0.3": "#B4D7FF", "0.6": "#C8A2E8", "1.0": "#FFB6D9"}
            ).add_to(heat_layer)
    heat_layer.add_to(m)

    # ── Legend ────────────────────────────────────────────────────────────────
    cluster_names = df.groupby("cluster")["cluster_name"].first().to_dict()
    legend_html = """
    <div style="position:fixed;bottom:30px;left:30px;z-index:1000;
                background:white;padding:12px 16px;border-radius:10px;
                box-shadow:0 2px 8px rgba(0,0,0,0.15);font-family:sans-serif;font-size:13px">
      <b style="font-size:14px">CityMetric Clusters</b><br><br>
    """
    for c in sorted(cluster_names):
        col = CLUSTER_COLORS.get(c, "#CCC")
        legend_html += (f'<span style="display:inline-block;width:14px;height:14px;'
                        f'border-radius:50%;background:{col};margin-right:6px;'
                        f'vertical-align:middle"></span>{cluster_names[c]}<br>')
    legend_html += "</div>"
    m.get_root().html.add_child(folium.Element(legend_html))

    folium.LayerControl(collapsed=False).add_to(m)

    out = VIZ_DIR / "citymetric_map_interactive.html"
    m.save(str(out))
    print(f"    Saved: {out.name}  ({out.stat().st_size/1024:.0f} KB)")


# ═══════════════════════════════════════════════════════════════════════════════
# B — PLOTLY CHARTS (saved as interactive HTML)
# ═══════════════════════════════════════════════════════════════════════════════

def make_plotly_charts(df):
    print("\n[B] Building Plotly interactive charts...")
    import plotly.graph_objects as go
    import plotly.express as px
    from plotly.subplots import make_subplots

    cluster_names = df.groupby("cluster")["cluster_name"].first().to_dict()
    color_map     = {row["cluster_name"]: CLUSTER_COLORS[row["cluster"]]
                     for _, row in df.iterrows()}

    # ── B1: Radar charts — one per cluster ───────────────────────────────────
    print("    B1: Radar charts...")
    fig = make_subplots(
        rows=1, cols=5,
        specs=[[{"type":"polar"}]*5],
        subplot_titles=[f"C{c}: {cluster_names[c]}" for c in sorted(cluster_names)],
    )
    for i, c in enumerate(sorted(cluster_names), start=1):
        sub   = df[df["cluster"] == c]
        vals  = sub[DIMS].mean().tolist()
        vals += vals[:1]
        cats  = DIM_LABELS + [DIM_LABELS[0]]
        color = CLUSTER_COLORS.get(c, "#CCC")
        # Convert hex to rgba for Plotly fill opacity
        r_val = int(color[1:3], 16)
        g_val = int(color[3:5], 16)
        b_val = int(color[5:7], 16)
        fill_rgba = f"rgba({r_val},{g_val},{b_val},0.45)"
        fig.add_trace(
            go.Scatterpolar(
                r=vals, theta=cats, fill="toself",
                name=cluster_names[c],
                line_color=CLUSTER_COLORS_DARK.get(c, "#999"),
                fillcolor=fill_rgba,
                hovertemplate="%{theta}: %{r:.2f}<extra>" + cluster_names[c] + "</extra>",
            ), row=1, col=i
        )
        fig.update_layout(**{f"polar{i if i>1 else ''}": dict(radialaxis=dict(range=[0,10], tickfont_size=8))})

    fig.update_layout(
        title=dict(text="CityMetric — Cluster Dimension Profiles", font_size=16, x=0.5),
        showlegend=False,
        paper_bgcolor="#FFF0F8",
        height=450, width=1200,
    )
    out = VIZ_DIR / "plotly_radar_clusters.html"
    fig.write_html(str(out))
    print(f"      Saved: {out.name}")

    # ── B2: Scatter — Digital vs Innovation, sized by talent ─────────────────
    print("    B2: Scatter plots...")
    fig2 = px.scatter(
        df, x="digital_score", y="innovation_score",
        size="talent_score", color="cluster_name",
        color_discrete_map=color_map,
        text="city", hover_data=["country", "opportunity_index"],
        title="Digital vs Innovation (bubble = Talent Score)",
        labels={"digital_score": "Digital Score",
                "innovation_score": "Innovation Score",
                "cluster_name": "Cluster"},
        template="plotly_white",
    )
    fig2.update_traces(textposition="top center", textfont_size=9)
    fig2.update_layout(paper_bgcolor="#FFF8FC", height=550)
    out2 = VIZ_DIR / "plotly_scatter_digital_innovation.html"
    fig2.write_html(str(out2))
    print(f"      Saved: {out2.name}")

    # ── B3: Scatter — Affordability vs Opportunity ────────────────────────────
    fig3 = px.scatter(
        df, x="affordability_score", y="opportunity_index",
        color="cluster_name", color_discrete_map=color_map,
        text="city", size="growth_score",
        hover_data=["country","digital_score","innovation_score"],
        title="Affordability vs Opportunity (bubble = Growth Score)",
        labels={"affordability_score":"Affordability","opportunity_index":"Opportunity Index"},
        template="plotly_white",
    )
    fig3.update_traces(textposition="top center", textfont_size=9)
    fig3.update_layout(paper_bgcolor="#FFF8FC", height=550)
    out3 = VIZ_DIR / "plotly_scatter_afford_opportunity.html"
    fig3.write_html(str(out3))
    print(f"      Saved: {out3.name}")

    # ── B4: Horizontal bar — Top 20 cities ────────────────────────────────────
    print("    B4: Rankings bar chart...")
    top20 = df.nlargest(20, "opportunity_index").sort_values("opportunity_index")
    fig4  = px.bar(
        top20, x="opportunity_index", y="city",
        color="cluster_name", color_discrete_map=color_map,
        orientation="h", text="opportunity_index",
        hover_data=["country","affordability_score","digital_score","innovation_score"],
        title="Top 20 Cities — Opportunity Index",
        labels={"opportunity_index":"Opportunity Index","city":"","cluster_name":"Cluster"},
        template="plotly_white",
    )
    fig4.update_traces(texttemplate="%{x:.2f}", textposition="outside")
    fig4.update_layout(paper_bgcolor="#FFF8FC", height=600, showlegend=True)
    out4 = VIZ_DIR / "plotly_top20_ranking.html"
    fig4.write_html(str(out4))
    print(f"      Saved: {out4.name}")

    # ── B5: Heatmap — correlation matrix ──────────────────────────────────────
    print("    B5: Correlation heatmap...")
    corr  = df[DIMS + ["opportunity_index"]].corr().round(2)
    labels = DIM_LABELS + ["Opportunity"]
    fig5  = go.Figure(go.Heatmap(
        z=corr.values, x=labels, y=labels,
        colorscale=[[0,"#B4D7FF"],[0.5,"white"],[1,"#FFB6D9"]],
        zmin=-1, zmax=1,
        text=corr.values.round(2),
        texttemplate="%{text}",
        hovertemplate="%{y} × %{x}: %{z:.2f}<extra></extra>",
    ))
    fig5.update_layout(
        title=dict(text="Dimension Correlation Matrix", font_size=15, x=0.5),
        paper_bgcolor="#FFF8FC",
        height=500, width=600,
    )
    out5 = VIZ_DIR / "plotly_correlation_heatmap.html"
    fig5.write_html(str(out5))
    print(f"      Saved: {out5.name}")

    # ── B6: Box plots — score distributions per cluster ───────────────────────
    print("    B6: Box plots...")
    df_melt = df.melt(
        id_vars=["city","cluster_name"],
        value_vars=DIMS,
        var_name="dimension", value_name="score",
    )
    df_melt["dimension"] = df_melt["dimension"].str.replace("_score","").str.title()
    fig6 = px.box(
        df_melt, x="dimension", y="score",
        color="cluster_name", color_discrete_map=color_map,
        points="all", hover_data=["city"],
        title="Score Distribution by Cluster and Dimension",
        labels={"dimension":"Dimension","score":"Score (0-10)","cluster_name":"Cluster"},
        template="plotly_white",
    )
    fig6.update_layout(paper_bgcolor="#FFF8FC", height=550, boxmode="group")
    out6 = VIZ_DIR / "plotly_boxplots_dimensions.html"
    fig6.write_html(str(out6))
    print(f"      Saved: {out6.name}")

    # ── B7: Stacked bar — dimension breakdown per city (top 20) ───────────────
    print("    B7: Dimension breakdown stacked bar...")
    top20_full = df.nlargest(20, "opportunity_index").sort_values("opportunity_index", ascending=True)
    fig7 = go.Figure()
    bar_colors = ["#FFB6D9","#C8A2E8","#B4D7FF","#FFE8B6","#B4FFD7","#D5EEB4"]
    for dim, label, col in zip(DIMS, DIM_LABELS, bar_colors):
        fig7.add_trace(go.Bar(
            name=label,
            x=top20_full[dim],
            y=top20_full["city"],
            orientation="h",
            marker_color=col,
            hovertemplate=f"<b>%{{y}}</b><br>{label}: %{{x:.2f}}<extra></extra>",
        ))
    fig7.update_layout(
        barmode="stack",
        title=dict(text="Top 20 Cities — Dimension Breakdown", font_size=15, x=0.5),
        xaxis_title="Combined Score",
        paper_bgcolor="#FFF8FC",
        height=580, template="plotly_white",
        legend=dict(orientation="h", yanchor="bottom", y=1.01, xanchor="center", x=0.5),
    )
    out7 = VIZ_DIR / "plotly_dimension_breakdown.html"
    fig7.write_html(str(out7))
    print(f"      Saved: {out7.name}")


# ═══════════════════════════════════════════════════════════════════════════════
# C — STATIC MATPLOTLIB SUMMARY POSTER (for reports/PDF)
# ═══════════════════════════════════════════════════════════════════════════════

def make_summary_poster(df):
    print("\n[C] Building static summary poster...")

    fig = plt.figure(figsize=(18, 12))
    fig.patch.set_facecolor("#FFF0F8")
    fig.suptitle("CityMetric — Global City Opportunity & Innovation Index",
                 fontsize=18, fontweight="bold", y=0.98)

    # ── C1: Top 15 bar ────────────────────────────────────────────────────────
    ax1 = fig.add_subplot(2, 3, 1)
    top15 = df.nlargest(15, "opportunity_index").sort_values("opportunity_index")
    colors = [CLUSTER_COLORS.get(c, "#CCC") for c in top15["cluster"]]
    ax1.barh(top15["city"], top15["opportunity_index"], color=colors, edgecolor="white")
    ax1.set_xlabel("Opportunity Index", fontsize=9)
    ax1.set_title("Top 15 Cities", fontweight="bold")
    ax1.set_facecolor("#FFF8FC")
    ax1.grid(axis="x", alpha=0.3)
    for i, (v, city) in enumerate(zip(top15["opportunity_index"], top15["city"])):
        ax1.text(v + 0.03, i, f"{v:.2f}", va="center", fontsize=7)

    # ── C2: Cluster sizes pie ─────────────────────────────────────────────────
    ax2 = fig.add_subplot(2, 3, 2)
    cluster_counts = df.groupby("cluster_name").size()
    pie_colors     = [CLUSTER_COLORS[df.loc[df["cluster_name"]==n,"cluster"].iloc[0]]
                      for n in cluster_counts.index]
    wedges, texts, autotexts = ax2.pie(
        cluster_counts, labels=cluster_counts.index,
        colors=pie_colors, autopct="%1.0f%%",
        startangle=90, pctdistance=0.75,
        wedgeprops=dict(edgecolor="white", linewidth=1.5),
    )
    for t in texts:    t.set_fontsize(8)
    for t in autotexts: t.set_fontsize(8)
    ax2.set_title("Cluster Distribution", fontweight="bold")

    # ── C3: Regional average bar ──────────────────────────────────────────────
    ax3 = fig.add_subplot(2, 3, 3)
    reg = df.groupby("region")["opportunity_index"].mean().sort_values(ascending=True)
    reg_colors = ["#FFB6D9","#C8A2E8","#B4D7FF","#FFE8B6","#B4FFD7"][:len(reg)]
    ax3.barh(reg.index, reg.values, color=reg_colors, edgecolor="white")
    ax3.set_xlabel("Avg Opportunity Index", fontsize=9)
    ax3.set_title("Regional Averages", fontweight="bold")
    ax3.set_facecolor("#FFF8FC")
    ax3.grid(axis="x", alpha=0.3)
    for i, v in enumerate(reg.values):
        ax3.text(v + 0.02, i, f"{v:.2f}", va="center", fontsize=8)

    # ── C4: Scatter affordability vs opportunity ───────────────────────────────
    ax4 = fig.add_subplot(2, 3, 4)
    for c in sorted(df["cluster"].unique()):
        sub = df[df["cluster"] == c]
        ax4.scatter(sub["affordability_score"], sub["opportunity_index"],
                    c=CLUSTER_COLORS[c], s=60, alpha=0.85,
                    edgecolors="white", linewidth=0.6,
                    label=sub["cluster_name"].iloc[0])
    ax4.set_xlabel("Affordability Score", fontsize=9)
    ax4.set_ylabel("Opportunity Index", fontsize=9)
    ax4.set_title("Affordability vs Opportunity", fontweight="bold")
    ax4.legend(fontsize=6, loc="lower right")
    ax4.set_facecolor("#FFF8FC")
    ax4.grid(alpha=0.25)

    # ── C5: Correlation heatmap ───────────────────────────────────────────────
    ax5 = fig.add_subplot(2, 3, 5)
    corr = df[DIMS].corr()
    im   = ax5.imshow(corr, cmap="RdYlBu_r", vmin=-1, vmax=1, aspect="auto")
    ax5.set_xticks(range(len(DIM_LABELS)))
    ax5.set_yticks(range(len(DIM_LABELS)))
    short = ["Afford","Digital","Urban","Innov","Talent","Growth"]
    ax5.set_xticklabels(short, rotation=40, ha="right", fontsize=8)
    ax5.set_yticklabels(short, fontsize=8)
    for i in range(len(DIMS)):
        for j in range(len(DIMS)):
            ax5.text(j, i, f"{corr.iloc[i,j]:.2f}", ha="center", va="center", fontsize=7)
    ax5.set_title("Dimension Correlations", fontweight="bold")
    plt.colorbar(im, ax=ax5, shrink=0.8)

    # ── C6: Score stats summary table ────────────────────────────────────────
    ax6 = fig.add_subplot(2, 3, 6)
    ax6.axis("off")
    stats_data = []
    for dim, label in zip(DIMS, DIM_LABELS):
        row_d = [label,
                 f"{df[dim].mean():.2f}",
                 f"{df[dim].std():.2f}",
                 f"{df[dim].min():.2f}",
                 f"{df[dim].max():.2f}",
                 df.loc[df[dim].idxmax(), "city"]]
        stats_data.append(row_d)
    tbl = ax6.table(
        cellText=stats_data,
        colLabels=["Dimension","Mean","Std","Min","Max","Top City"],
        cellLoc="center", loc="center",
        bbox=[0, 0, 1, 1],
    )
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(8)
    for (r, c), cell in tbl.get_celld().items():
        cell.set_edgecolor("#E0D0F0")
        if r == 0:
            cell.set_facecolor("#C8A2E8")
            cell.set_text_props(fontweight="bold", color="white")
        else:
            cell.set_facecolor("#FFF8FC" if r % 2 == 0 else "white")
    ax6.set_title("Dimension Statistics", fontweight="bold", pad=10)

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    out = VIZ_DIR / "citymetric_summary_poster.png"
    plt.savefig(out, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"    Saved: {out.name}  ({out.stat().st_size/1024:.0f} KB)")


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    print("=" * 60)
    print("  CityMetric — Phase 4: Visualization")
    print("=" * 60)

    df = pd.read_csv(PROC_OUT / "cities_clustered.csv")
    print(f"  Loaded cities_clustered.csv: {len(df)} cities, {df['cluster'].nunique()} clusters")

    make_folium_map(df)
    make_plotly_charts(df)
    make_summary_poster(df)

    print("\n" + "=" * 60)
    print("  Phase 4 COMPLETE")
    print(f"  All outputs in: {VIZ_DIR}")
    print()
    for f in sorted(VIZ_DIR.iterdir()):
        print(f"    {f.name:<50} {f.stat().st_size/1024:>7.1f} KB")
    print("=" * 60)
    print("\n  Next step: run scripts/05_streamlit_app.py")


if __name__ == "__main__":
    main()
