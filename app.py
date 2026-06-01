"""Zawaj — Main Streamlit Application."""

import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from config import COLORS, MODELS_DIR


def init_session_state():
    defaults = {
        "person_a": {}, "person_b": {},
        "person_a_name": "", "person_b_name": "",
        "scenario_responses_a": {}, "scenario_responses_b": {},
        "inlaw_responses": {}, "boy_claims": {}, "girl_expectations": {},
        "assessment_complete": False, "inlaws_complete": False,
        "results_computed": False, "results": None, "conflicts": None,
        "domain_scores": None, "inlaw_score": None,
        "triangle_analysis": None, "model_trained": False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


@st.cache_resource
def auto_train_models():
    if not (MODELS_DIR / "compatibility_model.pkl").exists():
        from models.train import train_all
        train_all()
    return True


def main():
    st.set_page_config(
        page_title="Zawaj — Marriage Compatibility",
        page_icon="💖",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Poppins:wght@300;400;500&display=swap');

    .stApp {
        background: linear-gradient(135deg, #FDEEF2 0%, #FFFFFF 50%, #FDEEF2 100%);
        background-attachment: fixed;
    }
    .block-container { padding-top: 2rem; max-width: 900px; }
    h1,h2,h3 { font-family: 'Playfair Display', serif !important; color: #5C2A3E !important; }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #FDEEF2, #fff) !important;
        border-right: 1px solid #F0D0DC !important;
    }
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] div {
        color: #5C2A3E !important;
        font-family: 'Poppins', sans-serif !important;
    }
    </style>
    """, unsafe_allow_html=True)

    init_session_state()

    with st.spinner("Loading models..."):
        auto_train_models()
    st.session_state.model_trained = True

    # ── SIDEBAR ──
    with st.sidebar:
        st.markdown("""
        <div style='text-align:center; padding: 1rem 0;'>
            <div style='font-family:"Playfair Display",serif; font-size:2rem;
                        font-style:italic; font-weight:700; color:#5C2A3E;'>Zawaj</div>
            <div style='font-size:0.8rem; color:#D4577A; letter-spacing:3px;'>زواج</div>
            <hr style='border-color:#F0D0DC; margin:0.8rem 0;'>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 📋 Navigation")
        st.page_link("app.py", label="🏠 Home", icon="🏠")
        st.page_link("pages/1_Scenario_Assessment.py", label="💑 Partner Assessment")
        st.page_link("pages/2_InLaws_Questionnaire.py", label="🏠 Family Assessment")
        st.page_link("pages/3_Results_Dashboard.py", label="📊 Results Dashboard")
        st.page_link("pages/4_Conflict_Simulation.py", label="⚡ Conflict Simulation")
        st.page_link("pages/5_Improvement_Plan.py", label="🌱 Improvement Plan")

        st.markdown("<hr style='border-color:#F0D0DC;'>", unsafe_allow_html=True)
        st.markdown("""
        <div style='font-size:0.72rem; color:#8B4D6B; line-height:1.8;'>
            Aiman Fatima · Sania Saeed · Khadija<br>
            AI-201 · BSSE<br>Dr. Umara Zahid
        </div>
        """, unsafe_allow_html=True)

    # ── HOME PAGE ──
    st.markdown("""
    <div style='text-align:center; padding: 2rem 0 1rem;'>
        <div style='font-family:"Playfair Display",serif; font-size:4rem;
                    font-style:italic; font-weight:700;
                    background: linear-gradient(135deg, #5C2A3E, #D4577A);
                    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                    background-clip: text;'>Zawaj</div>
        <div style='font-size:1.2rem; color:#D4577A; letter-spacing:5px; margin-top:0.3rem;'>زواج</div>
        <p style='color:#8B4D6B; font-family:"Poppins",sans-serif; margin-top:1rem; font-size:1rem;'>
            AI-Powered Pre-Marriage Compatibility for Pakistani Families
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Steps overview
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div style='background:#fff; border:1px solid #F0D0DC; border-radius:14px;
                    padding:1.2rem; text-align:center;'>
            <div style='font-size:2rem;'>💑</div>
            <div style='font-family:"Playfair Display",serif; font-size:1.1rem;
                        color:#5C2A3E; font-weight:600;'>Step 1</div>
            <div style='color:#8B4D6B; font-size:0.85rem; font-family:"Poppins",sans-serif;'>
                Partner Assessment<br>Scenario-based questions
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style='background:#fff; border:1px solid #F0D0DC; border-radius:14px;
                    padding:1.2rem; text-align:center;'>
            <div style='font-size:2rem;'>🏠</div>
            <div style='font-family:"Playfair Display",serif; font-size:1.1rem;
                        color:#5C2A3E; font-weight:600;'>Step 2</div>
            <div style='color:#8B4D6B; font-size:0.85rem; font-family:"Poppins",sans-serif;'>
                Family Assessment<br>Both families profiled
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style='background:#fff; border:1px solid #F0D0DC; border-radius:14px;
                    padding:1.2rem; text-align:center;'>
            <div style='font-size:2rem;'>📊</div>
            <div style='font-family:"Playfair Display",serif; font-size:1.1rem;
                        color:#5C2A3E; font-weight:600;'>Step 3</div>
            <div style='color:#8B4D6B; font-size:0.85rem; font-family:"Poppins",sans-serif;'>
                Results & AI Advice<br>Full compatibility report
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🚀 Start Here")

    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("💑 Begin Partner Assessment", type="primary", use_container_width=True):
            st.switch_page("pages/1_Scenario_Assessment.py")

    with col_b:
        if st.button("🏠 Go to Family Assessment", use_container_width=True):
            st.switch_page("pages/2_InLaws_Questionnaire.py")

    col_c, col_d = st.columns(2)
    with col_c:
        if st.button("📊 View Results Dashboard", use_container_width=True):
            st.switch_page("pages/3_Results_Dashboard.py")
    with col_d:
        if st.button("⚡ Conflict Simulation", use_container_width=True):
            st.switch_page("pages/4_Conflict_Simulation.py")

    st.markdown("---")
    st.markdown("""
    <div style='text-align:center; color:#8B4D6B;
                font-family:"Poppins",sans-serif; font-size:0.8rem;'>
        Built for AI-201 · BSSE · Dr. Umara Zahid<br>
        Aiman Fatima · Sania Saeed · Khadija
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
