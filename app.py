import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from modules.ui_styles import inject_css, made_by_footer
from config import KPI_TARGETS, FISCAL_YEAR

st.set_page_config(page_title="AtliQ Mart SCDI", page_icon="📦", layout="wide", initial_sidebar_state="expanded")
inject_css()

with st.sidebar:
    st.markdown("""<div style="padding:1.2rem 0.5rem 1rem;text-align:center;border-bottom:1px solid #1E293B;margin-bottom:0.8rem;">
<div style="font-size:1.8rem;margin-bottom:0.3rem;">📦</div>
<div style="font-size:0.95rem;font-weight:800;color:#F1F5F9;">AtliQ Mart</div>
<div style="font-size:0.62rem;color:#5EEAD4;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin-top:2px;">SCDI Platform</div>
</div>""", unsafe_allow_html=True)

st.markdown("""
<div style="background:linear-gradient(135deg,#0D1B40,#0A2744);border-radius:24px;padding:3rem 3rem 2.5rem;margin-bottom:2rem;position:relative;overflow:hidden;border:1px solid #1E293B;">
<div style="position:absolute;top:-60px;right:-40px;width:280px;height:280px;background:radial-gradient(circle,rgba(13,148,136,0.25),transparent 65%);border-radius:50%;pointer-events:none;"></div>
<div style="position:absolute;bottom:-80px;left:30%;width:350px;height:350px;background:radial-gradient(circle,rgba(8,145,178,0.15),transparent 65%);border-radius:50%;pointer-events:none;"></div>
<div style="position:absolute;inset:0;opacity:0.03;pointer-events:none;background-image:radial-gradient(circle,#fff 1px,transparent 1px);background-size:28px 28px;"></div>
<div style="position:relative;z-index:2;">
<div style="display:inline-flex;align-items:center;gap:6px;background:rgba(13,148,136,0.18);border:1px solid rgba(13,148,136,0.4);border-radius:100px;padding:5px 14px;font-size:0.7rem;font-weight:700;color:#5EEAD4;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:1.2rem;">
<span style="width:6px;height:6px;background:#5EEAD4;border-radius:50%;display:inline-block;"></span> Live · Real Kaggle Data · FY 2024–25</div>
<h1 style="color:#fff;font-size:3rem;font-weight:900;margin:0 0 0.5rem;letter-spacing:-2px;line-height:1.05;">Supply Chain<br>
<span style="background:linear-gradient(135deg,#5EEAD4,#38BDF8);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">Decision Intelligence</span></h1>
<p style="color:#475569;font-size:0.98rem;max-width:600px;line-height:1.7;margin:0 0 2rem;">
<strong style="color:#94A3B8;">Not a dashboard.</strong> A full decision system on 57,096 real AtliQ Mart order lines —
tracking OT%, IF%, OTIF% daily, forecasting demand, simulating disruptions, and delivering
<strong style="color:#5EEAD4;">prescriptive recommendations with ₹ impact.</strong></p>
<div style="display:flex;gap:10px;flex-wrap:wrap;">
<div style="background:rgba(255,255,255,0.05);border:1px solid #1E293B;border-radius:12px;padding:0.6rem 1.1rem;text-align:center;"><div style="font-size:1.3rem;font-weight:800;color:#F1F5F9;">57K</div><div style="font-size:0.65rem;color:#475569;font-weight:600;letter-spacing:.5px;">ORDER LINES</div></div>
<div style="background:rgba(255,255,255,0.05);border:1px solid #1E293B;border-radius:12px;padding:0.6rem 1.1rem;text-align:center;"><div style="font-size:1.3rem;font-weight:800;color:#F1F5F9;">35</div><div style="font-size:0.65rem;color:#475569;font-weight:600;letter-spacing:.5px;">CUSTOMERS</div></div>
<div style="background:rgba(255,255,255,0.05);border:1px solid #1E293B;border-radius:12px;padding:0.6rem 1.1rem;text-align:center;"><div style="font-size:1.3rem;font-weight:800;color:#F1F5F9;">18</div><div style="font-size:0.65rem;color:#475569;font-weight:600;letter-spacing:.5px;">SKUs</div></div>
<div style="background:rgba(13,148,136,0.15);border:1px solid rgba(13,148,136,0.3);border-radius:12px;padding:0.6rem 1.1rem;text-align:center;"><div style="font-size:1.3rem;font-weight:800;color:#5EEAD4;">₹2.8Cr</div><div style="font-size:0.65rem;color:#5EEAD4;font-weight:600;letter-spacing:.5px;opacity:.8;">REV AT RISK</div></div>
<div style="background:rgba(239,68,68,0.12);border:1px solid rgba(239,68,68,0.3);border-radius:12px;padding:0.6rem 1.1rem;text-align:center;"><div style="font-size:1.3rem;font-weight:800;color:#F87171;">28</div><div style="font-size:0.65rem;color:#F87171;font-weight:600;letter-spacing:.5px;opacity:.8;">DECISIONS</div></div>
</div></div></div>""", unsafe_allow_html=True)

