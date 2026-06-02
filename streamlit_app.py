"""
CityMetric — Global City Opportunity & Innovation Index
Streamlit Dashboard v2 — Full UI/UX Revision
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

# ─── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CityMetric",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Paths ────────────────────────────────────────────────────────────────────
ROOT     = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data" / "processed"

# ─── Design System — Dark Mode ────────────────────────────────────────────────
PRIMARY      = "#C4B5FD"   # light lavender — headlines & accents on dark bg
PRIMARY_SOFT = "#3B2D6B"   # dark lavender tint — subtle fills
SIDEBAR_BG   = "#06040F"   # near-black with purple tint — sidebar
CARD_BG      = "#14102A"   # dark purple card surface
PAGE_BG      = "#0D0B1E"   # deep dark navy-purple — main background
TEXT_MAIN    = "#F1EEFF"   # near-white with slight lavender — primary text
TEXT_MUTED   = "#8B83B5"   # muted purple-grey — captions, labels
BORDER_COL   = "#2A2350"   # subtle dark border
GRID_COL     = "#231D45"   # chart gridlines

# Cluster palette: clearly distinct, accessible, still on-brand
CLUSTER_COLORS = {
    0: "#F9A8D4",   # pink
    1: "#A78BFA",   # violet
    2: "#67E8F9",   # cyan
    3: "#FCD34D",   # amber
    4: "#6EE7B7",   # emerald
}
CLUSTER_DARK = {
    0: "#DB2777",   # deep pink
    1: "#6D28D9",   # deep violet
    2: "#0891B2",   # deep cyan
    3: "#D97706",   # deep amber
    4: "#059669",   # deep emerald
}

DIMS       = ["affordability_score","digital_score","urban_score",
              "innovation_score","talent_score","growth_score"]
DIM_LABELS = ["Affordability","Digital","Urban","Innovation","Talent","Growth"]
DIM_ICONS  = ["💰","📡","🏙️","💡","👩‍💻","📈"]

# Truly distinct colors for comparison overlay (not pastels)
COMPARE_COLORS = ["#DB2777","#6D28D9","#0891B2","#D97706","#059669","#DC2626"]

# ─── CSS — Dark Mode ──────────────────────────────────────────────────────────
st.markdown(f"""
<style>
  /* ── Global dark background ── */
  .stApp, .stApp > div {{ background-color: {PAGE_BG} !important; }}
  .block-container {{ padding-top: 1.5rem; padding-bottom: 2rem; }}

  /* ── Body text — high contrast on dark bg ── */
  body, .stApp {{ color: {TEXT_MAIN} !important; }}
  h1 {{ font-size: 1.9rem !important; font-weight: 700 !important;
        color: {TEXT_MAIN} !important; letter-spacing: -0.02em;
        margin-bottom: 0.2rem !important; }}
  h2 {{ font-size: 1.25rem !important; font-weight: 600 !important;
        color: {TEXT_MAIN} !important; margin-top: 1.4rem !important; }}
  h3 {{ font-size: 1.05rem !important; font-weight: 600 !important;
        color: {PRIMARY} !important; }}
  p, li, span, label {{ color: {TEXT_MAIN} !important; line-height: 1.65; }}
  .stCaption, [data-testid="stCaption"] {{
      color: {TEXT_MUTED} !important; font-size: 0.8rem; }}
  a {{ color: {PRIMARY} !important; }}

  /* ── Metric cards — dark ── */
  [data-testid="stMetric"] {{
      background: {CARD_BG} !important;
      border: 1px solid {BORDER_COL};
      border-radius: 12px; padding: 14px 18px;
      box-shadow: 0 2px 12px rgba(0,0,0,0.4);
  }}
  [data-testid="stMetricLabel"] {{
      font-size: 0.75rem !important; font-weight: 500 !important;
      color: {TEXT_MUTED} !important;
      text-transform: uppercase; letter-spacing: 0.05em; }}
  [data-testid="stMetricValue"] {{
      font-size: 1.6rem !important; font-weight: 700 !important;
      color: {TEXT_MAIN} !important; }}

  /* ── Sidebar — dark ── */
  [data-testid="stSidebar"] {{
      background-color: {SIDEBAR_BG} !important;
      border-right: 1px solid {BORDER_COL};
  }}
  [data-testid="stSidebar"] * {{ color: #D1D5DB !important; }}
  [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2,
  [data-testid="stSidebar"] h3, [data-testid="stSidebar"] strong {{
      color: #F1EEFF !important; }}
  [data-testid="stSidebar"] label {{
      color: {TEXT_MUTED} !important; font-size: 0.75rem !important;
      text-transform: uppercase; letter-spacing: 0.06em; }}
  [data-testid="stSidebar"] .stRadio label {{
      text-transform: none !important; font-size: 0.9rem !important;
      color: #D1D5DB !important; letter-spacing: 0; }}
  [data-testid="stSidebar"] hr {{ border-color: {BORDER_COL}; }}

  /* ── Multiselect & selectbox inputs — dark ── */
  [data-baseweb="input"], [data-baseweb="select"],
  [data-baseweb="popover"], [data-testid="stMultiSelect"] > div,
  [data-testid="stSelectbox"] > div > div {{
      background-color: #1E1840 !important;
      border-color: {BORDER_COL} !important;
  }}
  /* ── Multiselect TAGS — girly pink/rose ── */
  [data-baseweb="tag"] {{
      background-color: #831843 !important;
      border: 1px solid #F472B6 !important;
      border-radius: 20px !important;
  }}
  [data-baseweb="tag"] span {{
      color: #FCE7F3 !important;
      font-weight: 600 !important;
      font-size: 12px !important;
  }}
  [data-baseweb="tag"] [role="presentation"] svg,
  [data-baseweb="tag"] button svg {{
      fill: #F9A8D4 !important;
  }}
  /* Dropdown options */
  [data-baseweb="menu"] {{
      background-color: #1A1438 !important;
      border: 1px solid {BORDER_COL} !important;
  }}
  [data-baseweb="menu"] li {{ color: {TEXT_MAIN} !important; }}
  [data-baseweb="menu"] li:hover {{ background-color: #2D2460 !important; }}
  /* Selectbox text */
  [data-testid="stSelectbox"] span, [data-testid="stMultiSelect"] span {{
      color: {TEXT_MAIN} !important;
  }}

  /* ── Tabs — dark ── */
  .stTabs [data-baseweb="tab-list"] {{
      background: #1A1438; border-radius: 10px; padding: 3px; gap: 2px;
  }}
  .stTabs [data-baseweb="tab"] {{
      border-radius: 8px; font-weight: 500;
      color: {TEXT_MUTED} !important;
      font-size: 0.88rem; padding: 6px 16px;
  }}
  .stTabs [aria-selected="true"] {{
      background: #2D2460 !important;
      color: {PRIMARY} !important;
      box-shadow: 0 1px 6px rgba(0,0,0,0.4);
      font-weight: 600;
  }}

  /* ── Cards ── */
  .metric-card {{
      background: {CARD_BG}; border: 1px solid {BORDER_COL};
      border-radius: 12px; padding: 14px 18px;
  }}
  .insight-card {{
      border-radius: 10px; padding: 10px 14px; margin: 5px 0;
      border-left: 4px solid;
  }}
  .cluster-badge {{
      display: inline-block; border-radius: 20px;
      padding: 3px 12px; font-size: 12px; font-weight: 600;
  }}

  /* ── Slider — dark ── */
  [data-testid="stSlider"] [data-baseweb="slider"] [role="slider"] {{
      background: #BE185D !important;
  }}
  [data-testid="stSlider"] [data-testid="stTickBarMin"],
  [data-testid="stSlider"] [data-testid="stTickBarMax"] {{
      color: {TEXT_MUTED} !important;
  }}

  /* ── Dataframe — dark ── */
  [data-testid="stDataFrame"] {{ border-radius: 10px; overflow: hidden; }}
  [data-testid="stDataFrame"] * {{ color: {TEXT_MAIN} !important; }}

  /* ── Expander — dark ── */
  [data-testid="stExpander"] {{
      background: {CARD_BG} !important;
      border: 1px solid {BORDER_COL} !important;
      border-radius: 10px !important;
  }}
  [data-testid="stExpander"] summary {{
      font-size: 0.82rem !important; font-weight: 500 !important;
      color: {TEXT_MUTED} !important;
      text-transform: uppercase; letter-spacing: 0.05em;
  }}
  [data-testid="stExpander"] summary:hover {{
      color: {PRIMARY} !important;
  }}

  /* ── Selectbox arrow ── */
  [data-testid="stSelectbox"] svg {{ fill: {TEXT_MUTED} !important; }}

  /* ── Info / warning boxes ── */
  [data-testid="stInfo"] {{ background: #1E1840 !important;
      border-color: {PRIMARY} !important; color: {TEXT_MAIN} !important; }}

  /* ── Page divider ── */
  .page-divider {{ height: 1px; background: {BORDER_COL}; margin: 1.5rem 0; }}

  /* ── Dimension picker — horizontal radio as pill buttons ── */
  [data-testid="stRadio"] [data-baseweb="radio"] {{
      background: {CARD_BG};
      border: 1px solid {BORDER_COL};
      border-radius: 30px;
      padding: 8px 18px;
      margin-right: 8px;
      cursor: pointer;
      transition: all 0.15s ease;
  }}
  [data-testid="stRadio"] [data-baseweb="radio"]:hover {{
      border-color: {PRIMARY};
      background: {PRIMARY_SOFT};
  }}
  [data-testid="stRadio"] [aria-checked="true"] [data-baseweb="radio"] {{
      background: #3B2D6B !important;
      border-color: {PRIMARY} !important;
  }}
  /* Hide the actual radio dot — we only want the label */
  [data-testid="stRadio"] [data-baseweb="radio"] div:first-child {{
      display: none !important;
  }}
  [data-testid="stRadio"] label {{
      font-size: 0.88rem !important;
      font-weight: 500 !important;
      color: {TEXT_MAIN} !important;
      text-transform: none !important;
      letter-spacing: 0 !important;
      cursor: pointer;
  }}

  /* ── Scrollbar — subtle dark ── */
  ::-webkit-scrollbar {{ width: 6px; height: 6px; }}
  ::-webkit-scrollbar-track {{ background: {PAGE_BG}; }}
  ::-webkit-scrollbar-thumb {{ background: #3B2D6B; border-radius: 3px; }}
  ::-webkit-scrollbar-thumb:hover {{ background: {PRIMARY}; }}
</style>
""", unsafe_allow_html=True)


# ─── Helpers ──────────────────────────────────────────────────────────────────
def fmt(val, dp=2):
    """Format a number to dp decimal places."""
    try:
        return f"{float(val):.{dp}f}"
    except Exception:
        return str(val)


def hex_to_rgb(h):
    h = h.lstrip("#")
    return [int(h[i:i+2], 16) for i in (0, 2, 4)]


def empty_state(msg="No cities match your current filters."):
    st.markdown(
        f'<div style="text-align:center;padding:60px 20px;color:{TEXT_MUTED}">'
        f'<div style="font-size:2.5rem">🔍</div>'
        f'<div style="font-size:1rem;margin-top:12px">{msg}</div>'
        f'<div style="font-size:0.85rem;margin-top:6px">Try adjusting the filters in the sidebar.</div>'
        f'</div>',
        unsafe_allow_html=True,
    )


def chart_defaults():
    return dict(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, sans-serif", color=TEXT_MAIN),
    )

def dark_axes():
    """Shared axis style for dark mode — high-contrast tick labels, subtle grid."""
    ax = dict(
        gridcolor=GRID_COL,
        linecolor=BORDER_COL,
        tickfont=dict(color=TEXT_MUTED, size=11),
        title_font=dict(color=TEXT_MAIN, size=12),
        zerolinecolor=BORDER_COL,
    )
    return ax


CHART_H = 460   # standard chart height
CHART_H_SM = 280  # small chart height


# ─── Data ─────────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv(DATA_DIR / "cities_clustered.csv")
    # Pre-round all score columns so they never show 6.200000
    score_cols = [c for c in df.columns if "_score" in c or c == "opportunity_index"]
    df[score_cols] = df[score_cols].round(2)
    return df

df_all = load_data()
all_clusters  = sorted(df_all["cluster"].unique())
cluster_names = df_all.groupby("cluster")["cluster_name"].first().to_dict()
color_map     = {cluster_names[c]: CLUSTER_COLORS[c] for c in all_clusters}


# ═══════════════════════════════════════════════════════════════════════════════
# SIDEBAR  —  Navigation FIRST, then collapsible filters
# ═══════════════════════════════════════════════════════════════════════════════
with st.sidebar:
    # Brand
    st.markdown(
        f'<div style="padding:8px 0 18px">'
        f'<div style="font-size:1.3rem;font-weight:700;color:#F3F4F6">🌍 CityMetric</div>'
        f'<div style="font-size:0.78rem;color:#9CA3AF;margin-top:2px">'
        f'Measure Your City, Measure Your Future</div>'
        f'</div>',
        unsafe_allow_html=True,
    )

    # ── Navigation — always visible at top ───────────────────────────────────
    page = st.radio(
        "Navigate",
        ["🏠  Overview", "🗺️  World Map", "📊  Cluster Analysis",
         "🔍  Dimension Deep-Dive", "🔄  City Comparison",
         "🚀  Insights", "📖  About"],
        label_visibility="collapsed",
    )
    page = page.strip()   # remove extra spaces used for icon padding

    st.markdown('<hr style="border-color:rgba(255,255,255,0.08);margin:14px 0">', unsafe_allow_html=True)

    # ── Filters — collapsible, below nav ─────────────────────────────────────
    with st.expander("🔧  Filters", expanded=True):
        sel_clusters = st.multiselect(
            "Cluster",
            options=all_clusters,
            default=all_clusters,
            format_func=lambda c: f"{cluster_names[c]}",
        )
        all_regions = sorted(df_all["region"].unique())
        sel_regions = st.multiselect(
            "Region",
            options=all_regions,
            default=all_regions,
        )
        opp_range = st.slider(
            "Min opportunity score",
            0.0, 10.0, 0.0, 0.1,
            format="%.1f",
        )
        highlight = st.selectbox(
            "Map color",
            ["opportunity_index"] + DIMS,
            format_func=lambda x: x.replace("_score","").replace("_"," ").title(),
        )

    st.markdown('<hr style="border-color:rgba(255,255,255,0.08);margin:14px 0">', unsafe_allow_html=True)
    st.markdown(
        f'<div style="font-size:0.72rem;color:#4B5563;line-height:1.6">'
        f'55 cities · 6 dimensions<br>'
        f'Sources: Numbeo · World Bank<br>'
        f'Stack Overflow · CWUR · NOAA</div>',
        unsafe_allow_html=True,
    )

# ─── Apply filters ────────────────────────────────────────────────────────────
df = df_all[
    df_all["cluster"].isin(sel_clusters if sel_clusters else all_clusters) &
    df_all["region"].isin(sel_regions if sel_regions else all_regions) &
    (df_all["opportunity_index"] >= opp_range)
].copy()


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: OVERVIEW
# ═══════════════════════════════════════════════════════════════════════════════
if "Overview" in page:
    st.title("Global City Opportunity & Innovation Index")
    st.caption(
        "Data-driven analysis of 55 global cities across 6 key dimensions — "
        "find where to build, invest, or move."
    )
    st.markdown('<div class="page-divider"></div>', unsafe_allow_html=True)

    if len(df) == 0:
        empty_state()
    else:
        # ── KPI row ──────────────────────────────────────────────────────────
        k1, k2, k3, k4, k5 = st.columns(5)
        top_city = df_all.loc[df_all["opportunity_index"].idxmax(), "city"]
        k1.metric("Cities Shown",    f"{len(df)} / {len(df_all)}")
        k2.metric("Clusters",        f"{df['cluster'].nunique()}")
        k3.metric("Avg Opportunity", f"{df['opportunity_index'].mean():.2f} / 10")
        k4.metric("Top City",        top_city)
        k5.metric("Data Sources",    "8+")

        st.markdown('<div class="page-divider"></div>', unsafe_allow_html=True)

        col_left, col_right = st.columns([3, 2], gap="large")

        with col_left:
            st.subheader("Top 20 Cities by Opportunity Index")
            top20 = df.nlargest(20, "opportunity_index").sort_values("opportunity_index")
            fig = px.bar(
                top20, x="opportunity_index", y="city",
                color="cluster_name", color_discrete_map=color_map,
                orientation="h", text="opportunity_index",
                labels={"opportunity_index":"Opportunity Index","city":"","cluster_name":"Cluster"},
                template="plotly_dark",
            )
            fig.update_traces(
                texttemplate="%{x:.2f}", textposition="outside",
                marker_line_width=0,
            )
            fig.update_layout(
                **chart_defaults(),
                height=CHART_H,
                xaxis=dict(range=[0, top20["opportunity_index"].max() + 0.8],
                           showgrid=True, gridcolor=GRID_COL),
                yaxis=dict(showgrid=False),
                legend=dict(orientation="h", y=-0.1, x=0,
                            font=dict(size=11), title=""),
                margin=dict(l=0, r=40, t=10, b=40),
            )
            st.plotly_chart(fig, use_container_width=True)

        with col_right:
            st.subheader("Cluster Distribution")
            counts = df.groupby("cluster_name").size().reset_index(name="count")
            fig2 = px.pie(
                counts, values="count", names="cluster_name",
                color="cluster_name", color_discrete_map=color_map,
                hole=0.52, template="plotly_dark",
            )
            fig2.update_traces(
                textposition="outside", textinfo="label+percent",
                marker=dict(line=dict(color=PAGE_BG, width=3)),
                textfont_size=11,
            )
            fig2.update_layout(
                **chart_defaults(),
                height=240, showlegend=False,
                margin=dict(t=10, b=10, l=20, r=20),
            )
            st.plotly_chart(fig2, use_container_width=True)

            st.subheader("Regional Averages")
            reg = (df.groupby("region")["opportunity_index"]
                   .mean().sort_values(ascending=True).reset_index())
            fig3 = px.bar(
                reg, x="opportunity_index", y="region", orientation="h",
                color="opportunity_index",
                color_continuous_scale=[[0,"#3B2D6B"],[0.5,"#7C3AED"],[1,"#C4B5FD"]],
                text="opportunity_index",
                labels={"opportunity_index":"Avg Score","region":""},
                template="plotly_dark",
            )
            fig3.update_traces(
                texttemplate="%{x:.2f}", textposition="outside",
                marker_line_width=0,
            )
            fig3.update_layout(
                **chart_defaults(),
                height=220, coloraxis_showscale=False,
                xaxis=dict(range=[0, reg["opportunity_index"].max() + 0.5],
                           showgrid=False),
                yaxis=dict(showgrid=False),
                margin=dict(l=0, r=40, t=0, b=0),
            )
            st.plotly_chart(fig3, use_container_width=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: WORLD MAP
# ═══════════════════════════════════════════════════════════════════════════════
elif "World Map" in page:
    st.title("City Intelligence Map")

    # Cluster legend pills
    legend_cols = st.columns(len(all_clusters))
    for i, c in enumerate(all_clusters):
        legend_cols[i].markdown(
            f'<span class="cluster-badge" style="background:{CLUSTER_COLORS[c]};'
            f'border:1.5px solid {CLUSTER_DARK[c]};color:{TEXT_MAIN}">'
            f'{cluster_names[c]}</span>',
            unsafe_allow_html=True,
        )
    st.markdown("")

    if len(df) == 0:
        empty_state()
    else:
        tab1, tab2, tab3 = st.tabs(["🗺️  Interactive Map", "🌐  3D Globe", "🔥  Heatmap"])

        # ── TAB 1: Plotly Mapbox ─────────────────────────────────────────────
        with tab1:
            st.caption("Hover any city for scores · Zoom & pan · Click legend to filter")
            with st.spinner("Loading map…"):
                df["_hover"] = df.apply(lambda r: (
                    f"<b>{r['city']}, {r['country']}</b><br>"
                    f"<span style='color:#888'>{r['cluster_name']}</span><br><br>"
                    f"Opportunity  <b>{r['opportunity_index']:.2f}</b>/10<br>"
                    f"Affordability  {r['affordability_score']:.2f} &nbsp;·&nbsp; "
                    f"Digital  {r['digital_score']:.2f}<br>"
                    f"Urban  {r['urban_score']:.2f} &nbsp;·&nbsp; "
                    f"Innovation  {r['innovation_score']:.2f}<br>"
                    f"Talent  {r['talent_score']:.2f} &nbsp;·&nbsp; "
                    f"Growth  {r['growth_score']:.2f}"
                ), axis=1)
                fig_map = px.scatter_mapbox(
                    df, lat="latitude", lon="longitude",
                    color="cluster_name", color_discrete_map=color_map,
                    size="opportunity_index", size_max=24,
                    hover_name="city", custom_data=["_hover"],
                    zoom=1.4, center={"lat": 20, "lon": 10},
                    mapbox_style="open-street-map",
                    height=560,
                )
                fig_map.update_traces(
                    hovertemplate="%{customdata[0]}<extra></extra>",
                    marker=dict(opacity=0.88, sizemin=7),
                )
                fig_map.update_layout(
                    **chart_defaults(),
                    margin=dict(l=0, r=0, t=0, b=0),
                    legend=dict(
                        title="", bgcolor="rgba(255,255,255,0.92)",
                        bordercolor="#E5E7EB", borderwidth=1,
                        x=0.01, y=0.99, font=dict(size=12),
                    ),
                )
                st.plotly_chart(fig_map, use_container_width=True)

        # ── TAB 2: PyDeck 3D Globe ───────────────────────────────────────────
        with tab2:
            st.caption("Drag to rotate · Scroll to zoom · Hover city · Column height = Opportunity Index")
            with st.spinner("Building 3D globe…"):
                import pydeck as pdk
                df_deck = df.copy()
                df_deck["color"]     = df_deck["cluster"].map(lambda c: hex_to_rgb(CLUSTER_COLORS[c]))
                df_deck["color_dark"]= df_deck["cluster"].map(lambda c: hex_to_rgb(CLUSTER_DARK[c]))
                df_deck["elevation"] = df_deck["opportunity_index"] * 130000
                df_deck["radius"]    = (df_deck["opportunity_index"] * 55000 + 70000).astype(int)

                col_layer = pdk.Layer(
                    "ColumnLayer", data=df_deck,
                    get_position=["longitude","latitude"],
                    get_elevation="elevation", elevation_scale=1,
                    radius=75000, get_fill_color="color",
                    pickable=True, auto_highlight=True, extruded=True,
                )
                scatter_layer = pdk.Layer(
                    "ScatterplotLayer", data=df_deck,
                    get_position=["longitude","latitude"],
                    get_radius="radius",
                    get_fill_color="color",
                    get_line_color="color_dark",
                    line_width_min_pixels=1,
                    pickable=True, opacity=0.45,
                )
                view = pdk.ViewState(
                    latitude=20, longitude=10,
                    zoom=1.2, pitch=48, bearing=0,
                )
                tooltip = {
                    "html": (
                        "<b style='font-size:14px'>{city}, {country}</b><br/>"
                        "<span style='color:#A78BFA'>{cluster_name}</span><br/><br/>"
                        "Opportunity: <b>{opportunity_index}</b>/10<br/>"
                        "Afford: {affordability_score} &nbsp;·&nbsp; Digital: {digital_score}<br/>"
                        "Innovation: {innovation_score} &nbsp;·&nbsp; Talent: {talent_score}"
                    ),
                    "style": {
                        "background": "rgba(24,16,58,0.95)",
                        "color": "#F3F4F6",
                        "font-family": "Inter, sans-serif",
                        "font-size": "13px",
                        "padding": "12px 14px",
                        "border-radius": "10px",
                        "border": "1px solid rgba(167,139,250,0.3)",
                    },
                }
                deck = pdk.Deck(
                    layers=[scatter_layer, col_layer],
                    initial_view_state=view,
                    tooltip=tooltip,
                    map_style="https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json",
                )
                st.pydeck_chart(deck, use_container_width=True, height=560)

        # ── TAB 3: Heatmap ───────────────────────────────────────────────────
        with tab3:
            dim_choice = st.selectbox(
                "Show heatmap for",
                ["opportunity_index"] + DIMS,
                format_func=lambda x: x.replace("_score","").replace("_"," ").title(),
            )
            st.caption(f"Intensity = {dim_choice.replace('_score','').replace('_',' ').title()} score")
            with st.spinner("Loading heatmap…"):
                fig_heat = px.density_mapbox(
                    df, lat="latitude", lon="longitude",
                    z=dim_choice, radius=55, zoom=1.3,
                    center={"lat": 20, "lon": 10},
                    mapbox_style="carto-darkmatter",
                    color_continuous_scale=["#0F0A2A","#4C1D95","#7C3AED","#F9A8D4","#FEF3C7"],
                    hover_name="city",
                    hover_data={"latitude":False,"longitude":False,dim_choice:":.2f"},
                    height=540,
                )
                fig_heat.update_layout(
                    **chart_defaults(),
                    margin=dict(l=0, r=0, t=0, b=0),
                    coloraxis_colorbar=dict(
                        title=dim_choice.replace("_score","").title(),
                        tickformat=".1f", len=0.6,
                    ),
                )
                st.plotly_chart(fig_heat, use_container_width=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: CLUSTER ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════
elif "Cluster Analysis" in page:
    st.title("Cluster Analysis")
    st.caption("Explore how cities group together based on their opportunity profiles.")
    st.markdown('<div class="page-divider"></div>', unsafe_allow_html=True)

    sel_c  = st.selectbox(
        "Select a cluster",
        options=all_clusters,
        format_func=lambda c: f"C{c} — {cluster_names[c]}",
    )
    cdata = df_all[df_all["cluster"] == sel_c]
    color = CLUSTER_COLORS[sel_c]
    rv, gv, bv = hex_to_rgb(color)

    # KPIs
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Cities in cluster",   len(cdata))
    k2.metric("Avg Opportunity",     f"{cdata['opportunity_index'].mean():.2f}")
    k3.metric("Avg Affordability",   f"{cdata['affordability_score'].mean():.2f}")
    k4.metric("Avg Growth",          f"{cdata['growth_score'].mean():.2f}")

    st.markdown('<div class="page-divider"></div>', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        # Radar with bigger tick labels
        means  = cdata[DIMS].mean().tolist() + [cdata[DIMS[0]].mean()]
        cats   = DIM_LABELS + [DIM_LABELS[0]]
        fig_r  = go.Figure(go.Scatterpolar(
            r=means, theta=cats, fill="toself",
            line_color=CLUSTER_DARK[sel_c], line_width=2.5,
            fillcolor=f"rgba({rv},{gv},{bv},0.35)",
            name=cluster_names[sel_c],
        ))
        fig_r.update_layout(
            **chart_defaults(),
            polar=dict(
                radialaxis=dict(range=[0,10], tickfont=dict(size=11),
                                gridcolor=GRID_COL, linecolor=BORDER_COL),
                angularaxis=dict(tickfont=dict(size=13, color=TEXT_MAIN)),
                bgcolor="rgba(0,0,0,0)",
            ),
            title=dict(text=f"{cluster_names[sel_c]} — Dimension Profile",
                       font=dict(size=13, color=TEXT_MUTED), x=0.5),
            height=CHART_H, margin=dict(t=40, b=20),
            showlegend=False,
        )
        st.plotly_chart(fig_r, use_container_width=True)

    with col2:
        st.subheader(f"Cities — {cluster_names[sel_c]}")
        show_cols = ["city","country","opportunity_index"] + DIMS
        rename_map = {d: d.replace("_score","").title() for d in DIMS}
        rename_map["opportunity_index"] = "Opportunity"
        display_df = (
            cdata[show_cols]
            .sort_values("opportunity_index", ascending=False)
            .reset_index(drop=True)
            .rename(columns=rename_map)
        )
        # Format all number columns to 2dp
        num_cols = display_df.select_dtypes("number").columns
        display_df[num_cols] = display_df[num_cols].round(2)
        st.dataframe(
            display_df.style.background_gradient(
                subset=["Opportunity"], cmap="Purples"
            ).format({c: "{:.2f}" for c in num_cols}),
            use_container_width=True, height=CHART_H - 20,
        )

    st.markdown('<div class="page-divider"></div>', unsafe_allow_html=True)
    st.subheader("All 5 Clusters — Side-by-Side")
    fig_all = make_subplots(
        rows=1, cols=5, specs=[[{"type":"polar"}]*5],
        subplot_titles=[cluster_names[c] for c in all_clusters],
    )
    for i, c in enumerate(all_clusters, start=1):
        sub    = df_all[df_all["cluster"]==c]
        vals   = sub[DIMS].mean().tolist() + [sub[DIMS[0]].mean()]
        cats2  = DIM_LABELS + [DIM_LABELS[0]]
        col_h  = CLUSTER_COLORS[c]
        r2,g2,b2 = hex_to_rgb(col_h)
        fig_all.add_trace(
            go.Scatterpolar(
                r=vals, theta=cats2, fill="toself",
                line_color=CLUSTER_DARK[c], line_width=2,
                fillcolor=f"rgba({r2},{g2},{b2},0.4)",
                name=cluster_names[c],
            ), row=1, col=i,
        )
        pk = "polar" if i == 1 else f"polar{i}"
        fig_all.update_layout(**{
            pk: dict(
                radialaxis=dict(range=[0,10], tickfont_size=8,
                                gridcolor=GRID_COL, linecolor=BORDER_COL,
                                tickfont=dict(color=TEXT_MUTED)),
                angularaxis=dict(tickfont=dict(size=9, color=TEXT_MUTED)),
                bgcolor="rgba(0,0,0,0)",
            )
        })
    fig_all.update_layout(
        **chart_defaults(),
        height=360, showlegend=False,
        margin=dict(t=30, b=10),
    )
    st.plotly_chart(fig_all, use_container_width=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: DIMENSION DEEP-DIVE
# ═══════════════════════════════════════════════════════════════════════════════
elif "Dimension" in page:
    st.title("Dimension Deep-Dive")
    st.caption("Explore any single dimension across all cities and regions.")
    st.markdown('<div class="page-divider"></div>', unsafe_allow_html=True)

    # Single clickable radio — icon + label, horizontal layout, no dropdown
    sel_dim = st.radio(
        "Dimension",
        options=DIMS,
        format_func=lambda x: f"{DIM_ICONS[DIMS.index(x)]}  {x.replace('_score','').title()}",
        horizontal=True,
        label_visibility="collapsed",
    )
    label = sel_dim.replace("_score","").title()

    if len(df) == 0:
        empty_state()
    else:
        st.markdown('<div class="page-divider"></div>', unsafe_allow_html=True)
        col1, col2 = st.columns([3, 2], gap="large")

        with col1:
            st.subheader(f"Top 20 Cities — {label}")
            top_dim = df.nlargest(20, sel_dim).sort_values(sel_dim)
            fig = px.bar(
                top_dim, x=sel_dim, y="city",
                color="cluster_name", color_discrete_map=color_map,
                orientation="h", text=sel_dim,
                labels={sel_dim: f"{label} Score","city":""},
                template="plotly_dark",
            )
            fig.update_traces(
                texttemplate="%{x:.2f}", textposition="outside",
                marker_line_width=0,
            )
            fig.update_layout(
                **chart_defaults(),
                height=CHART_H,
                xaxis=dict(range=[0, top_dim[sel_dim].max() + 0.8],
                           showgrid=True, gridcolor=GRID_COL),
                yaxis=dict(showgrid=False),
                legend=dict(title="", orientation="h", y=-0.1, font=dict(size=11)),
                margin=dict(l=0, r=40, t=10, b=40),
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("By Region")
            reg_dim = df.groupby("region")[sel_dim].mean().sort_values(ascending=True).reset_index()
            fig2 = px.bar(
                reg_dim, x=sel_dim, y="region", orientation="h",
                color=sel_dim,
                color_continuous_scale=[[0,"#3B2D6B"],[1,"#C4B5FD"]],
                text=sel_dim,
                labels={sel_dim: f"{label} Score","region":""},
                template="plotly_dark",
            )
            fig2.update_traces(
                texttemplate="%{x:.2f}", textposition="outside",
                marker_line_width=0,
            )
            fig2.update_layout(
                **chart_defaults(),
                height=CHART_H_SM + 20,
                coloraxis_showscale=False,
                xaxis=dict(range=[0, reg_dim[sel_dim].max()+0.5], showgrid=False),
                yaxis=dict(showgrid=False),
                margin=dict(l=0, r=40, t=0, b=0),
            )
            st.plotly_chart(fig2, use_container_width=True)

            st.subheader("Distribution by Cluster")
            fig3 = px.box(
                df, x="cluster_name", y=sel_dim,
                color="cluster_name", color_discrete_map=color_map,
                points="all", hover_data=["city"],
                labels={sel_dim: f"{label} Score","cluster_name":""},
                template="plotly_dark",
            )
            fig3.update_layout(
                **chart_defaults(),
                height=CHART_H_SM,
                showlegend=False,
                xaxis=dict(tickfont=dict(size=10)),
                margin=dict(t=0, b=0),
            )
            st.plotly_chart(fig3, use_container_width=True)

        st.markdown('<div class="page-divider"></div>', unsafe_allow_html=True)
        st.subheader("Correlation Between Dimensions")
        corr = df[DIMS].corr().round(2)
        fig4 = go.Figure(go.Heatmap(
            z=corr.values, x=DIM_LABELS, y=DIM_LABELS,
            colorscale=[[0,"#0891B2"],[0.5,"#1A1438"],[1,"#7C3AED"]],
            zmin=-1, zmax=1,
            text=corr.values, texttemplate="%{text:.2f}",
            textfont=dict(size=12),
            hovertemplate="%{y} × %{x} = %{z:.2f}<extra></extra>",
        ))
        fig4.update_layout(
            **chart_defaults(),
            height=380, width=540,
            margin=dict(l=0, r=0, t=0, b=0),
            xaxis=dict(tickfont=dict(size=12)),
            yaxis=dict(tickfont=dict(size=12)),
        )
        st.plotly_chart(fig4)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: CITY COMPARISON
# ═══════════════════════════════════════════════════════════════════════════════
elif "Comparison" in page:
    st.title("City Comparison")
    st.caption("Select 2–6 cities to compare across all dimensions side by side.")
    st.markdown('<div class="page-divider"></div>', unsafe_allow_html=True)

    default_cities = ["Bangkok", "Lisbon", "Singapore", "Berlin", "Seoul"]
    cities_to_compare = st.multiselect(
        "Choose cities",
        options=sorted(df_all["city"].unique()),
        default=[c for c in default_cities if c in df_all["city"].values],
        max_selections=6,
    )

    if len(cities_to_compare) < 2:
        st.markdown(
            f'<div style="text-align:center;padding:50px;color:{TEXT_MUTED}">'
            f'<div style="font-size:2rem">🏙️</div>'
            f'<div style="margin-top:10px">Select at least <b>2 cities</b> to compare.</div>'
            f'</div>', unsafe_allow_html=True,
        )
    else:
        cmp = df_all[df_all["city"].isin(cities_to_compare)].copy()

        # ── Radar overlay with distinct colors ───────────────────────────────
        st.subheader("Dimension Profile Overlay")
        fig_radar = go.Figure()
        for i, (_, row) in enumerate(cmp.iterrows()):
            vals = [row[d] for d in DIMS] + [row[DIMS[0]]]
            cats = DIM_LABELS + [DIM_LABELS[0]]
            col_i = COMPARE_COLORS[i % len(COMPARE_COLORS)]
            rv, gv, bv = hex_to_rgb(col_i)
            fig_radar.add_trace(go.Scatterpolar(
                r=vals, theta=cats, fill="toself",
                name=row["city"],
                line=dict(color=col_i, width=2.5),
                fillcolor=f"rgba({rv},{gv},{bv},0.12)",
            ))
        fig_radar.update_layout(
            **chart_defaults(),
            polar=dict(
                radialaxis=dict(range=[0,10], tickfont=dict(size=11),
                                gridcolor=GRID_COL, linecolor=BORDER_COL),
                angularaxis=dict(tickfont=dict(size=13, color=TEXT_MAIN)),
                bgcolor="rgba(0,0,0,0)",
            ),
            height=CHART_H,
            legend=dict(orientation="h", y=-0.08, font=dict(size=12)),
            margin=dict(t=20, b=60),
        )
        st.plotly_chart(fig_radar, use_container_width=True)

        st.markdown('<div class="page-divider"></div>', unsafe_allow_html=True)
        col1, col2 = st.columns([1,1], gap="large")

        with col1:
            st.subheader("Score Breakdown")
            melt = cmp.melt(id_vars=["city"], value_vars=DIMS,
                            var_name="dimension", value_name="score")
            melt["dimension"] = melt["dimension"].str.replace("_score","").str.title()
            city_colors = {row["city"]: COMPARE_COLORS[i]
                           for i, (_, row) in enumerate(cmp.iterrows())}
            fig_bar = px.bar(
                melt, x="dimension", y="score", color="city",
                barmode="group", color_discrete_map=city_colors,
                labels={"dimension":"","score":"Score (0–10)","city":""},
                template="plotly_dark",
            )
            fig_bar.update_layout(
                **chart_defaults(),
                height=CHART_H_SM + 40,
                legend=dict(orientation="h", y=-0.2, font=dict(size=11)),
                xaxis=dict(showgrid=False),
                yaxis=dict(range=[0,11], gridcolor=GRID_COL),
                margin=dict(t=10, b=60),
            )
            st.plotly_chart(fig_bar, use_container_width=True)

        with col2:
            st.subheader("Summary Table")
            tbl_cols = ["city","country","cluster_name","opportunity_index"] + DIMS
            rename = {d: d.replace("_score","").title() for d in DIMS}
            rename["opportunity_index"] = "Opportunity"
            rename["cluster_name"] = "Cluster"
            display_cmp = cmp[tbl_cols].set_index("city").rename(columns=rename)
            num_cols_cmp = display_cmp.select_dtypes("number").columns
            display_cmp[num_cols_cmp] = display_cmp[num_cols_cmp].round(2)
            st.dataframe(
                display_cmp.style
                    .background_gradient(subset=["Opportunity"], cmap="Purples")
                    .format({c: "{:.2f}" for c in num_cols_cmp}),
                use_container_width=True,
                height=CHART_H_SM + 40,
            )


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: INSIGHTS
# ═══════════════════════════════════════════════════════════════════════════════
elif "Insights" in page:
    st.title("Key Insights")
    st.caption("What the data reveals about global city opportunities.")
    st.markdown('<div class="page-divider"></div>', unsafe_allow_html=True)

    # ── 3 top cards — always visible, no expander ────────────────────────────
    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        st.subheader("💰 Best Value")
        st.caption("High opportunity · High affordability")
        best = df_all.nlargest(20,"opportunity_index").nlargest(5,"affordability_score")
        for _, r in best.iterrows():
            c = CLUSTER_COLORS[r["cluster"]]
            d = CLUSTER_DARK[r["cluster"]]
            st.markdown(
                f'<div class="insight-card" style="background:{c}22;border-color:{d}">'
                f'<b style="color:{TEXT_MAIN}">{r["city"]}</b>'
                f'<span style="color:{TEXT_MUTED};font-size:12px"> · {r["country"]}</span><br>'
                f'<span style="font-size:12px;color:{TEXT_MUTED}">'
                f'Score: <b style="color:{TEXT_MAIN}">{r["opportunity_index"]:.2f}</b> &nbsp;·&nbsp; '
                f'Afford: <b style="color:{TEXT_MAIN}">{r["affordability_score"]:.2f}</b></span>'
                f'</div>', unsafe_allow_html=True,
            )

    with col2:
        st.subheader("📈 Rising Stars")
        st.caption("Highest growth potential")
        stars = df_all.nlargest(5,"growth_score")
        for _, r in stars.iterrows():
            c = CLUSTER_COLORS[r["cluster"]]
            d = CLUSTER_DARK[r["cluster"]]
            st.markdown(
                f'<div class="insight-card" style="background:{c}22;border-color:{d}">'
                f'<b style="color:{TEXT_MAIN}">{r["city"]}</b>'
                f'<span style="color:{TEXT_MUTED};font-size:12px"> · {r["country"]}</span><br>'
                f'<span style="font-size:12px;color:{TEXT_MUTED}">'
                f'Growth: <b style="color:{TEXT_MAIN}">{r["growth_score"]:.2f}</b> &nbsp;·&nbsp; '
                f'Opp: <b style="color:{TEXT_MAIN}">{r["opportunity_index"]:.2f}</b></span>'
                f'</div>', unsafe_allow_html=True,
            )

    with col3:
        st.subheader("💡 Innovation Leaders")
        st.caption("Highest innovation scores")
        innov = df_all.nlargest(5,"innovation_score")
        for _, r in innov.iterrows():
            c = CLUSTER_COLORS[r["cluster"]]
            d = CLUSTER_DARK[r["cluster"]]
            st.markdown(
                f'<div class="insight-card" style="background:{c}22;border-color:{d}">'
                f'<b style="color:{TEXT_MAIN}">{r["city"]}</b>'
                f'<span style="color:{TEXT_MUTED};font-size:12px"> · {r["country"]}</span><br>'
                f'<span style="font-size:12px;color:{TEXT_MUTED}">'
                f'Innov: <b style="color:{TEXT_MAIN}">{r["innovation_score"]:.2f}</b> &nbsp;·&nbsp; '
                f'Talent: <b style="color:{TEXT_MAIN}">{r["talent_score"]:.2f}</b></span>'
                f'</div>', unsafe_allow_html=True,
            )

    st.markdown('<div class="page-divider"></div>', unsafe_allow_html=True)

    # ── Key findings — all visible, no expander needed ───────────────────────
    st.subheader("Key Findings")
    findings = [
        ("#F9A8D4", "#DB2777", "🌟 Top opportunity cities",
         "Los Angeles, New York, and San Francisco lead overall — driven by exceptional talent concentration and digital infrastructure."),
        ("#6EE7B7", "#059669", "💚 Best value for money",
         "Melbourne, Sydney, and Tel Aviv offer top-10 opportunity scores with significantly better affordability than US hubs."),
        ("#67E8F9", "#0891B2", "📡 Digital divide is real",
         "Hong Kong and Singapore score near-perfect (9.0/10) on digital. African cities average below 2.5 — a 6+ point gap."),
        ("#A78BFA", "#6D28D9", "🚀 Asia's growth trajectory",
         "Singapore, Hong Kong, and Seoul show the strongest growth scores in Asia-Pacific, driven by high-tech export share."),
        ("#FCD34D", "#D97706", "🏙️ Europe's consistency",
         "European cities cluster tightly — balanced across all dimensions, but no city stands out as a runaway leader."),
        ("#F9A8D4", "#DB2777", "⚠️ Innovation concentration",
         "Innovation scores are heavily concentrated. 40% of cities score below 2.0 — top innovators are mostly in USA and select EU cities."),
    ]
    f_col1, f_col2 = st.columns(2, gap="medium")
    for i, (bg, border, title, desc) in enumerate(findings):
        target = f_col1 if i % 2 == 0 else f_col2
        target.markdown(
            f'<div class="insight-card" style="background:{bg}18;border-color:{border};margin-bottom:10px">'
            f'<b style="color:{TEXT_MAIN}">{title}</b><br>'
            f'<span style="font-size:13px;color:{TEXT_MUTED}">{desc}</span>'
            f'</div>', unsafe_allow_html=True,
        )

    st.markdown('<div class="page-divider"></div>', unsafe_allow_html=True)
    st.subheader("Digital vs Innovation")
    if len(df) > 0:
        fig_scatter = px.scatter(
            df_all, x="digital_score", y="innovation_score",
            color="cluster_name", color_discrete_map=color_map,
            size="talent_score", text="city",
            hover_data={"country":True,"opportunity_index":":.2f",
                        "growth_score":":.2f","cluster_name":False},
            labels={"digital_score":"Digital Score","innovation_score":"Innovation Score",
                    "cluster_name":"Cluster"},
            template="plotly_dark",
        )
        fig_scatter.update_traces(
            textposition="top center", textfont=dict(size=8, color=TEXT_MUTED),
        )
        fig_scatter.update_layout(
            **chart_defaults(),
            height=CHART_H,
            xaxis=dict(gridcolor=GRID_COL, title_font=dict(size=12)),
            yaxis=dict(gridcolor=GRID_COL, title_font=dict(size=12)),
            legend=dict(title="", font=dict(size=11)),
            margin=dict(t=10, b=10),
        )
        st.plotly_chart(fig_scatter, use_container_width=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: ABOUT
# ═══════════════════════════════════════════════════════════════════════════════
elif "About" in page:
    st.title("About CityMetric")
    st.markdown('<div class="page-divider"></div>', unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2], gap="large")
    with col1:
        st.subheader("What is CityMetric?")
        st.markdown(
            "CityMetric is a data-driven platform that analyses **55 global cities** "
            "across **6 key dimensions** to answer: *Where should you build, invest, or move?*\n\n"
            "It combines data from 8+ global sources, engineers composite scores using "
            "Min-Max normalization, clusters cities with **K-Means (K=5) via WEKA**, "
            "and presents everything through this interactive dashboard."
        )
        st.markdown('<div class="page-divider"></div>', unsafe_allow_html=True)

        st.subheader("Methodology")
        for icon, dim, desc in zip(DIM_ICONS, DIM_LABELS, [
            "Salary-to-rent ratio, food costs, utilities, transport",
            "Internet penetration %, broadband, mobile subscriptions",
            "Population density, climate comfort score, urban growth",
            "R&D spending, research publications, university quality",
            "Education enrollment, developer density, skill seniority",
            "GDP growth, population trend, high-tech export share",
        ]):
            st.markdown(
                f'<div style="display:flex;gap:12px;padding:8px 0;border-bottom:1px solid #F3F4F6">'
                f'<span style="font-size:1.3rem">{icon}</span>'
                f'<div><b style="color:{TEXT_MAIN}">{dim}</b><br>'
                f'<span style="font-size:12px;color:{TEXT_MUTED}">{desc}</span></div>'
                f'</div>', unsafe_allow_html=True,
            )

        st.markdown('<div class="page-divider"></div>', unsafe_allow_html=True)
        st.subheader("Tech Stack")
        tech = [("Python","Data pipeline & scripts"),
                ("WEKA","SimpleKMeans clustering (K=5)"),
                ("Folium + PyDeck","Geospatial visualizations"),
                ("Plotly","Interactive charts"),
                ("Streamlit","This dashboard"),
                ("World Bank API","Economic & social indicators")]
        for t, d in tech:
            st.markdown(
                f'`{t}` <span style="color:{TEXT_MUTED};font-size:13px">— {d}</span>',
                unsafe_allow_html=True,
            )

    with col2:
        st.subheader("Cluster Reference")
        for c in all_clusters:
            cities = sorted(df_all.loc[df_all["cluster"]==c, "city"].tolist())
            st.markdown(
                f'<div style="background:{CLUSTER_COLORS[c]}22;border:1.5px solid {CLUSTER_DARK[c]};'
                f'border-radius:10px;padding:12px 14px;margin:8px 0">'
                f'<b style="color:{TEXT_MAIN}">{cluster_names[c]}</b>'
                f'<span style="font-size:11px;color:{TEXT_MUTED}"> · {len(cities)} cities</span><br>'
                f'<span style="font-size:11px;color:{TEXT_MUTED}">{", ".join(cities)}</span>'
                f'</div>', unsafe_allow_html=True,
            )

        st.markdown('<div class="page-divider"></div>', unsafe_allow_html=True)
        st.subheader("Author")
        st.markdown(
            f'<div style="background:{CARD_BG};border:1px solid #E5E7EB;'
            f'border-radius:10px;padding:16px">'
            f'<b style="font-size:1.05rem;color:{TEXT_MAIN}">Alma Nurul Salma</b><br>'
            f'<span style="font-size:12px;color:{TEXT_MUTED}">'
            f'Informatics — UII & Nanjing Xiaozhuang University</span><br><br>'
            f'<span style="font-size:12px;color:{TEXT_MUTED}">'
            f'📧 almanurulsalma@gmail.com<br>'
            f'🔗 github.com/AlmaNurulSalma-dev</span>'
            f'</div>', unsafe_allow_html=True,
        )


# ─── Footer ───────────────────────────────────────────────────────────────────
st.markdown('<div class="page-divider"></div>', unsafe_allow_html=True)
st.markdown(
    f'<div style="text-align:center;color:{TEXT_MUTED};font-size:12px;padding-bottom:8px">'
    f'CityMetric · Measure Your City, Measure Your Future · '
    f'Data: Numbeo · World Bank · Stack Overflow · CWUR · NOAA'
    f'</div>',
    unsafe_allow_html=True,
)
