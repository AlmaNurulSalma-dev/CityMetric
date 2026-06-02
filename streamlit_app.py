"""
CityMetric — Global City Opportunity & Innovation Index
Streamlit Dashboard (Phase 5)
"""

import warnings
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pathlib import Path

warnings.filterwarnings("ignore")

# ─── Page config (must be first Streamlit call) ───────────────────────────────
st.set_page_config(
    page_title="CityMetric",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Paths ────────────────────────────────────────────────────────────────────
ROOT     = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data" / "processed"
OUT_DIR  = ROOT / "output"

# ─── Colours ──────────────────────────────────────────────────────────────────
CLUSTER_COLORS = {
    0: "#FFB6D9", 1: "#C8A2E8", 2: "#B4D7FF", 3: "#FFE8B6", 4: "#B4FFD7",
}
CLUSTER_DARK = {
    0: "#E8669A", 1: "#9B59B6", 2: "#5B9BD5", 3: "#E8A020", 4: "#27AE60",
}
DIMS        = ["affordability_score","digital_score","urban_score",
               "innovation_score","talent_score","growth_score"]
DIM_LABELS  = ["Affordability","Digital","Urban","Innovation","Talent","Growth"]
DIM_EMOJI   = ["💰","📡","🏙️","💡","👩‍💻","📈"]

# ─── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
  /* Background */
  .stApp { background: linear-gradient(135deg, #fff0f8 0%, #f5f0ff 100%); }
  /* Metric cards */
  [data-testid="stMetric"] {
      background: white; border-radius: 12px; padding: 12px 16px;
      box-shadow: 0 2px 8px rgba(200,162,232,0.18);
  }
  /* Sidebar */
  [data-testid="stSidebar"] { background: #2d1b4e; }
  [data-testid="stSidebar"] * { color: #f0e8ff !important; }
  [data-testid="stSidebar"] .stSelectbox label,
  [data-testid="stSidebar"] .stMultiSelect label,
  [data-testid="stSidebar"] .stSlider label { color: #d4b8ff !important; }
  /* Title */
  h1 { color: #6b21a8 !important; }
  h2, h3 { color: #7c3aed !important; }
  /* Tab active */
  .stTabs [aria-selected="true"] {
      background: #c8a2e8; color: white; border-radius: 8px 8px 0 0;
  }
</style>
""", unsafe_allow_html=True)


# ─── Data loader ─────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv(DATA_DIR / "cities_clustered.csv")
    return df

df_all = load_data()


# ═══════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ═══════════════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("## 🌍 CityMetric")
    st.markdown("*Measure Your City, Measure Your Future*")
    st.markdown("---")

    st.markdown("### Filters")

    all_clusters  = sorted(df_all["cluster"].unique())
    cluster_names = df_all.groupby("cluster")["cluster_name"].first().to_dict()
    sel_clusters  = st.multiselect(
        "Cluster",
        options=all_clusters,
        default=all_clusters,
        format_func=lambda c: f"C{c}: {cluster_names[c]}",
    )

    all_regions  = sorted(df_all["region"].unique())
    sel_regions  = st.multiselect("Region", options=all_regions, default=all_regions)

    opp_range = st.slider("Opportunity Index", 0.0, 10.0, (0.0, 10.0), 0.1)

    st.markdown("---")
    st.markdown("### Highlight Dimension")
    highlight = st.selectbox(
        "Color map by",
        ["opportunity_index"] + DIMS,
        format_func=lambda x: x.replace("_score","").replace("_"," ").title(),
    )

    st.markdown("---")
    st.markdown("### Pages")
    page = st.radio("Navigate", [
        "🏠 Overview",
        "🗺️ World Map",
        "📊 Cluster Analysis",
        "🔍 Dimension Deep-Dive",
        "🔄 City Comparison",
        "🚀 Insights",
        "📖 About",
    ])

# ─── Apply filters ────────────────────────────────────────────────────────────
df = df_all[
    df_all["cluster"].isin(sel_clusters) &
    df_all["region"].isin(sel_regions) &
    df_all["opportunity_index"].between(*opp_range)
].copy()

color_map = {cluster_names[c]: CLUSTER_COLORS[c] for c in all_clusters}


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: OVERVIEW
# ═══════════════════════════════════════════════════════════════════════════════
if page == "🏠 Overview":
    st.title("🌍 CityMetric — Global City Opportunity & Innovation Index")
    st.markdown(
        "Data-driven analysis of **55 global cities** across **6 key dimensions** — "
        "find where to build, invest, or move."
    )
    st.markdown("---")

    # ── KPI row ──────────────────────────────────────────────────────────────
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Cities Analysed",   f"{len(df_all)}")
    c2.metric("Clusters Found",    f"{df_all['cluster'].nunique()}")
    c3.metric("Avg Opportunity",   f"{df['opportunity_index'].mean():.2f}/10")
    c4.metric("Top City",          df_all.loc[df_all['opportunity_index'].idxmax(), 'city'])
    c5.metric("Data Sources",      "8+")
    st.markdown("---")

    col_left, col_right = st.columns([3, 2])

    with col_left:
        st.subheader("Top 20 Cities")
        top20 = df.nlargest(20, "opportunity_index").sort_values("opportunity_index")
        fig = px.bar(
            top20, x="opportunity_index", y="city",
            color="cluster_name", color_discrete_map=color_map,
            orientation="h", text="opportunity_index",
            labels={"opportunity_index": "Opportunity Index", "city": "", "cluster_name": "Cluster"},
            template="plotly_white",
        )
        fig.update_traces(texttemplate="%{x:.2f}", textposition="outside")
        fig.update_layout(
            height=520, paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(255,255,255,0.6)",
            legend=dict(orientation="h", y=-0.15),
            showlegend=True,
        )
        st.plotly_chart(fig, use_container_width=True)

    with col_right:
        st.subheader("Cluster Distribution")
        counts = df.groupby("cluster_name").size().reset_index(name="count")
        fig2 = px.pie(
            counts, values="count", names="cluster_name",
            color="cluster_name", color_discrete_map=color_map,
            hole=0.45, template="plotly_white",
        )
        fig2.update_traces(textposition="inside", textinfo="percent+label",
                           marker=dict(line=dict(color="white", width=2)))
        fig2.update_layout(
            height=280, paper_bgcolor="rgba(0,0,0,0)",
            showlegend=False, margin=dict(t=10, b=10),
        )
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Regional Averages")
        reg = (df.groupby("region")["opportunity_index"]
               .mean().sort_values(ascending=True).reset_index())
        fig3 = px.bar(
            reg, x="opportunity_index", y="region",
            orientation="h", template="plotly_white",
            color="opportunity_index",
            color_continuous_scale=["#B4D7FF","#C8A2E8","#FFB6D9"],
            labels={"opportunity_index": "Avg Score", "region": ""},
        )
        fig3.update_layout(
            height=230, paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(255,255,255,0.6)",
            coloraxis_showscale=False, margin=dict(t=0, b=0),
        )
        st.plotly_chart(fig3, use_container_width=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: WORLD MAP
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "🗺️ World Map":
    st.title("🗺️ City Intelligence Map")

    # Cluster colour legend
    legend_cols = st.columns(5)
    for i, (c, name) in enumerate(cluster_names.items()):
        legend_cols[i].markdown(
            f'<span style="background:{CLUSTER_COLORS[c]};padding:4px 12px;'
            f'border-radius:12px;font-size:12px;font-weight:600">'
            f'C{c}: {name}</span>',
            unsafe_allow_html=True,
        )
    st.markdown("")

    tab1, tab2, tab3 = st.tabs(["🗺️ Interactive Map", "🌐 3D Globe", "🔥 Heatmap"])

    # ── TAB 1: Plotly Mapbox ─────────────────────────────────────────────────
    with tab1:
        st.caption("Hover over any city for details · Zoom & pan · Click legend to filter clusters")

        # Build hover text with all scores
        df["hover_text"] = df.apply(
            lambda r: (
                f"<b>{r['city']}, {r['country']}</b><br>"
                f"Cluster: {r['cluster_name']}<br>"
                f"Opportunity: {r['opportunity_index']:.2f}/10<br>"
                f"─────────────────<br>"
                f"Affordability: {r['affordability_score']:.1f} &nbsp;"
                f"Digital: {r['digital_score']:.1f}<br>"
                f"Urban: {r['urban_score']:.1f} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                f"Innovation: {r['innovation_score']:.1f}<br>"
                f"Talent: {r['talent_score']:.1f} &nbsp;&nbsp;&nbsp;&nbsp;"
                f"Growth: {r['growth_score']:.1f}"
            ), axis=1
        )

        fig_map = px.scatter_mapbox(
            df,
            lat="latitude", lon="longitude",
            color="cluster_name",
            color_discrete_map=color_map,
            size="opportunity_index",
            size_max=22,
            hover_name="city",
            custom_data=["hover_text"],
            zoom=1.5,
            center={"lat": 20, "lon": 10},
            mapbox_style="open-street-map",
            template="plotly_white",
            height=580,
        )
        fig_map.update_traces(
            hovertemplate="%{customdata[0]}<extra></extra>",
            marker=dict(opacity=0.85, sizemin=6),
        )
        fig_map.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=0, r=0, t=0, b=0),
            legend=dict(
                title="Cluster",
                bgcolor="rgba(255,255,255,0.85)",
                bordercolor="#E0D0F0",
                borderwidth=1,
                x=0.01, y=0.99,
            ),
        )
        st.plotly_chart(fig_map, use_container_width=True)

    # ── TAB 2: PyDeck 3D Globe ───────────────────────────────────────────────
    with tab2:
        st.caption("Drag to rotate · Scroll to zoom · Hover for city info · Column height = Opportunity Index")
        import pydeck as pdk

        # Hex colours → [R, G, B] for pydeck
        def hex_to_rgb(h):
            h = h.lstrip("#")
            return [int(h[i:i+2], 16) for i in (0, 2, 4)]

        df_deck = df.copy()
        df_deck["color"]       = df_deck["cluster"].map(lambda c: hex_to_rgb(CLUSTER_COLORS[c]))
        df_deck["color_dark"]  = df_deck["cluster"].map(lambda c: hex_to_rgb(CLUSTER_DARK[c]))
        df_deck["elevation"]   = df_deck["opportunity_index"] * 120000
        df_deck["radius"]      = df_deck["opportunity_index"] * 60000 + 80000

        column_layer = pdk.Layer(
            "ColumnLayer",
            data=df_deck,
            get_position=["longitude", "latitude"],
            get_elevation="elevation",
            elevation_scale=1,
            radius=80000,
            get_fill_color="color",
            pickable=True,
            auto_highlight=True,
            extruded=True,
        )

        scatter_layer = pdk.Layer(
            "ScatterplotLayer",
            data=df_deck,
            get_position=["longitude", "latitude"],
            get_radius="radius",
            get_fill_color="color",
            get_line_color="color_dark",
            line_width_min_pixels=1,
            pickable=True,
            opacity=0.5,
        )

        view = pdk.ViewState(
            latitude=20, longitude=10,
            zoom=1.2, pitch=45, bearing=0,
        )

        tooltip = {
            "html": (
                "<b>{city}, {country}</b><br/>"
                "Cluster: {cluster_name}<br/>"
                "Opportunity: {opportunity_index}/10<br/>"
                "Afford: {affordability_score} | Digital: {digital_score}<br/>"
                "Innovation: {innovation_score} | Talent: {talent_score}"
            ),
            "style": {
                "background": "rgba(50,20,80,0.92)",
                "color": "#fff",
                "font-family": "sans-serif",
                "font-size": "13px",
                "padding": "10px",
                "border-radius": "8px",
            },
        }

        deck = pdk.Deck(
            layers=[scatter_layer, column_layer],
            initial_view_state=view,
            tooltip=tooltip,
            map_style="mapbox://styles/mapbox/dark-v10",
        )
        st.pydeck_chart(deck, use_container_width=True, height=580)

    # ── TAB 3: Heatmap ───────────────────────────────────────────────────────
    with tab3:
        st.caption(f"Heatmap intensity = {highlight.replace('_',' ').replace('score','').title().strip()} score")

        dim_choice = st.selectbox(
            "Heatmap dimension",
            ["opportunity_index"] + DIMS,
            format_func=lambda x: x.replace("_score","").replace("_"," ").title(),
            key="heatmap_dim",
        )

        fig_heat = px.density_mapbox(
            df,
            lat="latitude", lon="longitude",
            z=dim_choice,
            radius=60,
            zoom=1.3,
            center={"lat": 20, "lon": 10},
            mapbox_style="carto-darkmatter",
            color_continuous_scale=["#1a0533","#C8A2E8","#FFB6D9","#FFE8B6"],
            template="plotly_white",
            height=560,
            hover_name="city",
            hover_data={"latitude":False,"longitude":False,dim_choice:":.2f"},
        )
        fig_heat.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=0, r=0, t=0, b=0),
            coloraxis_colorbar=dict(title=dim_choice.replace("_score","").title()),
        )
        st.plotly_chart(fig_heat, use_container_width=True)

        # Scatter overlay on top of heatmap context
        st.caption("City positions for reference:")
        fig_over = px.scatter_mapbox(
            df, lat="latitude", lon="longitude",
            color=dim_choice, size=dim_choice,
            size_max=18, zoom=1.3,
            center={"lat": 20, "lon": 10},
            hover_name="city",
            hover_data={dim_choice:":.2f","cluster_name":True,
                        "latitude":False,"longitude":False},
            mapbox_style="carto-positron",
            color_continuous_scale=["#B4D7FF","#C8A2E8","#FFB6D9"],
            template="plotly_white", height=420,
        )
        fig_over.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=0, r=0, t=0, b=0),
        )
        st.plotly_chart(fig_over, use_container_width=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: CLUSTER ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "📊 Cluster Analysis":
    st.title("📊 Cluster Analysis")

    sel_c = st.selectbox(
        "Select cluster to explore",
        options=all_clusters,
        format_func=lambda c: f"C{c}: {cluster_names[c]}",
    )
    cdata = df_all[df_all["cluster"] == sel_c]
    color = CLUSTER_COLORS[sel_c]

    # KPIs
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Cities",         len(cdata))
    k2.metric("Avg Opportunity", f"{cdata['opportunity_index'].mean():.2f}")
    k3.metric("Avg Affordability", f"{cdata['affordability_score'].mean():.2f}")
    k4.metric("Avg Growth",     f"{cdata['growth_score'].mean():.2f}")

    col1, col2 = st.columns([1, 1])

    with col1:
        # Radar
        means  = cdata[DIMS].mean().tolist()
        means += means[:1]
        cats   = DIM_LABELS + [DIM_LABELS[0]]
        r_val  = int(color[1:3], 16)
        g_val  = int(color[3:5], 16)
        b_val  = int(color[5:7], 16)
        fig_r = go.Figure(go.Scatterpolar(
            r=means, theta=cats, fill="toself",
            line_color=CLUSTER_DARK[sel_c],
            fillcolor=f"rgba({r_val},{g_val},{b_val},0.4)",
            name=cluster_names[sel_c],
        ))
        fig_r.update_layout(
            polar=dict(radialaxis=dict(range=[0,10])),
            title=f"C{sel_c}: {cluster_names[sel_c]} — Dimension Profile",
            paper_bgcolor="rgba(0,0,0,0)", height=350,
        )
        st.plotly_chart(fig_r, use_container_width=True)

    with col2:
        st.subheader(f"Cities in C{sel_c}: {cluster_names[sel_c]}")
        show_cols = ["city","country","opportunity_index"] + DIMS
        st.dataframe(
            cdata[show_cols].sort_values("opportunity_index", ascending=False)
                .reset_index(drop=True)
                .style.background_gradient(subset=["opportunity_index"], cmap="RdYlGn"),
            use_container_width=True, height=300,
        )

    st.markdown("---")
    st.subheader("All Clusters — Side-by-Side Radar")
    fig_all = make_subplots(rows=1, cols=5,
                            specs=[[{"type":"polar"}]*5],
                            subplot_titles=[f"C{c}: {cluster_names[c]}" for c in all_clusters])
    for i, c in enumerate(all_clusters, start=1):
        sub   = df_all[df_all["cluster"]==c]
        vals  = sub[DIMS].mean().tolist() + [sub[DIMS[0]].mean()]
        cats2 = DIM_LABELS + [DIM_LABELS[0]]
        col2  = CLUSTER_COLORS[c]
        rv, gv, bv = int(col2[1:3],16), int(col2[3:5],16), int(col2[5:7],16)
        fig_all.add_trace(
            go.Scatterpolar(r=vals, theta=cats2, fill="toself",
                            line_color=CLUSTER_DARK[c],
                            fillcolor=f"rgba({rv},{gv},{bv},0.4)",
                            name=cluster_names[c]),
            row=1, col=i,
        )
        polar_key = "polar" if i == 1 else f"polar{i}"
        fig_all.update_layout(**{polar_key: dict(radialaxis=dict(range=[0,10],tickfont_size=7))})
    fig_all.update_layout(
        height=340, paper_bgcolor="rgba(0,0,0,0)", showlegend=False,
    )
    st.plotly_chart(fig_all, use_container_width=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: DIMENSION DEEP-DIVE
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "🔍 Dimension Deep-Dive":
    st.title("🔍 Dimension Deep-Dive")

    sel_dim = st.selectbox(
        "Select dimension",
        options=DIMS,
        format_func=lambda x: x.replace("_score","").title(),
    )
    label = sel_dim.replace("_score","").title()

    col1, col2 = st.columns([3, 2])
    with col1:
        top_dim = df.nlargest(20, sel_dim).sort_values(sel_dim)
        fig = px.bar(
            top_dim, x=sel_dim, y="city",
            color="cluster_name", color_discrete_map=color_map,
            orientation="h", text=sel_dim,
            title=f"Top 20 Cities — {label} Score",
            labels={sel_dim: f"{label} Score", "city": ""},
            template="plotly_white",
        )
        fig.update_traces(texttemplate="%{x:.2f}", textposition="outside")
        fig.update_layout(height=520, paper_bgcolor="rgba(0,0,0,0)",
                          plot_bgcolor="rgba(255,255,255,0.6)")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Regional Average")
        reg_dim = (df.groupby("region")[sel_dim]
                   .mean().sort_values(ascending=True).reset_index())
        fig2 = px.bar(
            reg_dim, x=sel_dim, y="region", orientation="h",
            color=sel_dim, color_continuous_scale=["#B4D7FF","#C8A2E8","#FFB6D9"],
            template="plotly_white",
            labels={sel_dim: f"{label} Score", "region": ""},
        )
        fig2.update_layout(height=250, paper_bgcolor="rgba(0,0,0,0)",
                           coloraxis_showscale=False)
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Distribution by Cluster")
        fig3 = px.box(
            df, x="cluster_name", y=sel_dim,
            color="cluster_name", color_discrete_map=color_map,
            points="all", hover_data=["city"],
            template="plotly_white",
            labels={sel_dim: f"{label} Score", "cluster_name": ""},
        )
        fig3.update_layout(height=280, paper_bgcolor="rgba(0,0,0,0)",
                           showlegend=False)
        st.plotly_chart(fig3, use_container_width=True)

    st.markdown("---")
    st.subheader("Correlation Matrix")
    corr = df[DIMS].corr().round(2)
    fig4 = go.Figure(go.Heatmap(
        z=corr.values, x=DIM_LABELS, y=DIM_LABELS,
        colorscale=[[0,"#B4D7FF"],[0.5,"white"],[1,"#FFB6D9"]],
        zmin=-1, zmax=1,
        text=corr.values, texttemplate="%{text:.2f}",
        hovertemplate="%{y} × %{x}: %{z:.2f}<extra></extra>",
    ))
    fig4.update_layout(
        height=380, width=550, paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=10, r=10, t=10, b=10),
    )
    st.plotly_chart(fig4)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: CITY COMPARISON
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "🔄 City Comparison":
    st.title("🔄 City Comparison Tool")

    default_cities = ["Bangkok", "Lisbon", "Singapore", "Berlin", "Seoul"]
    cities_to_compare = st.multiselect(
        "Select 2–6 cities to compare",
        options=sorted(df_all["city"].unique()),
        default=[c for c in default_cities if c in df_all["city"].values],
    )

    if len(cities_to_compare) < 2:
        st.info("Please select at least 2 cities.")
    else:
        cmp = df_all[df_all["city"].isin(cities_to_compare)].copy()

        # ── Radar overlay ────────────────────────────────────────────────────
        st.subheader("Dimension Profile Overlay")
        fig_radar = go.Figure()
        palette = ["#FFB6D9","#C8A2E8","#B4D7FF","#FFE8B6","#B4FFD7","#D5EEB4"]
        for i, (_, row) in enumerate(cmp.iterrows()):
            vals  = [row[d] for d in DIMS] + [row[DIMS[0]]]
            cats  = DIM_LABELS + [DIM_LABELS[0]]
            col_i = palette[i % len(palette)]
            rv, gv, bv = int(col_i[1:3],16), int(col_i[3:5],16), int(col_i[5:7],16)
            fig_radar.add_trace(go.Scatterpolar(
                r=vals, theta=cats, fill="toself",
                name=row["city"],
                fillcolor=f"rgba({rv},{gv},{bv},0.25)",
                line=dict(width=2),
            ))
        fig_radar.update_layout(
            polar=dict(radialaxis=dict(range=[0,10])),
            height=420, paper_bgcolor="rgba(0,0,0,0)",
            legend=dict(orientation="h", y=-0.12),
        )
        st.plotly_chart(fig_radar, use_container_width=True)

        col1, col2 = st.columns(2)
        with col1:
            # ── Grouped bar ──────────────────────────────────────────────────
            st.subheader("Score Breakdown")
            melt = cmp.melt(id_vars=["city"],
                            value_vars=DIMS,
                            var_name="dimension", value_name="score")
            melt["dimension"] = melt["dimension"].str.replace("_score","").str.title()
            fig_bar = px.bar(
                melt, x="dimension", y="score", color="city",
                barmode="group", template="plotly_white",
                labels={"dimension":"","score":"Score (0–10)"},
            )
            fig_bar.update_layout(height=320, paper_bgcolor="rgba(0,0,0,0)",
                                  legend=dict(orientation="h",y=-0.2))
            st.plotly_chart(fig_bar, use_container_width=True)

        with col2:
            # ── Summary table ────────────────────────────────────────────────
            st.subheader("Summary Table")
            tbl_cols = ["city","country","cluster_name","opportunity_index"] + DIMS
            st.dataframe(
                cmp[tbl_cols].set_index("city")
                   .rename(columns={d: d.replace("_score","").title() for d in DIMS})
                   .T.style.background_gradient(cmap="RdYlGn", axis=1),
                use_container_width=True, height=320,
            )


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: INSIGHTS
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "🚀 Insights":
    st.title("🚀 Key Insights")

    # ── Best value, Rising Stars, Most Innovative ────────────────────────────
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### 💰 Best Value Cities")
        st.caption("High opportunity, high affordability")
        best = df_all.nlargest(20, "opportunity_index").nlargest(5, "affordability_score")
        for _, r in best.iterrows():
            c = CLUSTER_COLORS[r["cluster"]]
            st.markdown(
                f'<div style="background:{c};border-radius:8px;padding:8px 12px;margin:4px 0">'
                f'<b>{r["city"]}</b> — {r["country"]}<br>'
                f'Score: {r["opportunity_index"]:.2f}  |  Afford: {r["affordability_score"]:.2f}'
                f'</div>', unsafe_allow_html=True,
            )
    with col2:
        st.markdown("#### 📈 Rising Stars")
        st.caption("Highest growth potential")
        stars = df_all.nlargest(5, "growth_score")
        for _, r in stars.iterrows():
            c = CLUSTER_COLORS[r["cluster"]]
            st.markdown(
                f'<div style="background:{c};border-radius:8px;padding:8px 12px;margin:4px 0">'
                f'<b>{r["city"]}</b> — {r["country"]}<br>'
                f'Growth: {r["growth_score"]:.2f}  |  Opp: {r["opportunity_index"]:.2f}'
                f'</div>', unsafe_allow_html=True,
            )
    with col3:
        st.markdown("#### 💡 Innovation Leaders")
        st.caption("Highest innovation score")
        innov = df_all.nlargest(5, "innovation_score")
        for _, r in innov.iterrows():
            c = CLUSTER_COLORS[r["cluster"]]
            st.markdown(
                f'<div style="background:{c};border-radius:8px;padding:8px 12px;margin:4px 0">'
                f'<b>{r["city"]}</b> — {r["country"]}<br>'
                f'Innovation: {r["innovation_score"]:.2f}  |  Talent: {r["talent_score"]:.2f}'
                f'</div>', unsafe_allow_html=True,
            )

    st.markdown("---")
    # ── Scatter: Digital vs Innovation ───────────────────────────────────────
    st.subheader("Digital Infrastructure vs Innovation Readiness")
    fig = px.scatter(
        df_all, x="digital_score", y="innovation_score",
        color="cluster_name", color_discrete_map=color_map,
        size="talent_score", text="city",
        hover_data=["country","opportunity_index","growth_score"],
        template="plotly_white",
        labels={"digital_score":"Digital Score","innovation_score":"Innovation Score",
                "cluster_name":"Cluster"},
    )
    fig.update_traces(textposition="top center", textfont_size=8)
    fig.update_layout(height=480, paper_bgcolor="rgba(0,0,0,0)",
                      plot_bgcolor="rgba(255,255,255,0.6)")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    # ── Key findings text ────────────────────────────────────────────────────
    st.subheader("Key Findings")
    findings = [
        ("🌟", "Top opportunity cities",     "Los Angeles, New York, and San Francisco lead overall — driven by talent concentration and digital infrastructure."),
        ("💚", "Best value for tech workers","Melbourne, Sydney, and Tel Aviv offer high opportunity with better affordability than US cities."),
        ("📡", "Digital gap",                "Hong Kong and Singapore score near-perfect on digital (9.0), while African cities average below 3.0."),
        ("🚀", "Asia rising",                "Singapore, Hong Kong, and Seoul show the strongest growth trajectories in Asia-Pacific."),
        ("🏙️", "European balance",           "European cities (Paris, Berlin, Amsterdam) cluster together — balanced across all dimensions but no standout leader."),
        ("⚠️", "Innovation concentration",   "Top innovation scores heavily concentrated in USA and select EU cities — most of world still below 3.0."),
    ]
    for emoji, title, desc in findings:
        with st.expander(f"{emoji} {title}"):
            st.write(desc)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: ABOUT
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "📖 About":
    st.title("📖 About CityMetric")

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("""
        ### Overview
        **CityMetric** is a data-driven platform that analyses global cities across
        7 key dimensions to help answer: *"Where should you build, invest, or move?"*

        ### 6 Active Dimensions
        | # | Dimension | What it measures |
        |---|-----------|-----------------|
        | 1 | 💰 Affordability | Rent, salary, cost of living ratio |
        | 2 | 📡 Digital | Internet %, broadband, mobile penetration |
        | 3 | 🏙️ Urban | Population density, climate comfort, growth |
        | 4 | 💡 Innovation | R&D spending, research output, university quality |
        | 5 | 👩‍💻 Talent | Education enrollment, developer density, seniority |
        | 6 | 📈 Growth | GDP growth, population trend, tech exports |

        ### Methodology
        - **Data sources:** Numbeo, MaxMind World Cities, NOAA Temperature,
          World Bank API, Stack Overflow Survey, CWUR/Times/Shanghai Rankings
        - **Normalization:** Min-Max scaling (0–10) per dimension
        - **Clustering:** K-Means K=5 (sklearn / WEKA SimpleKMeans)
        - **Cities analyzed:** 55 major global cities

        ### Tech Stack
        `Python` · `pandas` · `scikit-learn` · `WEKA` · `Folium` · `Plotly` · `Streamlit`
        """)

    with col2:
        st.markdown("### Cluster Guide")
        for c in all_clusters:
            col_hex = CLUSTER_COLORS[c]
            cname   = cluster_names[c]
            cities  = df_all.loc[df_all["cluster"]==c, "city"].tolist()
            st.markdown(
                f'<div style="background:{col_hex};border-radius:10px;'
                f'padding:10px 14px;margin:6px 0">'
                f'<b>C{c}: {cname}</b><br>'
                f'<span style="font-size:12px">{", ".join(sorted(cities))}</span>'
                f'</div>', unsafe_allow_html=True,
            )

        st.markdown("---")
        st.markdown("### Author")
        st.markdown("""
        **Alma Nurul Salma**
        Informatics — UII & Nanjing Xiaozhuang University

        📧 almanurulsalma@gmail.com
        🔗 github.com/AlmaNurulSalma-dev
        """)


# ─── Footer ───────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    '<div style="text-align:center;color:#9b59b6;font-size:13px">'
    '🌍 CityMetric — Measure Your City, Measure Your Future &nbsp;|&nbsp; '
    'Data: Numbeo · World Bank · Stack Overflow · CWUR · NOAA'
    '</div>',
    unsafe_allow_html=True,
)