try:
    from modules.data_engine import get_master_data, get_summary_stats
    from modules.financials import fmt_inr
    @st.cache_data
    def load(): return get_master_data()
    df = load()
    stats = get_summary_stats(df)
    c1,c2,c3,c4,c5,c6 = st.columns(6)
    c1.metric("OTIF%",   f"{stats['overall_otif_pct']}%",  delta=f"{stats['overall_otif_pct']-KPI_TARGETS['otif_pct']:+.1f}pp vs target")
    c2.metric("OT%",     f"{stats['overall_ot_pct']}%",    delta=f"{stats['overall_ot_pct']-KPI_TARGETS['ot_pct']:+.1f}pp")
    c3.metric("IF%",     f"{stats['overall_if_pct']}%",    delta=f"{stats['overall_if_pct']-KPI_TARGETS['if_pct']:+.1f}pp")
    c4.metric("At-risk", f"{stats['at_risk_customers']} / 35", delta_color="inverse")
    c5.metric("Revenue", fmt_inr(stats['total_revenue_inr']))
    c6.metric("Stockout loss", fmt_inr(stats['total_stockout_loss']), delta_color="inverse")
except Exception as e:
    st.error(f"Error: {e}")

st.divider()
st.markdown("<h3 style='color:#F1F5F9;font-size:1.2rem;font-weight:800;margin-bottom:1rem;'>Navigate the platform</h3>", unsafe_allow_html=True)
cards = [
    ("📊","Dashboard","Live KPIs · city charts · alerts","#0D1B40","#0A2744"),
    ("🔍","Data Explorer","Filter 57K order lines · export","#1A1040","#251660"),
    ("💡","Insights","Root causes · forecast · cost","#0A2518","#0C3520"),
    ("⚡","Simulator","3 presets · what-if · A vs B","#2D1A0A","#3D2010"),
    ("🎯","Executive","28 recs · decision log · ₹ risk","#1A1212","#241818"),
]
cols = st.columns(5)
for col,(icon,title,desc,c1,c2) in zip(cols,cards):
    with col:
        st.markdown(f"""<div style="background:linear-gradient(145deg,{c1},{c2});border-radius:20px;padding:1.5rem 1.2rem;border:1px solid #1E293B;height:160px;display:flex;flex-direction:column;justify-content:center;">
<div style="font-size:2rem;margin-bottom:0.6rem;">{icon}</div>
<div style="font-weight:800;font-size:0.9rem;color:#F1F5F9;margin-bottom:0.4rem;">{title}</div>
<div style="font-size:0.72rem;color:#475569;line-height:1.5;">{desc}</div>
</div>""", unsafe_allow_html=True)

st.divider()
made_by_footer()
st.caption(f"AtliQ Mart SCDI · Python · Streamlit · Prophet · Plotly · Real Kaggle Dataset")
