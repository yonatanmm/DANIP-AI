import streamlit as st
import pandas as pd
from datetime import date, timedelta

st.set_page_config(page_title="Data Governance Intelligence Hub", page_icon="◈", layout="wide", initial_sidebar_state="expanded")

# Demo data is intentionally local and synthetic. Replace these records with your catalog/quality APIs.
quality = pd.DataFrame({
    "Domain": ["Maternal Health", "Immunization", "HIV & TB", "Nutrition", "WASH", "Community Health"],
    "Completeness": [98.2, 96.7, 94.1, 91.8, 89.6, 97.3],
    "Validity": [97.4, 98.1, 92.6, 95.2, 94.8, 96.4],
    "Freshness": [96.0, 89.0, 98.0, 93.0, 84.0, 97.0],
    "Assets": [42, 36, 58, 29, 24, 51],
})
rules = pd.DataFrame([
    {"Rule": "Reporting period is valid", "Domain": "Maternal Health", "Severity": "High", "Pass rate": "99.2%", "Status": "Healthy"},
    {"Rule": "Facility code matches registry", "Domain": "Immunization", "Severity": "High", "Pass rate": "97.8%", "Status": "Healthy"},
    {"Rule": "Required disaggregation present", "Domain": "HIV & TB", "Severity": "Medium", "Pass rate": "91.4%", "Status": "Needs review"},
    {"Rule": "No negative service counts", "Domain": "Nutrition", "Severity": "High", "Pass rate": "98.7%", "Status": "Healthy"},
    {"Rule": "Source updated within 30 days", "Domain": "WASH", "Severity": "Medium", "Pass rate": "84.0%", "Status": "Needs review"},
    {"Rule": "Organization unit is assigned", "Domain": "Community Health", "Severity": "Low", "Pass rate": "99.6%", "Status": "Healthy"},
])

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');
:root { --ink:#17243b; --muted:#71809a; --line:#e8edf4; --blue:#3478f6; --bg:#f6f8fc; }
html, body, [class*="css"] { font-family:'DM Sans',sans-serif; }
.stApp { background:var(--bg); color:var(--ink); }
[data-testid="stHeader"] { background:transparent; }
[data-testid="stSidebar"] { background:#101a2c; border-right:1px solid #1d2b43; }
[data-testid="stSidebar"] * { color:#dbe5f4; }
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p { margin-bottom:.2rem; }
[data-testid="stSidebar"] .block-container { padding-top:1.3rem; }
.brand { font:800 1.05rem/1.3 Manrope,sans-serif; color:#fff; letter-spacing:-.035em; }
.brand-sub { color:#91a5c3; font-size:.73rem; line-height:1.5; margin:.35rem 0 .55rem; }
.brand-by { color:#b5c5dc; font-size:.68rem; font-weight:600; padding-bottom:1.05rem; border-bottom:1px solid #26344a; }
.nav-group { color:#86b4ff; font-size:.63rem; font-weight:800; letter-spacing:.12em; margin:1.05rem 0 .45rem; }
[data-testid="stSidebar"] [data-testid^="st-key-nav_"] button { text-align:left; justify-content:flex-start; background:#172338; color:#dbe5f4; border:1px solid #263650; border-left:3px solid #3478f6; border-radius:10px; padding:.55rem .65rem; min-height:38px; margin-bottom:.35rem; }
[data-testid="stSidebar"] [data-testid^="st-key-nav_"] button:hover { border-color:#4c8cff; background:#1c2b44; color:#fff; }
[data-testid="stSidebar"] [data-testid^="st-key-nav_"] button[kind="primary"] { background:#1c3153; border-color:#3478f6; color:#fff; }
[data-testid="stSidebar"] [data-testid^="st-key-nav_"] button p { font-size:.78rem; font-weight:600; }
.eyebrow { text-transform:uppercase; letter-spacing:.12em; color:#497fe0; font-size:.65rem; font-weight:800; }
h1,h2,h3 { font-family:Manrope,sans-serif!important; letter-spacing:-.035em!important; color:#17243b!important; }
.page-title { font:800 1.8rem Manrope,sans-serif; letter-spacing:-.045em; color:#17243b; margin:.15rem 0 .2rem; }
.page-subtitle { color:#71809a; font-size:.88rem; margin-bottom:1.1rem; }
.metric { background:white; border:1px solid var(--line); border-radius:14px; padding:17px 18px; min-height:126px; box-shadow:0 2px 10px #19335a08; }
.metric-label { color:#71809a; font-size:.73rem; font-weight:600; }
.metric-value { color:#17243b; font:800 1.65rem Manrope,sans-serif; margin:.35rem 0 .25rem; letter-spacing:-.04em; }
.metric-note { color:#25956d; font-size:.69rem; font-weight:600; }
.panel { background:#fff; border:1px solid var(--line); border-radius:14px; padding:18px 20px; box-shadow:0 2px 10px #19335a08; }
.panel-title { color:#17243b; font:700 .93rem Manrope,sans-serif; }
.panel-note { color:#8390a5; font-size:.7rem; margin-top:.18rem; }
.stDataFrame { border:1px solid var(--line); border-radius:10px; overflow:hidden; }
section.main > div { padding-top:1.7rem; }
@media(max-width:760px){ .page-title{font-size:1.45rem}.metric{min-height:105px;padding:13px}.metric-value{font-size:1.35rem} }
</style>
""", unsafe_allow_html=True)

NAV = {
    "OVERVIEW": ["RPT Executive Dashboard", "RPT Application Usage Analytics", "AI Activity Analytics"],
    "DATA DISCOVERY": ["RPT Metadata Report"],
    "DATA QUALITY": ["RPT Data Quality Detail Report", "RPT Validation Rule Performance", "RPT Source & Table Health", "RPT Data Profiling Activity"],
    "PLATFORM": ["OPS About / Platform Info"],
}
def select_page(page):
    st.session_state.active_page = page

with st.sidebar:
    st.markdown('<div class="brand">Data Governance<br>Intelligence Hub</div><div class="brand-sub">AI-Powered Data Quality, Metadata &amp; Governance</div><div class="brand-by">Developed by Fitsum Yimam</div>', unsafe_allow_html=True)
    for group, pages in NAV.items():
        st.markdown(f'<div class="nav-group">{group}</div>', unsafe_allow_html=True)
        with st.container(key=f"nav_{group.lower().replace(' ', '_')}"):
            for index, item in enumerate(pages):
                st.button(item, key=f"page_{group}_{index}", use_container_width=True,
                          type="primary" if st.session_state.get("active_page", "RPT Executive Dashboard") == item else "secondary",
                          on_click=select_page, args=(item,))
    st.markdown('<div style="height:12px"></div>', unsafe_allow_html=True)
    st.caption("●  Connected to demo workspace")
    st.caption("Last catalog sync · 18 min ago")

page = st.session_state.get("active_page", "RPT Executive Dashboard")

st.markdown('<div class="eyebrow">Data Governance Intelligence Hub</div>', unsafe_allow_html=True)
st.markdown(f'<div class="page-title">{page.replace("RPT ", "").replace("OPS ", "")}</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">A clear view of your data estate, quality signals, and governance activity.</div>', unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)
metrics = [("CATALOGED ASSETS", "1,284", "↑ 8.4% this quarter"), ("QUALITY SCORE", "94.6%", "↑ 2.1 pts this month"), ("ACTIVE DATA SOURCES", "36", "Across 8 domains"), ("OPEN ISSUES", "23", "6 high priority")]
for col,(label,value,note) in zip((c1,c2,c3,c4),metrics):
    col.markdown(f'<div class="metric"><div class="metric-label">{label}</div><div class="metric-value">{value}</div><div class="metric-note">{note}</div></div>',unsafe_allow_html=True)

st.write("")
left,right = st.columns([1.55,1], gap="large")
with left:
    st.markdown('<div class="panel-title">Data quality by domain</div><div class="panel-note">Completeness, validity, and freshness scores · latest reporting period</div>',unsafe_allow_html=True)
    chart = quality.set_index("Domain")[["Completeness","Validity","Freshness"]]
    st.bar_chart(chart, color=["#3478f6", "#31b58b", "#a979f5"], height=285)
with right:
    st.markdown('<div class="panel-title">Governance at a glance</div><div class="panel-note">Current review queue and catalog health</div>',unsafe_allow_html=True)
    st.write("")
    st.markdown("**23** open quality issues  ·  **6** high priority")
    st.progress(.76, text="76% of assets have an assigned owner")
    st.progress(.89, text="89% of sources refreshed on schedule")
    st.progress(.68, text="68% of sensitive assets classified")
    st.info("**Needs attention** · WASH source freshness is below the 90% target.", icon="⚑")

st.write("")
tab1,tab2,tab3 = st.tabs(["Quality by domain", "Validation rules", "Recent activity"])
with tab1:
    st.dataframe(quality.style.format({"Completeness":"{:.1f}%","Validity":"{:.1f}%","Freshness":"{:.1f}%"}), use_container_width=True, hide_index=True)
with tab2:
    st.dataframe(rules, use_container_width=True, hide_index=True)
with tab3:
    st.dataframe(pd.DataFrame([
        {"Event":"Metadata scan completed", "Asset":"DHIS2 monthly aggregate", "Owner":"Data Platform", "When":"18 min ago", "Result":"42 assets updated"},
        {"Event":"Quality rule flagged", "Asset":"WASH facility report", "Owner":"Governance team", "When":"1 hour ago", "Result":"Freshness below target"},
        {"Event":"Classification approved", "Asset":"Maternal health dataset", "Owner":"A. Bekele", "When":"3 hours ago", "Result":"Sensitive · restricted"},
        {"Event":"New source registered", "Asset":"Community health API", "Owner":"Data Platform", "When":"Yesterday", "Result":"Pending owner review"},
    ]), use_container_width=True, hide_index=True)

st.caption("Demo workspace · Synthetic data for preview. Connect your catalog, warehouse, and quality-rule sources to make this hub operational.")
