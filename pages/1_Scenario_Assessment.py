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


def page_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Poppins:wght@300;400;500;600&display=swap');
    .stApp {
        background: linear-gradient(135deg, #FDEEF2 0%, #FFFFFF 50%, #FDEEF2 100%);
    }
    .block-container { padding-top: 1.5rem; max-width: 1100px; }
    h1,h2,h3,h4 { font-family: 'Playfair Display', serif !important; color: #5C2A3E !important; }

    .scenario-card {
        background: white;
        border: 1px solid #F0D0DC;
        border-radius: 14px;
        padding: 1.4rem 1.6rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 12px rgba(212,87,122,0.08);
    }
    .scenario-title {
        font-family: 'Playfair Display', serif;
        font-size: 1rem;
        font-weight: 700;
        color: #D4577A;
        margin-bottom: 0.5rem;
    }
    .scenario-text {
        font-family: 'Poppins', sans-serif;
        font-size: 0.95rem;
        color: #3A1A2B;
        line-height: 1.6;
        margin-bottom: 0.8rem;
    }
    .gender-badge {
        display: inline-block;
        padding: 0.3rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        font-family: 'Poppins', sans-serif;
        margin-bottom: 0.8rem;
    }
    .badge-female { background: #F8D7DE; color: #5C2A3E; }
    .badge-male   { background: #D7E8F8; color: #1A3A5C; }

    .complete-box {
        background: linear-gradient(135deg, #6BAF73, #4A8A50);
        color: white;
        border-radius: 12px;
        padding: 1rem 1.5rem;
        text-align: center;
        font-family: 'Playfair Display', serif;
        font-size: 1.1rem;
        margin: 1rem 0;
    }
    div[data-testid="stRadio"] label {
        font-family: 'Poppins', sans-serif !important;
        font-size: 0.9rem !important;
        color: #3A1A2B !important;
    }
    </style>
    """, unsafe_allow_html=True)


def main():
    st.set_page_config(page_title="Zawaj — Assessment", page_icon="💑", layout="wide")
    page_css()

    st.markdown("<h1 style='text-align:center;'>💑 Partner Compatibility Assessment</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;color:#8B4D6B;font-family:Poppins,sans-serif;'>Scenario-based questions reveal your true values</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        name_a = st.text_input("💐 Partner 1 (Girl) name", value="Sara", key="name_a")
    with col2:
        name_b = st.text_input("🌙 Partner 2 (Boy) name", value="Ahmed", key="name_b")

    # Load scenarios
    scenarios_a = load_scenarios("female")
    scenarios_b = load_scenarios("male")

    total_a = len(scenarios_a)
    total_b = len(scenarios_b)

    if "responses_a" not in st.session_state:
        st.session_state.responses_a = {}
    if "responses_b" not in st.session_state:
        st.session_state.responses_b = {}

    # Demo mode
    st.markdown("---")
    with st.expander("⚡ Demo Mode — auto-fill both partners instantly"):
        col_d1, col_d2, col_d3 = st.columns(3)
        with col_d1:
            if st.button(f"Load {name_a}'s demo answers"):
                for sc in scenarios_a:
                    sid = str(sc["id"])
                    chosen = sc["choices"][0]
                    chosen["domain"] = sc["domain"]
                    st.session_state.responses_a[sid] = chosen
                st.rerun()
        with col_d2:
            if st.button(f"Load {name_b}'s demo answers"):
                for sc in scenarios_b:
                    sid = str(sc["id"])
                    chosen = sc["choices"][0]
                    chosen["domain"] = sc["domain"]
                    st.session_state.responses_b[sid] = chosen
                st.rerun()
        with col_d3:
            if st.button("🔄 Reset all"):
                st.session_state.responses_a = {}
                st.session_state.responses_b = {}
                st.rerun()

    st.markdown("---")

    completed_a = len(st.session_state.responses_a)
    completed_b = len(st.session_state.responses_b)

    col_a, col_b = st.columns(2)

    # ── SARA'S SCENARIOS ──
    with col_a:
        st.markdown(f'<div class="gender-badge badge-female">💐 {name_a} — Her Scenarios ({completed_a}/{total_a})</div>', unsafe_allow_html=True)
        st.progress(completed_a / total_a if total_a else 0)

        if completed_a >= total_a:
            st.markdown('<div class="complete-box">✨ All scenarios complete!</div>', unsafe_allow_html=True)
        else:
            for sc in scenarios_a:
                sid = str(sc["id"])
                if sid in st.session_state.responses_a:
                    continue
                # Show this scenario
                title = sc.get("title", sc.get("domain", "").replace("_", " ").title())
                text = get_scenario_text(sc)
                st.markdown(f"""
                <div class="scenario-card">
                    <div class="scenario-title">📌 {title}</div>
                    <div class="scenario-text">{text}</div>
                </div>
                """, unsafe_allow_html=True)
                choice_labels = [c["text"] for c in sc["choices"]]
                sel = st.radio("Choose:", choice_labels, key=f"a_{sid}", index=None, label_visibility="collapsed")
                if sel is not None:
                    chosen = next(c for c in sc["choices"] if c["text"] == sel)
                    chosen["domain"] = sc["domain"]
                    st.session_state.responses_a[sid] = chosen
                    st.rerun()
                break

    # ── AHMED'S SCENARIOS ──
    with col_b:
        st.markdown(f'<div class="gender-badge badge-male">🌙 {name_b} — His Scenarios ({completed_b}/{total_b})</div>', unsafe_allow_html=True)
        st.progress(completed_b / total_b if total_b else 0)

        if completed_b >= total_b:
            st.markdown('<div class="complete-box">✨ All scenarios complete!</div>', unsafe_allow_html=True)
        else:
            for sc in scenarios_b:
                sid = str(sc["id"])
                if sid in st.session_state.responses_b:
                    continue
                title = sc.get("title", sc.get("domain", "").replace("_", " ").title())
                text = get_scenario_text(sc)
                st.markdown(f"""
                <div class="scenario-card" style="border-color:#C9E0F5;">
                    <div class="scenario-title" style="color:#1A5C8B;">📌 {title}</div>
                    <div class="scenario-text">{text}</div>
                </div>
                """, unsafe_allow_html=True)
                choice_labels = [c["text"] for c in sc["choices"]]
                sel = st.radio("Choose:", choice_labels, key=f"b_{sid}", index=None, label_visibility="collapsed")
                if sel is not None:
                    chosen = next(c for c in sc["choices"] if c["text"] == sel)
                    chosen["domain"] = sc["domain"]
                    st.session_state.responses_b[sid] = chosen
                    st.rerun()
                break

    # ── SAVE PROFILES ──
    if completed_a >= total_a and completed_b >= total_b:
        st.markdown("---")
        st.success("🎉 Both partners have completed all scenarios!")
        if st.button("📊 Save Profiles & Continue", type="primary"):
            profile_a = extract_profile_from_responses(st.session_state.responses_a)
            profile_b = extract_profile_from_responses(st.session_state.responses_b)
            profile_a["name"] = name_a
            profile_b["name"] = name_b
            st.session_state.profile_a = profile_a
            st.session_state.profile_b = profile_b
            st.session_state.names = {"a": name_a, "b": name_b}
            st.session_state.assessment_complete = True
            st.success(f"✅ Profiles saved! Go to Family Assessment in the sidebar.")


main()
