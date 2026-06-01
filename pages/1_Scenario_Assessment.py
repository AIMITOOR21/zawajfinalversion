"""Page 1 — Partner Compatibility Questionnaire."""

import streamlit as st
import json
import numpy as np
from collections import Counter
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
from config import DATA_DIR, DOMAIN_OPTIONS, PERSONALITY_TRAITS


def load_scenarios(gender="female"):
    path = DATA_DIR / ("boy_scenarios.json" if gender == "male" else "scenarios.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_text(sc):
    return sc.get("scenario", sc.get("text", ""))


def extract_profile(responses):
    profile = {}
    domain_values = {}
    for _, choice in responses.items():
        d = choice.get("domain")
        v = choice.get("value")
        if d and v:
            domain_values.setdefault(d, []).append(v)
    for d, vals in domain_values.items():
        profile[d] = Counter(vals).most_common(1)[0][0]
    for d, opts in DOMAIN_OPTIONS.items():
        if d not in profile:
            profile[d] = opts[1]
    vectors = [c.get("vector", {}) for c in responses.values()]
    if vectors:
        profile["openness"] = float(np.clip(np.mean([v.get("individualism", 0.5) for v in vectors]), 0, 1))
        profile["conscientiousness"] = float(np.clip(np.mean([v.get("tradition", 0.5) for v in vectors]) * 0.7 + 0.15, 0, 1))
        profile["extraversion"] = float(np.clip(np.random.beta(5, 5), 0, 1))
        profile["agreeableness"] = float(np.clip(1 - np.mean([v.get("individualism", 0.5) for v in vectors]), 0, 1))
        profile["neuroticism"] = float(np.clip(np.random.beta(3, 7), 0, 1))
    else:
        for t in PERSONALITY_TRAITS:
            profile[t] = 0.5
    return profile


def page_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;900&family=Poppins:wght@300;400;500;600&display=swap');

    .stApp {
        background: linear-gradient(135deg, #FDEEF2 0%, #FFFFFF 50%, #FDEEF2 100%);
        background-attachment: fixed;
    }
    .block-container { padding-top: 1.5rem; max-width: 1150px; }
    h1,h2,h3,h4 { font-family: 'Playfair Display', serif !important; color: #5C2A3E !important; }
    p, div, span, label, .stMarkdown { font-family: 'Poppins', sans-serif; }

    .page-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.8rem; font-weight: 700; font-style: italic;
        background: linear-gradient(135deg, #5C2A3E, #D4577A);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        background-clip: text; text-align: center; margin: 0;
    }
    .page-sub {
        color: #8A6B7A; font-style: italic;
        font-size: 1rem; text-align: center; margin-top: 0.3rem;
    }
    .divider-gold {
        width: 120px; height: 2px;
        background: linear-gradient(90deg, transparent, #C9A96E, transparent);
        margin: 1rem auto;
    }

    .scenario-card {
        background: white;
        border-radius: 16px;
        padding: 1.5rem 1.8rem;
        box-shadow: 0 4px 18px rgba(212,87,122,0.1);
        margin-bottom: 1.2rem;
        border-left: 4px solid #D4577A;
        animation: fadeInUp 0.5s ease-out;
    }
    .scenario-card-blue {
        background: white;
        border-radius: 16px;
        padding: 1.5rem 1.8rem;
        box-shadow: 0 4px 18px rgba(26,92,139,0.1);
        margin-bottom: 1.2rem;
        border-left: 4px solid #1A5C8B;
        animation: fadeInUp 0.5s ease-out;
    }
    .scenario-domain {
        font-size: 0.7rem; font-weight: 600; letter-spacing: 2px;
        text-transform: uppercase; color: #D4577A; margin-bottom: 0.4rem;
    }
    .scenario-domain-blue {
        font-size: 0.7rem; font-weight: 600; letter-spacing: 2px;
        text-transform: uppercase; color: #1A5C8B; margin-bottom: 0.4rem;
    }
    .scenario-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.1rem; font-weight: 700;
        color: #3A1A2B; margin-bottom: 0.6rem;
    }
    .scenario-text {
        font-family: 'Poppins', sans-serif;
        font-size: 0.92rem; color: #5A3A4A;
        line-height: 1.65;
    }

    .partner-header {
        background: white;
        border-radius: 14px;
        padding: 1rem 1.4rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 10px rgba(212,87,122,0.08);
        display: flex; align-items: center; gap: 10px;
    }
    .partner-name {
        font-family: 'Playfair Display', serif;
        font-size: 1.3rem; font-weight: 700; color: #5C2A3E;
    }
    .progress-text {
        font-size: 0.8rem; color: #8A6B7A; margin-top: 0.2rem;
    }

    .complete-card {
        background: linear-gradient(135deg, #6BAF73, #4A8A52);
        border-radius: 14px; padding: 1.2rem;
        text-align: center; color: white;
        font-family: 'Playfair Display', serif;
        font-size: 1.1rem; font-weight: 600;
        box-shadow: 0 4px 16px rgba(107,175,115,0.3);
    }

    /* Hide black radio dot */
    /* Hide radio dot */
    div[data-testid="stRadio"] > div > label > div:first-child {
        display: none !important;
    }
    div[data-testid="stRadio"] > div {
        gap: 0.5rem !important;
        display: flex !important;
        flex-direction: column !important;
    }
    div[data-testid="stRadio"] > div > label {
        background: white !important;
        border: 1.5px solid #F0D0DC !important;
        border-radius: 12px !important;
        padding: 0.8rem 1.2rem !important;
        cursor: pointer !important;
        transition: all 0.2s ease !important;
        margin: 0 !important;
        width: 100% !important;
    }
    div[data-testid="stRadio"] > div > label:hover {
        background: #FFF0F4 !important;
        border-color: #D4577A !important;
    }
    /* Force ALL text inside radio labels to be visible - covers all Streamlit versions */
    div[data-testid="stRadio"] > div > label *,
    div[data-testid="stRadio"] > div > label p,
    div[data-testid="stRadio"] > div > label span,
    div[data-testid="stRadio"] > div > label div {
        color: #3A1A2B !important;
        font-family: 'Poppins', sans-serif !important;
        font-size: 0.9rem !important;
        line-height: 1.5 !important;
    }

    .stTabs [data-baseweb="tab"] {
        background: white; border-radius: 10px 10px 0 0;
        padding: 0.55rem 1.3rem; color: #8A6B7A;
        border: 1px solid #F8D7DE; border-bottom: none;
        font-family: 'Poppins', sans-serif; font-weight: 500;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #5C2A3E, #D4577A) !important;
        color: white !important;
    }
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #D4577A, #C9A96E) !important;
    }
    .stButton > button {
        background: linear-gradient(135deg, #5C2A3E, #D4577A) !important;
        color: white !important; border: none !important;
        border-radius: 50px !important;
        font-family: 'Poppins', sans-serif !important;
        font-weight: 500 !important;
        padding: 0.6rem 2rem !important;
        box-shadow: 0 4px 14px rgba(212,87,122,0.3) !important;
    }

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(16px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-16px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    </style>
    """, unsafe_allow_html=True)


def main():
    st.set_page_config(page_title="Zawaj — Assessment", page_icon="💑", layout="wide")
    page_css()

    st.markdown('<p class="page-title">💑 Partner Compatibility Assessment</p>', unsafe_allow_html=True)
    st.markdown('<p class="page-sub">Scenario-based questions that reveal true values — not just stated ones</p>', unsafe_allow_html=True)
    st.markdown('<div class="divider-gold"></div>', unsafe_allow_html=True)

    # Initialize name defaults in session state ONCE
    if "name_a" not in st.session_state:
        st.session_state["name_a"] = st.session_state.get("person_a_name", "Sara")
    if "name_b" not in st.session_state:
        st.session_state["name_b"] = st.session_state.get("person_b_name", "Ahmed")

    col1, col2 = st.columns(2)
    with col1:
        name_a = st.text_input("💐 Girl's name", key="name_a")
        st.session_state.person_a_name = name_a
        st.session_state.setdefault("names", {})["a"] = name_a
    with col2:
        name_b = st.text_input("🌙 Boy's name", key="name_b")
        st.session_state.person_b_name = name_b
        st.session_state.setdefault("names", {})["b"] = name_b

    scenarios_a = load_scenarios("female")
    scenarios_b = load_scenarios("male")
    total = len(scenarios_a)

    if "responses_a" not in st.session_state:
        st.session_state.responses_a = {}
    if "responses_b" not in st.session_state:
        st.session_state.responses_b = {}

    # Demo buttons
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button(f"⚡ Auto-fill {name_a}", key="autofill_a", use_container_width=True):
            for sc in scenarios_a:
                sid = str(sc["id"])
                chosen = dict(sc["choices"][0])
                chosen["domain"] = sc["domain"]
                st.session_state.responses_a[sid] = chosen
            st.rerun()
    with c2:
        if st.button(f"⚡ Auto-fill {name_b}", key="autofill_b", use_container_width=True):
            for sc in scenarios_b:
                sid = str(sc["id"])
                chosen = dict(sc["choices"][0])
                chosen["domain"] = sc["domain"]
                st.session_state.responses_b[sid] = chosen
            st.rerun()
    with c3:
        if st.button("🔄 Reset All", key="reset_all_p1", use_container_width=True):
            st.session_state.responses_a = {}
            st.session_state.responses_b = {}
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    done_a = len(st.session_state.responses_a)
    done_b = len(st.session_state.responses_b)

    tab_a, tab_b = st.tabs([
        f"💐 {name_a} — {done_a}/{total} completed",
        f"🌙 {name_b} — {done_b}/{total} completed"
    ])

    # ── SARA ──
    with tab_a:
        st.progress(done_a / total if total else 0)
        if done_a >= total:
            st.markdown('<div class="complete-card">✨ All scenarios complete!</div>', unsafe_allow_html=True)
        else:
            for sc in scenarios_a:
                sid = str(sc["id"])
                if sid in st.session_state.responses_a:
                    continue
                title = sc.get("title", sc.get("domain", "").replace("_", " ").title())
                text = get_text(sc)
                domain = sc.get("domain", "").replace("_", " ").upper()
                st.markdown(f"""
                <div class="scenario-card">
                    <div class="scenario-domain">{domain}</div>
                    <div class="scenario-title">{title}</div>
                    <div class="scenario-text">{text}</div>
                </div>
                """, unsafe_allow_html=True)
                opts = [c["text"] for c in sc["choices"]]
                sel = st.radio("Choose your answer:", opts, key=f"ra_{sid}", index=None)
                if sel is not None:
                    chosen = dict(next(c for c in sc["choices"] if c["text"] == sel))
                    chosen["domain"] = sc["domain"]
                    st.session_state.responses_a[sid] = chosen
                    st.rerun()
                break

    # ── AHMED ──
    with tab_b:
        st.progress(done_b / total if total else 0)
        if done_b >= total:
            st.markdown('<div class="complete-card">✨ All scenarios complete!</div>', unsafe_allow_html=True)
        else:
            for sc in scenarios_b:
                sid = str(sc["id"])
                if sid in st.session_state.responses_b:
                    continue
                title = sc.get("title", sc.get("domain", "").replace("_", " ").title())
                text = get_text(sc)
                domain = sc.get("domain", "").replace("_", " ").upper()
                st.markdown(f"""
                <div class="scenario-card-blue">
                    <div class="scenario-domain-blue">{domain}</div>
                    <div class="scenario-title">{title}</div>
                    <div class="scenario-text">{text}</div>
                </div>
                """, unsafe_allow_html=True)
                opts = [c["text"] for c in sc["choices"]]
                sel = st.radio("Choose your answer:", opts, key=f"rb_{sid}", index=None)
                if sel is not None:
                    chosen = dict(next(c for c in sc["choices"] if c["text"] == sel))
                    chosen["domain"] = sc["domain"]
                    st.session_state.responses_b[sid] = chosen
                    st.rerun()
                break

    # ── SAVE ──
    if done_a >= total and done_b >= total:
        st.markdown('<div class="divider-gold"></div>', unsafe_allow_html=True)
        st.success("🎉 Both partners completed all scenarios!")
        if st.button("💾 Save Profiles & Continue to Family Assessment", key="save_profiles", type="primary"):
            pa = extract_profile(st.session_state.responses_a)
            pb = extract_profile(st.session_state.responses_b)
            pa["name"] = name_a
            pb["name"] = name_b
            st.session_state.profile_a = pa
            st.session_state.profile_b = pb
            st.session_state.names = {"a": name_a, "b": name_b}
            st.session_state.person_a_name = name_a
            st.session_state.person_b_name = name_b
            st.session_state.person_a = pa
            st.session_state.person_b = pb
            st.session_state.assessment_complete = True
            st.success(f"✅ Profiles saved for {name_a} and {name_b}! Navigate to In-Laws Questionnaire.")


main()
