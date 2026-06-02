"""
CityMetric — Global City Opportunity & Innovation Index
Dashboard v3 — Modern Pastel Design
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
ASSETS   = ROOT / "assets"

# ─── Design System — Pastel Palette ──────────────────────────────────────────
# Blends Coastal Breeze + Lilac Field + Cotton Candy accents
PAGE_BG      = "#F5F3FA"   # Very light lavender-white (base)
CARD_BG      = "#FFFFFF"   # Pure white cards
SIDEBAR_BG   = "#1C1733"   # Deep dark (high contrast for nav)
BORDER_COL   = "#E4E2F4"   # Soft lilac border
PRIMARY      = "#7275B3"   # Deeper lilac — interactive elements
PRIMARY_LIGHT= "#D1D4F5"   # Soft Lilac (Lilac Field)
TEXT_MAIN    = "#1E1A35"   # Near-black with purple tint
TEXT_MUTED   = "#8B8AAD"   # Muted lavender-grey
TEXT_ON_DARK = "#EDE9FF"   # Text on dark sidebar
SHADOW       = "0 2px 16px rgba(114,117,179,0.10), 0 1px 4px rgba(0,0,0,0.04)"
SHADOW_HOVER = "0 8px 32px rgba(114,117,179,0.18), 0 2px 8px rgba(0,0,0,0.06)"
GRID_COL     = "#F0EEF9"   # Very light grid lines

# Cluster palette — one color per palette family
CLUSTER_COLORS = {
    0: "#F9C0D3",   # Soft Pink    — Balanced Cities
    1: "#B4B8E0",   # Deep Lilac   — Digital Leaders
    2: "#A7D8DE",   # Baby Blue    — Established Hubs
    3: "#A8C3A5",   # Mint Green   — Rising Stars
    4: "#FFB399",   # Peach        — Emerging Markets
}
CLUSTER_DARK = {
    0: "#C2547A",   # deep pink
    1: "#5254A3",   # deep indigo
    2: "#3A9DAA",   # deep teal
    3: "#4A8A47",   # deep green
    4: "#C26B42",   # deep coral
}

# Truly distinct for comparison overlay
COMPARE_COLORS = ["#C2547A","#5254A3","#3A9DAA","#C26B42","#4A8A47","#9B59B6"]

DIMS       = ["affordability_score","digital_score","urban_score",
              "innovation_score","talent_score","growth_score"]
DIM_LABELS = ["Affordability","Digital","Urban","Innovation","Talent","Growth"]
DIM_ICONS  = ["","","","","",""]   # no icons — text only


# ─── Google Fonts + CSS ───────────────────────────────────────────────────────
st.markdown(f"""
<style>
/* ── Google Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=Inter:wght@400;500;600&display=swap');

/* ── Reset & base ── */
*, *::before, *::after {{ box-sizing: border-box; }}
html, body, .stApp {{
    background-color: {PAGE_BG} !important;
    font-family: 'Plus Jakarta Sans', 'Inter', sans-serif !important;
    color: {TEXT_MAIN} !important;
    -webkit-font-smoothing: antialiased;
}}
.block-container {{ padding: 1.5rem 2rem 3rem 2rem !important; max-width: 1320px; }}

/* ── Typography hierarchy ── */
h1 {{
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 1.875rem !important; font-weight: 800 !important;
    color: {TEXT_MAIN} !important; letter-spacing: -0.03em !important;
    line-height: 1.2 !important; margin-bottom: 0.25rem !important;
}}
h2 {{
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 1.125rem !important; font-weight: 700 !important;
    color: {TEXT_MAIN} !important; letter-spacing: -0.01em !important;
    line-height: 1.3 !important; margin-top: 1.5rem !important;
}}
h3 {{
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 0.75rem !important; font-weight: 600 !important;
    color: {TEXT_MUTED} !important;
    text-transform: uppercase !important; letter-spacing: 0.08em !important;
}}
p, li, td, th {{
    font-family: 'Inter', 'Plus Jakarta Sans', sans-serif !important;
    font-size: 0.875rem !important; color: {TEXT_MAIN} !important;
    line-height: 1.65 !important;
}}
/* Tabular numbers for all data values */
[data-testid="stMetricValue"], .tabnum {{
    font-variant-numeric: tabular-nums !important;
    font-feature-settings: "tnum" !important;
}}
.stCaption, [data-testid="stCaption"] {{
    font-size: 0.8rem !important; color: {TEXT_MUTED} !important;
    font-family: 'Inter', sans-serif !important; line-height: 1.5 !important;
}}

/* ── KPI Metric cards ── */
[data-testid="stMetric"] {{
    background: {CARD_BG} !important;
    border: 1px solid {BORDER_COL} !important;
    border-radius: 14px !important; padding: 18px 20px !important;
    box-shadow: {SHADOW} !important;
    transition: box-shadow 0.2s ease, transform 0.2s ease !important;
}}
[data-testid="stMetric"]:hover {{
    box-shadow: {SHADOW_HOVER} !important;
    transform: translateY(-1px) !important;
}}
[data-testid="stMetricLabel"] {{
    font-size: 0.68rem !important; font-weight: 600 !important;
    color: {TEXT_MUTED} !important; text-transform: uppercase !important;
    letter-spacing: 0.08em !important; font-family: 'Inter', sans-serif !important;
}}
[data-testid="stMetricValue"] {{
    font-size: 1.75rem !important; font-weight: 800 !important;
    color: {TEXT_MAIN} !important; letter-spacing: -0.02em !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-variant-numeric: tabular-nums !important;
}}

/* ── Sidebar ── */
[data-testid="stSidebar"] {{
    background-color: {SIDEBAR_BG} !important;
    border-right: 1px solid rgba(255,255,255,0.06) !important;
}}
[data-testid="stSidebar"] * {{ color: {TEXT_ON_DARK} !important; }}
[data-testid="stSidebar"] label {{
    font-size: 0.68rem !important; font-weight: 600 !important;
    color: rgba(237,233,255,0.45) !important;
    text-transform: uppercase !important; letter-spacing: 0.1em !important;
    font-family: 'Inter', sans-serif !important;
}}
[data-testid="stSidebar"] .stRadio label {{
    text-transform: none !important; font-size: 0.875rem !important;
    font-weight: 500 !important; color: rgba(237,233,255,0.75) !important;
    letter-spacing: 0 !important; font-family: 'Plus Jakarta Sans', sans-serif !important;
    padding: 3px 0 !important;
}}
[data-testid="stSidebar"] [data-testid="stRadioGroup"] label:hover {{
    color: {TEXT_ON_DARK} !important;
}}
[data-testid="stSidebar"] hr {{
    border-color: rgba(255,255,255,0.08) !important; margin: 12px 0 !important;
}}

