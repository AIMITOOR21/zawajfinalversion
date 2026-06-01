"""Page 1 — Partner Compatibility Questionnaire."""

import streamlit as st
import json
import numpy as np
from collections import Counter
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
from config import COLORS, DATA_DIR, DOMAIN_OPTIONS, PERSONALITY_TRAITS


def load_scenarios(gender="female"):
    if gender == "male":
        path = DATA_DIR / "boy_scenarios.json"
    else:
        path = DATA_DIR / "scenarios.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_scenario_text(sc):
    return sc.get("scenario", sc.get("text", ""))


def extract_profile_from_responses(responses):
    profile = {}
    domain_values = {}
    for _, choice in responses.items():
        domain = choice.get("domain")
        value = choice.get("value")
        if domain and value:
            domain_values.setdefault(domain, []).append(value)
    for domain, values in domain_values.items():
        profile[domain] = Counter(values).most_common(1)[0][0]
    for domain, options in DOMAIN_OPTIONS.items():
        if domain not in profile:
            profile[domain] = options[1]
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


def main():
    st.set_page_config(page_title="Zawaj — Assessment", page_icon="💑", layout="wide")

    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Poppins:wght@300;400;500;600&display=swap');

    .stApp {
        background: linear-gradient(135deg, #FDEEF2 0%, #FFFFFF 50%, #FDEEF2 100%) !important;
    }
    .block-container { padding-top: 1.5rem !important; max-width: 1100px !important; }

    h1, h2, h3 {
        font-family: 'Playfair Display', serif !important;
        color: #5C2A3E !important;
    }

    /* Fix invisible radio button text */
    div[data-testid="stRadio"] label p {
        color: #2A1018 !important;
        font-family: 'Poppins', sans-serif !important;
        font-size: 0.92rem !important;
    }
    div[data-testid="stRadio"] label {
        color: #2A1018 !important;
        font-family: 'Poppins', sans-serif !important;
        background: white !important;
        border: 1px solid #F0D0DC !important;
        border-radius: 8px !important;
        padding: 0.5rem 0.8rem !important;
        margin-bottom: 0.4rem !important;
        display: block !important;
    }
    div[data-testid="stRadio"] label:hover {
        background: #FFF0F4 !important;
        border-color: #D4577A !important;
    }

    /* Progress bar */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #D4577A, #C9A96E) !important;
    }

    .scenario-box {
        background: white;
        border: 1px solid #F0D0DC;
        border-left: 4px solid #D4577A;
        border-radius: 12px;
        padding: 1.2rem 1.4rem;
        margin-bottom: 1rem;
    }
    .scenario-box-blue {
        background: white;
        border: 1px solid #C9E0F5;
        border-left: 4px solid #1A5C8B;
        border-radius: 12px;
        padding: 1.2rem 1.4rem;
        margin-bottom: 1rem;
    }
    .sc-title {
        font-family: 'Playfair Display', serif;
        font-size: 1rem;
        font-weight: 700;
        color: #D4577A;
        margin-bottom: 0.5rem;
    }
    .sc-title-blue {
        font-family: 'Playfair Display', serif;
        font-size: 1rem;
        font-weight: 700;
        color: #1A5C8B;
        margin-bottom: 0.5rem;
    }
    .sc-text {
        font-family: 'Poppins', sans-serif;
        font-size: 0.92rem;
        color: #3A1A2B;
        line-height: 1.6;
    }
    .done-box {
        background: #6BAF73;
        color: white;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        font-family: 'Playfair Display', serif;
        font-size: 1.1rem;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align:center;'>💑 Partner Compatibility Assessment</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#8B4D6B; font-family:Poppins,sans-serif;'>Scenario-based questions reveal your true values</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        name_a = st.text_input("💐 Girl's name", value="Sara", key="name_a")
    with col2:
        name_b = st.text_input("🌙 Boy's name", value="Ahmed", key="name_b")

    scenarios_a = load_scenarios("female")
    scenarios_b = load_scenarios("male")
    total_a = len(scenarios_a)
    total_b = len(scenarios_b)

    if "responses_a" not in st.session_state:
        st.session_state.responses_a = {}
    if "responses_b" not in st.session_state:
        st.session_state.responses_b = {}

    st.markdown("---")

    # Demo mode
    col_d1, col_d2, col_d3 = st.columns(3)
    with col_d1:
        if st.button(f"⚡ Demo: Fill {name_a}", use_container_width=True):
            for sc in scenarios_a:
                sid = str(sc["id"])
                chosen = dict(sc["choices"][0])
                chosen["domain"] = sc["domain"]
                st.session_state.responses_a[sid] = chosen
            st.rerun()
    with col_d2:
        if st.button(f"⚡ Demo: Fill {name_b}", use_container_width=True):
            for sc in scenarios_b:
                sid = str(sc["id"])
                chosen = dict(sc["choices"][0])
                chosen["domain"] = sc["domain"]
                st.session_state.responses_b[sid] = chosen
            st.rerun()
    with col_d3:
        if st.button("🔄 Reset All", use_container_width=True):
            st.session_state.responses_a = {}
            st.session_state.responses_b = {}
            st.rerun()

    st.markdown("---")

    completed_a = len(st.session_state.responses_a)
    completed_b = len(st.session_state.responses_b)

    col_a, col_b = st.columns(2)

    # SARA
    with col_a:
        st.markdown(f"**💐 {name_a} — Her Scenarios ({completed_a}/{total_a})**")
        st.progress(completed_a / total_a if total_a else 0)

        if completed_a >= total_a:
            st.markdown('<div class="done-box">✨ All done!</div>', unsafe_allow_html=True)
        else:
            for sc in scenarios_a:
                sid = str(sc["id"])
                if sid in st.session_state.responses_a:
                    continue
                title = sc.get("title", sc.get("domain", "").replace("_", " ").title())
                text = get_scenario_text(sc)
                st.markdown(f"""
                <div class="scenario-box">
                    <div class="sc-title">📌 {title}</div>
                    <div class="sc-text">{text}</div>
                </div>
                """, unsafe_allow_html=True)
                opts = [c["text"] for c in sc["choices"]]
                sel = st.radio("Select your answer:", opts, key=f"ra_{sid}", index=None)
                if sel is not None:
                    chosen = dict(next(c for c in sc["choices"] if c["text"] == sel))
                    chosen["domain"] = sc["domain"]
                    st.session_state.responses_a[sid] = chosen
                    st.rerun()
                break

    # AHMED
    with col_b:
        st.markdown(f"**🌙 {name_b} — His Scenarios ({completed_b}/{total_b})**")
        st.progress(completed_b / total_b if total_b else 0)

        if completed_b >= total_b:
            st.markdown('<div class="done-box">✨ All done!</div>', unsafe_allow_html=True)
        else:
            for sc in scenarios_b:
                sid = str(sc["id"])
                if sid in st.session_state.responses_b:
                    continue
                title = sc.get("title", sc.get("domain", "").replace("_", " ").title())
                text = get_scenario_text(sc)
                st.markdown(f"""
                <div class="scenario-box-blue">
                    <div class="sc-title-blue">📌 {title}</div>
                    <div class="sc-text">{text}</div>
                </div>
                """, unsafe_allow_html=True)
                opts = [c["text"] for c in sc["choices"]]
                sel = st.radio("Select your answer:", opts, key=f"rb_{sid}", index=None)
                if sel is not None:
                    chosen = dict(next(c for c in sc["choices"] if c["text"] == sel))
                    chosen["domain"] = sc["domain"]
                    st.session_state.responses_b[sid] = chosen
                    st.rerun()
                break

    # Save profiles
    if completed_a >= total_a and completed_b >= total_b:
        st.markdown("---")
        st.success("🎉 Both partners completed all scenarios!")
        if st.button("💾 Save & Continue to Family Assessment", type="primary"):
            profile_a = extract_profile_from_responses(st.session_state.responses_a)
            profile_b = extract_profile_from_responses(st.session_state.responses_b)
            profile_a["name"] = name_a
            profile_b["name"] = name_b
            st.session_state.profile_a = profile_a
            st.session_state.profile_b = profile_b
            st.session_state.names = {"a": name_a, "b": name_b}
            st.session_state.assessment_complete = True
            st.success("✅ Saved! Go to Family Assessment in the sidebar.")


main()