/* ── Multiselect tags — pastel pink ── */
[data-baseweb="tag"] {{
    background-color: #8B3062 !important;
    border: 1px solid #F9C0D3 !important;
    border-radius: 20px !important;
}}
[data-baseweb="tag"] span {{
    color: #FDE8F1 !important; font-weight: 600 !important;
    font-size: 11px !important; font-family: 'Inter', sans-serif !important;
}}
[data-baseweb="tag"] [role="presentation"] svg,
[data-baseweb="tag"] button svg {{ fill: #F9C0D3 !important; }}

/* ── Selectbox / inputs — light ── */
[data-baseweb="input"], [data-baseweb="select"],
[data-testid="stMultiSelect"] > div,
[data-testid="stSelectbox"] > div > div {{
    background-color: #F0EEF9 !important;
    border-color: {BORDER_COL} !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}}
[data-baseweb="menu"] {{
    background-color: {CARD_BG} !important;
    border: 1px solid {BORDER_COL} !important;
    box-shadow: {SHADOW} !important;
}}
[data-baseweb="menu"] li {{ color: {TEXT_MAIN} !important; font-size: 0.875rem !important; }}
[data-baseweb="menu"] li:hover {{ background-color: {PRIMARY_LIGHT} !important; }}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {{
    background: {CARD_BG}; border-radius: 12px;
    padding: 4px; gap: 2px;
    border: 1px solid {BORDER_COL};
    box-shadow: {SHADOW};
}}
.stTabs [data-baseweb="tab"] {{
    border-radius: 9px; font-weight: 500;
    color: {TEXT_MUTED} !important;
    font-size: 0.85rem; padding: 6px 18px;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    transition: all 0.15s ease;
}}
.stTabs [aria-selected="true"] {{
    background: {PRIMARY_LIGHT} !important;
    color: {PRIMARY} !important;
    font-weight: 700 !important;
}}

/* ── Dimension pill buttons ── */
[data-testid="stBaseButton-secondary"] {{
    background: {CARD_BG} !important;
    border: 1.5px solid {BORDER_COL} !important;
    border-radius: 100px !important;
    color: {TEXT_MUTED} !important;
    font-size: 0.8rem !important; font-weight: 600 !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    transition: all 0.15s ease !important;
    padding: 6px 0 !important;
    letter-spacing: 0.01em !important;
}}
[data-testid="stBaseButton-secondary"]:hover {{
    border-color: {PRIMARY} !important;
    color: {PRIMARY} !important;
    background: {PRIMARY_LIGHT} !important;
    box-shadow: 0 0 0 3px rgba(114,117,179,0.12) !important;
}}
[data-testid="stBaseButton-primary"] {{
    background: linear-gradient(135deg, #5254A3 0%, #7275B3 100%) !important;
    border: 1.5px solid #5254A3 !important;
    border-radius: 100px !important;
    color: #FFFFFF !important;
    font-size: 0.8rem !important; font-weight: 700 !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    box-shadow: 0 2px 12px rgba(82,84,163,0.28) !important;
    padding: 6px 0 !important;
    letter-spacing: 0.01em !important;
}}
[data-testid="stBaseButton-primary"]:hover {{
    background: linear-gradient(135deg, #4446A0 0%, #6568B0 100%) !important;
    box-shadow: 0 4px 20px rgba(82,84,163,0.35) !important;
    transform: translateY(-1px) !important;
}}

/* ── Expander ── */
[data-testid="stExpander"] {{
    background: {CARD_BG} !important;
    border: 1px solid {BORDER_COL} !important;
    border-radius: 12px !important; overflow: hidden !important;
}}
[data-testid="stExpander"] summary {{
    font-size: 0.72rem !important; font-weight: 600 !important;
    color: rgba(237,233,255,0.5) !important;
    text-transform: uppercase !important; letter-spacing: 0.08em !important;
    font-family: 'Inter', sans-serif !important;
}}

/* ── Dataframe ── */
[data-testid="stDataFrame"] {{ border-radius: 12px !important; overflow: hidden !important; }}

/* ── Slider ── */
[data-testid="stSlider"] [data-baseweb="slider"] [role="slider"] {{
    background: {PRIMARY} !important;
}}

/* ── Page divider ── */
.divider {{ height: 1px; background: {BORDER_COL}; margin: 1.5rem 0; }}

/* ── Section label — like Stripe/Linear ── */
.section-label {{
    font-size: 0.68rem; font-weight: 700; color: {TEXT_MUTED};
    text-transform: uppercase; letter-spacing: 0.1em;
    font-family: 'Inter', sans-serif; margin-bottom: 0.5rem;
}}

/* ── Cluster badge ── */
.cluster-badge {{
    display: inline-block; border-radius: 100px;
    padding: 3px 12px; font-size: 11px; font-weight: 700;
    font-family: 'Inter', sans-serif; letter-spacing: 0.03em;
}}

/* ── Card ── */
.metric-card {{
    background: {CARD_BG}; border: 1px solid {BORDER_COL};
    border-radius: 14px; padding: 16px 20px;
    box-shadow: {SHADOW};
}}
.insight-card {{
    border-radius: 12px; padding: 12px 16px; margin: 5px 0;
    border-left: 3px solid; font-family: 'Inter', sans-serif;
}}

/* ── Image placeholder ── */
.img-placeholder {{
    border-radius: 12px; display: flex; align-items: center;
    justify-content: center; color: rgba(255,255,255,0.8);
    font-weight: 600; font-size: 12px; letter-spacing: 0.06em;
    text-transform: uppercase; font-family: 'Inter', sans-serif;
}}

/* ── Hero section ── */
.hero-text {{ position: relative; z-index: 2; }}

/* ── Scrollbar ── */
::-webkit-scrollbar {{ width: 6px; height: 6px; }}
::-webkit-scrollbar-track {{ background: {PAGE_BG}; }}
::-webkit-scrollbar-thumb {{ background: {BORDER_COL}; border-radius: 3px; }}
::-webkit-scrollbar-thumb:hover {{ background: {PRIMARY}; }}

/* ── Responsive adjustments ── */
@media (max-width: 768px) {{
    h1 {{ font-size: 1.4rem !important; }}
    .block-container {{ padding: 1rem !important; }}
}}
</style>
""", unsafe_allow_html=True)


# ─── Helpers ──────────────────────────────────────────────────────────────────
def hex_to_rgb(h):
    h = h.lstrip("#")
    return [int(h[i:i+2], 16) for i in (0, 2, 4)]

def divider():
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

def section_label(text):
    st.markdown(f'<div class="section-label">{text}</div>', unsafe_allow_html=True)

def empty_state(msg="No cities match your current filters."):
    st.markdown(
        f'<div style="text-align:center;padding:60px 20px">'
        f'<div style="width:48px;height:48px;border-radius:50%;background:{PRIMARY_LIGHT};'
        f'margin:0 auto 16px;display:flex;align-items:center;justify-content:center;'
        f'font-size:20px">?</div>'
        f'<div style="font-size:0.9rem;font-weight:600;color:{TEXT_MAIN}">{msg}</div>'
        f'<div style="font-size:0.8rem;color:{TEXT_MUTED};margin-top:4px">'
        f'Try adjusting the filters.</div></div>',
        unsafe_allow_html=True,
    )

def show_image(filename, fallback_text, fallback_color="#B4B8E0", height=180):
    """Show image if exists, else styled placeholder with instructions."""
    path = ASSETS / filename
    if path.exists():
        st.image(str(path), use_container_width=True)
    else:
        rv, gv, bv = hex_to_rgb(fallback_color)
        st.markdown(
            f'<div class="img-placeholder" style="height:{height}px;'
            f'background:linear-gradient(135deg,rgba({rv},{gv},{bv},0.7),'
            f'rgba({rv},{gv},{bv},0.4));border:1.5px dashed rgba({rv},{gv},{bv},0.6)">'
            f'[ {fallback_text} ]</div>',
            unsafe_allow_html=True,
        )

def chart_defaults():
    return dict(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, Plus Jakarta Sans, sans-serif",
                  color=TEXT_MAIN, size=12),
    )

CHART_H    = 460
CHART_H_SM = 280


# ─── Data ─────────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv(DATA_DIR / "cities_clustered.csv")
    score_cols = [c for c in df.columns if "_score" in c or c == "opportunity_index"]
    df[score_cols] = df[score_cols].round(2)
    return df

df_all = load_data()
all_clusters  = sorted(df_all["cluster"].unique())
cluster_names = df_all.groupby("cluster")["cluster_name"].first().to_dict()
color_map     = {cluster_names[c]: CLUSTER_COLORS[c] for c in all_clusters}


# ═══════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ═══════════════════════════════════════════════════════════════════════════════
with st.sidebar:
    # Brand
    st.markdown(
        f'<div style="padding:4px 0 20px">'
        f'<div style="font-size:1.1rem;font-weight:800;color:#F1EEFF;'
        f'font-family:Plus Jakarta Sans,sans-serif;letter-spacing:-0.02em">'
        f'CityMetric</div>'
        f'<div style="font-size:0.72rem;color:rgba(237,233,255,0.45);'
        f'font-family:Inter,sans-serif;margin-top:2px;letter-spacing:0.04em">'
        f'GLOBAL CITY INDEX</div></div>',
        unsafe_allow_html=True,
    )

    # Navigation
    page = st.radio(
        "Navigate",
        ["Overview","World Map","Cluster Analysis",
         "Dimension Deep-Dive","City Comparison","Insights","About"],
        label_visibility="collapsed",
    )

    st.markdown('<hr/>', unsafe_allow_html=True)

    # Filters
    with st.expander("Filters", expanded=True):
        sel_clusters = st.multiselect(
            "Cluster",
            options=all_clusters, default=all_clusters,
            format_func=lambda c: cluster_names[c],
        )
        all_regions = sorted(df_all["region"].unique())
        sel_regions = st.multiselect(
            "Region", options=all_regions, default=all_regions,
        )
        opp_min = st.slider("Min Opportunity Score", 0.0, 10.0, 0.0, 0.1)
        highlight = st.selectbox(
            "Map dimension",
            ["opportunity_index"] + DIMS,
            format_func=lambda x: x.replace("_score","").replace("_"," ").title(),
        )

    st.markdown('<hr/>', unsafe_allow_html=True)
    st.markdown(
        f'<div style="font-size:0.68rem;color:rgba(237,233,255,0.3);'
        f'font-family:Inter,sans-serif;line-height:1.8">'
        f'55 cities · 6 dimensions<br>'
        f'Numbeo · World Bank · NOAA<br>'
        f'Stack Overflow · CWUR</div>',
        unsafe_allow_html=True,
    )

# ─── Filter ───────────────────────────────────────────────────────────────────
df = df_all[
    df_all["cluster"].isin(sel_clusters if sel_clusters else all_clusters) &
    df_all["region"].isin(sel_regions if sel_regions else all_regions) &
    (df_all["opportunity_index"] >= opp_min)
].copy()


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: OVERVIEW
# ═══════════════════════════════════════════════════════════════════════════════
if page == "Overview":

    # ── Hero image ────────────────────────────────────────────────────────────
    # IMAGE NEEDED: assets/hero_city.jpg
    # Aerial/night cityscape, wide format (1400x280px recommended).
    # Suggestion: night aerial of a major city (Tokyo, NYC, Singapore).
    # Dark-toned photo so the overlay text reads clearly.
    show_image(
        "hero_city.jpg",
        "Place hero image here — assets/hero_city.jpg (1400x280px aerial city night)",
        "#7275B3", height=200,
    )
    st.markdown('<div style="margin-top:1.5rem"></div>', unsafe_allow_html=True)

    st.title("Global City Opportunity & Innovation Index")
    st.caption(
        "Data-driven analysis of 55 global cities across 6 key dimensions — "
        "find where to build, invest, or move."
    )
    divider()

    if len(df) == 0:
        empty_state()
    else:
        # ── KPIs ─────────────────────────────────────────────────────────────
        k1, k2, k3, k4, k5 = st.columns(5)
        top_city = df_all.loc[df_all["opportunity_index"].idxmax(), "city"]
        k1.metric("Cities Shown",    f"{len(df)} / {len(df_all)}")
        k2.metric("Clusters",        f"{df['cluster'].nunique()}")
        k3.metric("Avg Opportunity", f"{df['opportunity_index'].mean():.2f}")
        k4.metric("Top City",        top_city)
        k5.metric("Data Sources",    "8+")
        divider()

        col_left, col_right = st.columns([3, 2], gap="large")

        with col_left:
            section_label("Rankings")
            st.subheader("Top 20 Cities")
            top20 = df.nlargest(20, "opportunity_index").sort_values("opportunity_index")
            fig = px.bar(
                top20, x="opportunity_index", y="city",
                color="cluster_name", color_discrete_map=color_map,
                orientation="h", text="opportunity_index",
                labels={"opportunity_index":"Opportunity Index","city":"","cluster_name":"Cluster"},
                template="plotly_white",
            )
            fig.update_traces(
                texttemplate="%{x:.2f}", textposition="outside",
                marker_line_width=0, marker_opacity=0.9,
            )
            fig.update_layout(
                **chart_defaults(), height=CHART_H,
                xaxis=dict(range=[0, top20["opportunity_index"].max()+0.8],
                           showgrid=True, gridcolor=GRID_COL,
                           tickfont=dict(color=TEXT_MUTED, size=11),
                           title_font=dict(color=TEXT_MUTED)),
                yaxis=dict(showgrid=False, tickfont=dict(color=TEXT_MAIN, size=11)),
                legend=dict(orientation="h", y=-0.12, font=dict(size=11), title=""),
                margin=dict(l=0, r=50, t=10, b=40),
            )
            st.plotly_chart(fig, use_container_width=True)

        with col_right:
            section_label("Distribution")
            st.subheader("Cluster Breakdown")
            counts = df.groupby("cluster_name").size().reset_index(name="count")
            fig2 = px.pie(
                counts, values="count", names="cluster_name",
                color="cluster_name", color_discrete_map=color_map,
                hole=0.55, template="plotly_white",
            )
            fig2.update_traces(
                textposition="outside", textinfo="label+percent",
                marker=dict(line=dict(color="#FFFFFF", width=3)),
                textfont=dict(size=11, family="Inter"),
            )
            fig2.update_layout(
                **chart_defaults(), height=260,
                showlegend=False, margin=dict(t=10, b=10, l=20, r=20),
            )
            st.plotly_chart(fig2, use_container_width=True)

            section_label("Geography")
            st.subheader("Regional Averages")
            reg = (df.groupby("region")["opportunity_index"]
                   .mean().sort_values(ascending=True).reset_index())
            fig3 = px.bar(
                reg, x="opportunity_index", y="region", orientation="h",
                color="opportunity_index",
                color_continuous_scale=[[0,"#D1D4F5"],[0.5,"#7275B3"],[1,"#3A3B8E"]],
                text="opportunity_index",
                labels={"opportunity_index":"Avg Score","region":""},
                template="plotly_white",
            )
            fig3.update_traces(
                texttemplate="%{x:.2f}", textposition="outside",
                marker_line_width=0,
            )
            fig3.update_layout(
                **chart_defaults(), height=230,
                coloraxis_showscale=False,
                xaxis=dict(range=[0, reg["opportunity_index"].max()+0.5],
                           showgrid=False, tickfont=dict(color=TEXT_MUTED)),
                yaxis=dict(showgrid=False, tickfont=dict(color=TEXT_MAIN, size=11)),
                margin=dict(l=0, r=50, t=0, b=0),
            )
            st.plotly_chart(fig3, use_container_width=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: WORLD MAP
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "World Map":
    st.title("City Intelligence Map")

    # Cluster legend
    legend_cols = st.columns(len(all_clusters))
    for i, c in enumerate(all_clusters):
        legend_cols[i].markdown(
            f'<span class="cluster-badge" style="background:{CLUSTER_COLORS[c]};'
            f'color:{CLUSTER_DARK[c]};border:1.5px solid {CLUSTER_DARK[c]}44">'
            f'{cluster_names[c]}</span>',
            unsafe_allow_html=True,
        )
    st.markdown("")

    if len(df) == 0:
        empty_state()
    else:
        tab1, tab2, tab3 = st.tabs(["Interactive Map","3D Globe","Heatmap"])

        with tab1:
            st.caption("Hover any city · Zoom & pan · Click legend items to filter")
            with st.spinner("Loading map..."):
                df["_hover"] = df.apply(lambda r: (
                    f"<b style='font-size:14px'>{r['city']}, {r['country']}</b><br>"
                    f"<span style='color:#888;font-size:12px'>{r['cluster_name']}</span>"
                    f"<br><br>"
                    f"<b>Opportunity</b>  {r['opportunity_index']:.2f}/10<br><br>"
                    f"Affordability  {r['affordability_score']:.2f}<br>"
                    f"Digital  {r['digital_score']:.2f} &nbsp; Urban  {r['urban_score']:.2f}<br>"
                    f"Innovation  {r['innovation_score']:.2f} &nbsp; Talent  {r['talent_score']:.2f}<br>"
                    f"Growth  {r['growth_score']:.2f}"
                ), axis=1)
                fig_map = px.scatter_mapbox(
                    df, lat="latitude", lon="longitude",
                    color="cluster_name", color_discrete_map=color_map,
                    size="opportunity_index", size_max=22,
                    hover_name="city", custom_data=["_hover"],
                    zoom=1.4, center={"lat":20,"lon":10},
                    mapbox_style="open-street-map", height=560,
                )
                fig_map.update_traces(
                    hovertemplate="%{customdata[0]}<extra></extra>",
                    marker=dict(opacity=0.88, sizemin=7),
                )
                fig_map.update_layout(
                    **chart_defaults(),
                    margin=dict(l=0,r=0,t=0,b=0),
                    legend=dict(
                        title="", bgcolor="rgba(255,255,255,0.92)",
                        bordercolor=BORDER_COL, borderwidth=1,
                        x=0.01, y=0.99, font=dict(size=12),
                    ),
                )
                st.plotly_chart(fig_map, use_container_width=True)

        with tab2:
            st.caption("Drag to rotate · Scroll to zoom · Hover for city data · Column height = Opportunity")
            with st.spinner("Building 3D view..."):
                import pydeck as pdk
                df_deck = df.copy()
                df_deck["color"]      = df_deck["cluster"].map(lambda c: hex_to_rgb(CLUSTER_COLORS[c]))
                df_deck["color_dark"] = df_deck["cluster"].map(lambda c: hex_to_rgb(CLUSTER_DARK[c]))
                df_deck["elevation"]  = df_deck["opportunity_index"] * 130000
                df_deck["radius"]     = (df_deck["opportunity_index"] * 55000 + 70000).astype(int)

                col_layer = pdk.Layer(
                    "ColumnLayer", data=df_deck,
                    get_position=["longitude","latitude"],
                    get_elevation="elevation", radius=75000,
                    get_fill_color="color",
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
                view = pdk.ViewState(latitude=20, longitude=10, zoom=1.2, pitch=48)
                tooltip = {
                    "html": (
                        "<b>{city}, {country}</b><br/>"
                        "<span style='color:#B4B8E0'>{cluster_name}</span><br/><br/>"
                        "Opportunity: <b>{opportunity_index}</b>/10<br/>"
                        "Digital: {digital_score} · Innovation: {innovation_score}"
                    ),
                    "style": {
                        "background":"rgba(28,23,51,0.96)",
                        "color":"#F1EEFF",
                        "font-family":"Inter,sans-serif",
                        "font-size":"13px",
                        "padding":"12px 14px",
                        "border-radius":"10px",
                        "border":"1px solid rgba(180,184,224,0.3)",
                    },
                }
                deck = pdk.Deck(
                    layers=[scatter_layer, col_layer],
                    initial_view_state=view, tooltip=tooltip,
                    map_style="https://basemaps.cartocdn.com/gl/positron-gl-style/style.json",
                )
                st.pydeck_chart(deck, use_container_width=True, height=560)

        with tab3:
            dim_choice = st.selectbox(
                "Dimension",
                ["opportunity_index"] + DIMS,
                format_func=lambda x: x.replace("_score","").replace("_"," ").title(),
            )
            with st.spinner("Loading heatmap..."):
                fig_heat = px.density_mapbox(
                    df, lat="latitude", lon="longitude",
                    z=dim_choice, radius=55, zoom=1.3,
                    center={"lat":20,"lon":10},
                    mapbox_style="carto-positron",
                    color_continuous_scale=["#FFF7E4","#D1D4F5","#7275B3","#3A3B8E"],
                    hover_name="city",
                    hover_data={"latitude":False,"longitude":False,dim_choice:":.2f"},
                    height=540,
                )
                fig_heat.update_layout(
                    **chart_defaults(),
                    margin=dict(l=0,r=0,t=0,b=0),
                    coloraxis_colorbar=dict(
                        title=dim_choice.replace("_score","").title(),
                        tickformat=".1f",len=0.6,
                        tickfont=dict(color=TEXT_MUTED),
                        title_font=dict(color=TEXT_MUTED),
                    ),
                )
                st.plotly_chart(fig_heat, use_container_width=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: CLUSTER ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "Cluster Analysis":
    st.title("Cluster Analysis")
    st.caption("Explore how cities group together based on their combined opportunity profiles.")
    divider()

    sel_c  = st.selectbox(
        "Select cluster",
        options=all_clusters,
        format_func=lambda c: f"{cluster_names[c]}",
    )
    cdata = df_all[df_all["cluster"] == sel_c]
    color = CLUSTER_COLORS[sel_c]
    rv, gv, bv = hex_to_rgb(color)

    # KPIs
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Cities",            len(cdata))
    k2.metric("Avg Opportunity",   f"{cdata['opportunity_index'].mean():.2f}")
    k3.metric("Avg Affordability", f"{cdata['affordability_score'].mean():.2f}")
    k4.metric("Avg Growth",        f"{cdata['growth_score'].mean():.2f}")

    divider()

    # Cluster image + radar side by side
    img_col, radar_col, table_col = st.columns([1, 1.4, 1.6], gap="large")

    with img_col:
        section_label("Representative City")
        # IMAGE NEEDED: assets/cluster_0.jpg through assets/cluster_4.jpg
        # 400x260px city photo representing each cluster archetype:
        # cluster_0 = Balanced Cities (e.g. Barcelona street view)
        # cluster_1 = Digital Leaders (e.g. Tokyo/Amsterdam skyline)
        # cluster_2 = Established Hubs (e.g. NYC/London at night)
        # cluster_3 = Rising Stars (e.g. Seoul/Bangalore tech district)
        # cluster_4 = Emerging Markets (e.g. Jakarta/Mumbai aerial)
        show_image(
            f"cluster_{sel_c}.jpg",
            f"assets/cluster_{sel_c}.jpg · 400x260px",
            color, height=260,
        )
        st.markdown(
            f'<div style="margin-top:12px">'
            f'<span class="cluster-badge" style="background:{color};color:{CLUSTER_DARK[sel_c]};'
            f'border:1.5px solid {CLUSTER_DARK[sel_c]}44">{cluster_names[sel_c]}</span>'
            f'<div style="font-size:0.78rem;color:{TEXT_MUTED};margin-top:8px;'
            f'font-family:Inter,sans-serif;line-height:1.6">'
            f'{len(cdata)} cities · {len(cdata)/len(df_all)*100:.0f}% of dataset</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

    with radar_col:
        section_label("Dimension Profile")
        means = cdata[DIMS].mean().tolist() + [cdata[DIMS[0]].mean()]
        cats  = DIM_LABELS + [DIM_LABELS[0]]
        fig_r = go.Figure(go.Scatterpolar(
            r=means, theta=cats, fill="toself",
            line_color=CLUSTER_DARK[sel_c], line_width=2.5,
            fillcolor=f"rgba({rv},{gv},{bv},0.35)",
        ))
        fig_r.update_layout(
            **chart_defaults(),
            polar=dict(
                radialaxis=dict(range=[0,10],
                                tickfont=dict(size=10, color=TEXT_MUTED),
                                gridcolor=GRID_COL, linecolor=BORDER_COL),
                angularaxis=dict(tickfont=dict(size=12, color=TEXT_MAIN)),
                bgcolor="rgba(0,0,0,0)",
            ),
            height=300, showlegend=False,
            margin=dict(t=20, b=20, l=20, r=20),
        )
        st.plotly_chart(fig_r, use_container_width=True)

    with table_col:
        section_label(f"Cities in this cluster")
        rename_map = {d: d.replace("_score","").title() for d in DIMS}
        rename_map["opportunity_index"] = "Score"
        display_df = (
            cdata[["city","country","opportunity_index"] + DIMS]
            .sort_values("opportunity_index", ascending=False)
            .reset_index(drop=True)
            .rename(columns=rename_map)
        )
        num_cols = display_df.select_dtypes("number").columns
        display_df[num_cols] = display_df[num_cols].round(2)
        st.dataframe(
            display_df.style
                .background_gradient(subset=["Score"], cmap="BuPu")
                .format({c: "{:.2f}" for c in num_cols}),
            use_container_width=True, height=330,
        )

    divider()
    section_label("All clusters compared")
    st.subheader("Side-by-Side Profiles")
    fig_all = make_subplots(
        rows=1, cols=5, specs=[[{"type":"polar"}]*5],
        subplot_titles=[cluster_names[c] for c in all_clusters],
    )
    for i, c in enumerate(all_clusters, start=1):
        sub   = df_all[df_all["cluster"]==c]
        vals  = sub[DIMS].mean().tolist() + [sub[DIMS[0]].mean()]
        col_h = CLUSTER_COLORS[c]
        r2,g2,b2 = hex_to_rgb(col_h)
        fig_all.add_trace(
            go.Scatterpolar(
                r=vals, theta=DIM_LABELS+[DIM_LABELS[0]], fill="toself",
                line_color=CLUSTER_DARK[c], line_width=1.8,
                fillcolor=f"rgba({r2},{g2},{b2},0.4)",
                name=cluster_names[c],
            ), row=1, col=i,
        )
        pk = "polar" if i==1 else f"polar{i}"
        fig_all.update_layout(**{
            pk: dict(
                radialaxis=dict(range=[0,10], tickfont_size=7,
                                gridcolor=GRID_COL, linecolor=BORDER_COL,
                                tickfont=dict(color=TEXT_MUTED)),
                angularaxis=dict(tickfont=dict(size=9, color=TEXT_MUTED)),
                bgcolor="rgba(0,0,0,0)",
            )
        })
    fig_all.update_layout(
        **chart_defaults(), height=340, showlegend=False,
        margin=dict(t=30, b=10),
    )
    st.plotly_chart(fig_all, use_container_width=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: DIMENSION DEEP-DIVE
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "Dimension Deep-Dive":
    st.title("Dimension Deep-Dive")
    st.caption("Explore any single dimension across all cities and regions.")
    divider()

    # Pill buttons
    if "sel_dim" not in st.session_state:
        st.session_state.sel_dim = DIMS[0]

    btn_cols = st.columns(len(DIMS))
    for i, (d, lbl) in enumerate(zip(DIMS, DIM_LABELS)):
        with btn_cols[i]:
            is_active = (st.session_state.sel_dim == d)
            if st.button(
                lbl, key=f"dim_{d}",
                use_container_width=True,
                type="primary" if is_active else "secondary",
            ):
                st.session_state.sel_dim = d
                st.rerun()

    sel_dim = st.session_state.sel_dim
    label   = sel_dim.replace("_score","").title()

    if len(df) == 0:
        empty_state()
    else:
        divider()
        col1, col2 = st.columns([3, 2], gap="large")

        with col1:
            section_label(f"Rankings — {label}")
            st.subheader(f"Top 20 Cities")
            top_dim = df.nlargest(20, sel_dim).sort_values(sel_dim)
            fig = px.bar(
                top_dim, x=sel_dim, y="city",
                color="cluster_name", color_discrete_map=color_map,
                orientation="h", text=sel_dim,
                labels={sel_dim:f"{label} Score","city":""},
                template="plotly_white",
            )
            fig.update_traces(
                texttemplate="%{x:.2f}", textposition="outside", marker_line_width=0,
            )
            fig.update_layout(
                **chart_defaults(), height=CHART_H,
                xaxis=dict(range=[0, top_dim[sel_dim].max()+0.8],
                           showgrid=True, gridcolor=GRID_COL,
                           tickfont=dict(color=TEXT_MUTED)),
                yaxis=dict(showgrid=False, tickfont=dict(color=TEXT_MAIN, size=11)),
                legend=dict(title="", orientation="h", y=-0.1, font=dict(size=11)),
                margin=dict(l=0, r=50, t=10, b=40),
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            section_label("By Region")
            st.subheader("Regional Average")
            reg_dim = df.groupby("region")[sel_dim].mean().sort_values(ascending=True).reset_index()
            fig2 = px.bar(
                reg_dim, x=sel_dim, y="region", orientation="h",
                color=sel_dim,
                color_continuous_scale=[[0,"#D1D4F5"],[1,"#5254A3"]],
                text=sel_dim,
                labels={sel_dim:f"{label} Score","region":""},
                template="plotly_white",
            )
            fig2.update_traces(
                texttemplate="%{x:.2f}", textposition="outside", marker_line_width=0,
            )
            fig2.update_layout(
                **chart_defaults(), height=CHART_H_SM+20,
                coloraxis_showscale=False,
                xaxis=dict(range=[0, reg_dim[sel_dim].max()+0.5],
                           showgrid=False, tickfont=dict(color=TEXT_MUTED)),
                yaxis=dict(showgrid=False, tickfont=dict(color=TEXT_MAIN, size=11)),
                margin=dict(l=0, r=50, t=0, b=0),
            )
            st.plotly_chart(fig2, use_container_width=True)

            section_label("By Cluster")
            st.subheader("Distribution")
            fig3 = px.box(
                df, x="cluster_name", y=sel_dim,
                color="cluster_name", color_discrete_map=color_map,
                points="all", hover_data=["city"],
                labels={sel_dim:f"{label} Score","cluster_name":""},
                template="plotly_white",
            )
            fig3.update_layout(
                **chart_defaults(), height=CHART_H_SM,
                showlegend=False,
                xaxis=dict(tickfont=dict(size=10, color=TEXT_MUTED)),
                yaxis=dict(gridcolor=GRID_COL),
                margin=dict(t=0, b=0),
            )
            st.plotly_chart(fig3, use_container_width=True)

        divider()
        section_label("Relationships")
        st.subheader("Dimension Correlations")
        corr = df[DIMS].corr().round(2)
        fig4 = go.Figure(go.Heatmap(
            z=corr.values, x=DIM_LABELS, y=DIM_LABELS,
            colorscale=[[0,"#A7D8DE"],[0.5,"#F9F6F0"],[1,"#7275B3"]],
            zmin=-1, zmax=1,
            text=corr.values, texttemplate="%{text:.2f}",
            textfont=dict(size=12, family="Inter"),
            hovertemplate="%{y} × %{x}: %{z:.2f}<extra></extra>",
        ))
        fig4.update_layout(
            **chart_defaults(), height=380, width=540,
            margin=dict(l=0,r=0,t=0,b=0),
            xaxis=dict(tickfont=dict(size=12, color=TEXT_MAIN)),
            yaxis=dict(tickfont=dict(size=12, color=TEXT_MAIN)),
        )
        st.plotly_chart(fig4)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: CITY COMPARISON
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "City Comparison":
    st.title("City Comparison")
    st.caption("Select 2–6 cities to compare across all dimensions.")
    divider()

    default_cities = ["Bangkok","Lisbon","Singapore","Berlin","Seoul"]
    cities_to_compare = st.multiselect(
        "Choose cities",
        options=sorted(df_all["city"].unique()),
        default=[c for c in default_cities if c in df_all["city"].values],
        max_selections=6,
    )

    if len(cities_to_compare) < 2:
        st.markdown(
            f'<div style="text-align:center;padding:50px;color:{TEXT_MUTED}">'
            f'<div style="font-size:0.9rem;font-weight:600">Select at least 2 cities to compare.</div>'
            f'</div>', unsafe_allow_html=True,
        )
    else:
        cmp = df_all[df_all["city"].isin(cities_to_compare)].copy()

        section_label("Overlay")
        st.subheader("Dimension Profile Comparison")
        fig_radar = go.Figure()
        for i, (_, row) in enumerate(cmp.iterrows()):
            vals  = [row[d] for d in DIMS] + [row[DIMS[0]]]
            col_i = COMPARE_COLORS[i % len(COMPARE_COLORS)]
            rv, gv, bv = hex_to_rgb(col_i)
            fig_radar.add_trace(go.Scatterpolar(
                r=vals, theta=DIM_LABELS+[DIM_LABELS[0]], fill="toself",
                name=row["city"],
                line=dict(color=col_i, width=2.5),
                fillcolor=f"rgba({rv},{gv},{bv},0.1)",
            ))
        fig_radar.update_layout(
            **chart_defaults(),
            polar=dict(
                radialaxis=dict(range=[0,10],
                                tickfont=dict(size=11, color=TEXT_MUTED),
                                gridcolor=GRID_COL, linecolor=BORDER_COL),
                angularaxis=dict(tickfont=dict(size=13, color=TEXT_MAIN)),
                bgcolor="rgba(0,0,0,0)",
            ),
            height=CHART_H,
            legend=dict(orientation="h", y=-0.08, font=dict(size=12)),
            margin=dict(t=20, b=60),
        )
        st.plotly_chart(fig_radar, use_container_width=True)

        divider()
        col1, col2 = st.columns([1,1], gap="large")

        with col1:
            section_label("Score Breakdown")
            st.subheader("Per Dimension")
            melt = cmp.melt(id_vars=["city"], value_vars=DIMS,
                            var_name="dimension", value_name="score")
            melt["dimension"] = melt["dimension"].str.replace("_score","").str.title()
            city_colors = {row["city"]: COMPARE_COLORS[i]
                           for i,(_, row) in enumerate(cmp.iterrows())}
            fig_bar = px.bar(
                melt, x="dimension", y="score", color="city",
                barmode="group", color_discrete_map=city_colors,
                labels={"dimension":"","score":"Score (0–10)","city":""},
                template="plotly_white",
            )
            fig_bar.update_layout(
                **chart_defaults(), height=CHART_H_SM+40,
                legend=dict(orientation="h", y=-0.2, font=dict(size=11)),
                xaxis=dict(showgrid=False, tickfont=dict(color=TEXT_MUTED)),
                yaxis=dict(range=[0,11], gridcolor=GRID_COL),
                margin=dict(t=10, b=60),
            )
            st.plotly_chart(fig_bar, use_container_width=True)

        with col2:
            section_label("Summary")
            st.subheader("Score Table")
            tbl_cols = ["city","country","cluster_name","opportunity_index"] + DIMS
            rename = {d: d.replace("_score","").title() for d in DIMS}
            rename.update({"opportunity_index":"Score","cluster_name":"Cluster"})
            display_cmp = cmp[tbl_cols].set_index("city").rename(columns=rename)
            num_cols_c = display_cmp.select_dtypes("number").columns
            display_cmp[num_cols_c] = display_cmp[num_cols_c].round(2)
            st.dataframe(
                display_cmp.style
                    .background_gradient(subset=["Score"], cmap="BuPu")
                    .format({c:"{:.2f}" for c in num_cols_c}),
                use_container_width=True, height=CHART_H_SM+40,
            )


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: INSIGHTS
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "Insights":
    st.title("Key Insights")
    st.caption("What the data reveals about global city opportunities.")
    divider()

    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        section_label("Value")
        st.subheader("Best Value Cities")
        st.caption("High opportunity · High affordability")
        best = df_all.nlargest(20,"opportunity_index").nlargest(5,"affordability_score")
        for _, r in best.iterrows():
            c = CLUSTER_COLORS[r["cluster"]]
            d = CLUSTER_DARK[r["cluster"]]
            st.markdown(
                f'<div class="insight-card" style="background:{c}22;border-color:{d}">'
                f'<div style="font-weight:700;color:{TEXT_MAIN};font-family:Plus Jakarta Sans,sans-serif">'
                f'{r["city"]}</div>'
                f'<div style="font-size:11px;color:{TEXT_MUTED};font-family:Inter,sans-serif;margin-top:2px">'
                f'{r["country"]} · Score {r["opportunity_index"]:.2f} · '
                f'Afford {r["affordability_score"]:.2f}</div></div>',
                unsafe_allow_html=True,
            )

    with col2:
        section_label("Growth")
        st.subheader("Rising Stars")
        st.caption("Highest growth potential")
        stars = df_all.nlargest(5,"growth_score")
        for _, r in stars.iterrows():
            c = CLUSTER_COLORS[r["cluster"]]
            d = CLUSTER_DARK[r["cluster"]]
            st.markdown(
                f'<div class="insight-card" style="background:{c}22;border-color:{d}">'
                f'<div style="font-weight:700;color:{TEXT_MAIN};font-family:Plus Jakarta Sans,sans-serif">'
                f'{r["city"]}</div>'
                f'<div style="font-size:11px;color:{TEXT_MUTED};font-family:Inter,sans-serif;margin-top:2px">'
                f'{r["country"]} · Growth {r["growth_score"]:.2f} · '
                f'Opp {r["opportunity_index"]:.2f}</div></div>',
                unsafe_allow_html=True,
            )

    with col3:
        section_label("Innovation")
        st.subheader("Innovation Leaders")
        st.caption("Highest innovation scores")
        innov = df_all.nlargest(5,"innovation_score")
        for _, r in innov.iterrows():
            c = CLUSTER_COLORS[r["cluster"]]
            d = CLUSTER_DARK[r["cluster"]]
            st.markdown(
                f'<div class="insight-card" style="background:{c}22;border-color:{d}">'
                f'<div style="font-weight:700;color:{TEXT_MAIN};font-family:Plus Jakarta Sans,sans-serif">'
                f'{r["city"]}</div>'
                f'<div style="font-size:11px;color:{TEXT_MUTED};font-family:Inter,sans-serif;margin-top:2px">'
                f'{r["country"]} · Innov {r["innovation_score"]:.2f} · '
                f'Talent {r["talent_score"]:.2f}</div></div>',
                unsafe_allow_html=True,
            )

    divider()
    section_label("Key Findings")
    st.subheader("What the data says")

    findings = [
        (CLUSTER_COLORS[2], CLUSTER_DARK[2],
         "Digital score is the primary differentiator",
         "J48 Decision Tree identifies digital_score (threshold 5.2) as the single most important feature separating city archetypes. Cities above 5.2 are fundamentally different from those below."),
        (CLUSTER_COLORS[0], CLUSTER_DARK[0],
         "Top cities are concentrated in the USA",
         "Los Angeles, New York, San Francisco, and Chicago dominate the top 4 — driven by exceptional developer density and R&D investment, despite high living costs."),
        (CLUSTER_COLORS[3], CLUSTER_DARK[3],
         "Asia-Pacific offers the best value proposition",
         "Melbourne, Sydney, Seoul, and Bangalore combine high opportunity scores with significantly better affordability than Western counterparts."),
        (CLUSTER_COLORS[1], CLUSTER_DARK[1],
         "Innovation is highly concentrated geographically",
         "40% of all cities score below 2.0 on innovation. Top innovation scores are almost exclusively in USA and select European cities, revealing a significant global gap."),
        (CLUSTER_COLORS[4], CLUSTER_DARK[4],
         "Digital divide mirrors economic development",
         "Emerging Markets cluster averages 2.5/10 on digital infrastructure vs 9.0/10 for Digital Leaders — a 6.5-point gap that correlates directly with economic output."),
        (CLUSTER_COLORS[2], CLUSTER_DARK[2],
         "EM clustering validates K-Means findings",
         "Using a probabilistic approach (EM), the same 5 archetypes emerge with consistent proportions, confirming the clustering solution is not random but reflects real underlying structure."),
    ]

    f_col1, f_col2 = st.columns(2, gap="medium")
    for i, (bg, border, title, desc) in enumerate(findings):
        target = f_col1 if i % 2 == 0 else f_col2
        target.markdown(
            f'<div class="insight-card" style="background:{bg}15;border-color:{border};margin-bottom:10px">'
            f'<div style="font-weight:700;font-size:0.85rem;color:{TEXT_MAIN};'
            f'font-family:Plus Jakarta Sans,sans-serif;margin-bottom:4px">{title}</div>'
            f'<div style="font-size:0.8rem;color:{TEXT_MUTED};font-family:Inter,sans-serif;'
            f'line-height:1.6">{desc}</div></div>',
            unsafe_allow_html=True,
        )

    divider()
    section_label("Scatter Analysis")
    st.subheader("Digital Infrastructure vs Innovation")
    if len(df) > 0:
        fig_scatter = px.scatter(
            df_all, x="digital_score", y="innovation_score",
            color="cluster_name", color_discrete_map=color_map,
            size="talent_score", text="city",
            hover_data={"country":True,"opportunity_index":":.2f",
                        "growth_score":":.2f","cluster_name":False},
            labels={"digital_score":"Digital Score","innovation_score":"Innovation Score",
                    "cluster_name":"Cluster"},
            template="plotly_white",
        )
        fig_scatter.update_traces(
            textposition="top center",
            textfont=dict(size=8, color=TEXT_MUTED, family="Inter"),
        )
        fig_scatter.update_layout(
            **chart_defaults(), height=CHART_H,
            xaxis=dict(gridcolor=GRID_COL, title_font=dict(size=12,color=TEXT_MUTED),
                       tickfont=dict(color=TEXT_MUTED)),
            yaxis=dict(gridcolor=GRID_COL, title_font=dict(size=12,color=TEXT_MUTED),
                       tickfont=dict(color=TEXT_MUTED)),
            legend=dict(title="", font=dict(size=11)),
            margin=dict(t=10, b=10),
        )
        st.plotly_chart(fig_scatter, use_container_width=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGE: ABOUT
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "About":
    # IMAGE NEEDED: assets/about_banner.jpg
    # Abstract city data visualization or aerial city overview, 1200x220px.
    # Style: wide, cinematic, slightly desaturated to match pastel palette.
    # Suggestion: blue-hour aerial city photo or abstract geometric city art.
    show_image(
        "about_banner.jpg",
        "assets/about_banner.jpg — 1200x220px · aerial city or data art",
        "#A7D8DE", height=180,
    )
    st.markdown('<div style="margin-top:1.5rem"></div>', unsafe_allow_html=True)

    st.title("About CityMetric")
    divider()

    col1, col2 = st.columns([3,2], gap="large")

    with col1:
        section_label("Project")
        st.subheader("What is CityMetric?")
        st.markdown(
            "CityMetric analyses **55 global cities** across **6 key dimensions** to answer: "
            "*Where should you build, invest, or move?*\n\n"
            "It combines data from 8+ global sources, engineers composite scores "
            "using Min-Max normalization, clusters cities into 5 archetypes via "
            "**K-Means (WEKA SimpleKMeans K=5)**, and presents findings through "
            "this interactive dashboard."
        )

        divider()
        section_label("Methodology")
        st.subheader("6 Dimensions")

        for lbl, desc in zip(DIM_LABELS, [
            "Salary-to-rent ratio, food & utility costs, transport",
            "Internet penetration %, broadband, mobile subscriptions",
            "Population density, climate comfort, urban growth",
            "R&D spending, research publications, university rankings",
            "Education enrollment, developer density, skill seniority",
            "GDP growth, population trend, high-tech export share",
        ]):
            st.markdown(
                f'<div style="display:flex;gap:14px;padding:10px 0;'
                f'border-bottom:1px solid {BORDER_COL}">'
                f'<div style="min-width:100px;font-weight:700;font-size:0.82rem;'
                f'color:{PRIMARY};font-family:Plus Jakarta Sans,sans-serif">{lbl}</div>'
                f'<div style="font-size:0.82rem;color:{TEXT_MUTED};'
                f'font-family:Inter,sans-serif;line-height:1.6">{desc}</div>'
                f'</div>', unsafe_allow_html=True,
            )

        divider()
        section_label("Stack")
        st.subheader("Tech Stack")
        stack = [("Python","Data pipeline, feature engineering, clustering"),
                 ("WEKA 3.8.6","SimpleKMeans K=5 clustering (primary method)"),
                 ("PyDeck + Folium","Geospatial visualizations"),
                 ("Plotly","All interactive charts"),
                 ("Streamlit","This dashboard"),
                 ("World Bank API","Economic & digital indicators")]
        for t, d in stack:
            st.markdown(
                f'<div style="display:flex;gap:10px;padding:6px 0;align-items:baseline">'
                f'<code style="background:{PRIMARY_LIGHT};color:{PRIMARY};padding:2px 8px;'
                f'border-radius:5px;font-size:11px;font-weight:700;min-width:80px;'
                f'text-align:center">{t}</code>'
                f'<span style="font-size:0.82rem;color:{TEXT_MUTED};'
                f'font-family:Inter,sans-serif">{d}</span></div>',
                unsafe_allow_html=True,
            )

    with col2:
        section_label("Clusters")
        st.subheader("City Archetypes")
        for c in all_clusters:
            cities = sorted(df_all.loc[df_all["cluster"]==c,"city"].tolist())
            st.markdown(
                f'<div style="background:{CLUSTER_COLORS[c]}22;'
                f'border:1.5px solid {CLUSTER_DARK[c]}44;'
                f'border-radius:12px;padding:12px 16px;margin-bottom:10px">'
                f'<div style="font-weight:700;font-size:0.88rem;color:{TEXT_MAIN};'
                f'font-family:Plus Jakarta Sans,sans-serif;margin-bottom:4px">'
                f'{cluster_names[c]}'
                f'<span style="font-size:11px;font-weight:500;color:{TEXT_MUTED};'
                f'margin-left:8px">{len(cities)} cities</span></div>'
                f'<div style="font-size:11px;color:{TEXT_MUTED};'
                f'font-family:Inter,sans-serif;line-height:1.6">'
                f'{", ".join(cities)}</div></div>',
                unsafe_allow_html=True,
            )

        divider()
        section_label("Author")
        st.subheader("About")
        st.markdown(
            f'<div style="background:{CARD_BG};border:1px solid {BORDER_COL};'
            f'border-radius:14px;padding:20px;box-shadow:{SHADOW}">'
            f'<div style="font-size:1rem;font-weight:800;color:{TEXT_MAIN};'
            f'font-family:Plus Jakarta Sans,sans-serif">Alma Nurul Salma</div>'
            f'<div style="font-size:0.78rem;color:{TEXT_MUTED};margin-top:4px;'
            f'font-family:Inter,sans-serif">'
            f'Informatics — UII & Nanjing Xiaozhuang University</div>'
            f'<div style="margin-top:14px;font-size:0.78rem;color:{TEXT_MUTED};'
            f'font-family:Inter,sans-serif;line-height:2">'
            f'almanurulsalma@gmail.com<br>'
            f'github.com/AlmaNurulSalma-dev</div></div>',
            unsafe_allow_html=True,
        )


# ─── Footer ───────────────────────────────────────────────────────────────────
divider()
st.markdown(
    f'<div style="text-align:center;color:{TEXT_MUTED};font-size:11px;'
    f'font-family:Inter,sans-serif;letter-spacing:0.04em;padding-bottom:8px">'
    f'CITYMETRIC &nbsp;·&nbsp; Measure Your City, Measure Your Future &nbsp;·&nbsp; '
    f'Numbeo · World Bank · Stack Overflow · CWUR · NOAA'
    f'</div>',
    unsafe_allow_html=True,
)
