"""Page 1 — Partner Compatibility Questionnaire.

Gender-specific scenarios: Girl (Sara) uses scenarios.json (original).
Boy (Ahmed) uses boy_scenarios.json (psychologically complex Option C).
"""

import streamlit as st
import json
import numpy as np
from collections import Counter
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
from config import COLORS, DATA_DIR, DOMAIN_OPTIONS, PERSONALITY_TRAITS


# ---------- Data loading ----------

def load_scenarios(gender="female"):
    """Load gender-appropriate scenarios."""
    if gender == "male":
        path = DATA_DIR / "boy_scenarios.json"
    else:
        path = DATA_DIR / "scenarios.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


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
        profile["openness"] = np.clip(np.mean([v.get("individualism", 0.5) for v in vectors]), 0, 1)
        profile["conscientiousness"] = np.clip(
            np.mean([v.get("tradition", 0.5) for v in vectors]) * 0.7 + 0.15, 0, 1)
        profile["extraversion"] = np.clip(np.random.beta(5, 5), 0, 1)
        profile["agreeableness"] = np.clip(
            1 - np.mean([v.get("confrontation", v.get("individualism", 0.5)) for v in vectors]), 0, 1)
        profile["neuroticism"] = np.clip(np.random.beta(3, 7), 0, 1)
    else:
        for t in PERSONALITY_TRAITS:
            profile[t] = 0.5
    return profile


# ---------- Styling ----------

def page_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;900&family=Poppins:wght@300;400;500;600&display=swap');

    .stApp {
        background: linear-gradient(135deg, #FDEEF2 0%, #FFFFFF 50%, #FDEEF2 100%);
        background-attachment: fixed;
    }
    .block-container { padding-top: 1.5rem; max-width: 1100px; }
    h1,h2,h3,h4 { font-family: 'Playfair Display', serif !important; color: #5C2A3E !important; }
    p,div,span,label,.stMarkdown { font-family: 'Poppins', sans-serif; }

    .page-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.6rem; font-weight: 700; font-style: italic;
        background: linear-gradient(135deg, #5C2A3E, #D4577A);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        background-clip: text; margin: 0; text-align: center;
    }
    .page-subtitle {
        font-family: 'Poppins', sans-serif; font-size: 1rem;
        color: #8B4D6B; text-align: center; margin-top: 0.4rem;
    }
    .gender-badge {
        display: inline-block; padding: 0.25rem 0.9rem;
        border-radius: 20px; font-size: 0.8rem; font-weight: 600;
        font-family: 'Poppins', sans-serif; margin-bottom: 0.5rem;
    }
    .badge-female { background: #F8D7DE; color: #5C2A3E; }
    .badge-male   { background: #D7E8F8; color: #1A3A5C; }

    .scenario-card {
        background: #fff;
        border: 1px solid #F0D0DC;
        border-radius: 14px;
        padding: 1.4rem 1.6rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 12px rgba(212,87,122,0.08);
        animation: fadeInUp 0.5s ease-out;
    }
    .scenario-num {
        font-size: 0.75rem; font-weight: 600; color: #D4577A;
        text-transform: uppercase; letter-spacing: 1px;
    }
    .scenario-q {
        font-family: 'Playfair Display', serif;
        font-size: 1.12rem; color: #3A1A2B;
        margin: 0.4rem 0 1rem;
        font-style: italic; line-height: 1.5;
    }
    .domain-pill {
        display: inline-block;
        background: linear-gradient(135deg, #F8D7DE, #FDEEF2);
        color: #5C2A3E; border-radius: 20px;
        padding: 0.2rem 0.8rem; font-size: 0.72rem;
        font-weight: 600; margin-bottom: 0.6rem;
    }
    .progress-bar-bg {
        background: #F8D7DE; border-radius: 10px;
        height: 8px; margin: 0.6rem 0 0.3rem; overflow: hidden;
    }
    .progress-bar-fill {
        background: linear-gradient(90deg, #D4577A, #C9A96E);
        border-radius: 10px; height: 100%;
        transition: width 0.4s ease;
    }
    .complete-banner {
        background: linear-gradient(135deg, #6BAF73, #4A8A50);
        color: white; border-radius: 12px; padding: 1.2rem 1.5rem;
        text-align: center; font-family: 'Playfair Display', serif;
        font-size: 1.1rem; margin: 1rem 0;
    }
    .stRadio > label { font-family: 'Poppins', sans-serif !important; }

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(16px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    </style>
    """, unsafe_allow_html=True)


def domain_label(d):
    return d.replace("_", " ").title()


# ---------- Main ----------

def main():
    page_css()

    st.markdown('<p class="page-title">💑 Partner Compatibility Assessment</p>', unsafe_allow_html=True)
    st.markdown('<p class="page-subtitle">Scenario-based questions reveal your true values</p>',
                unsafe_allow_html=True)

    # Partner names
    col1, col2 = st.columns(2)
    with col1:
        name_a = st.text_input("💐 Partner 1 (Girl) name", value="Sara", key="name_a")
    with col2:
        name_b = st.text_input("🌙 Partner 2 (Boy) name", value="Ahmed", key="name_b")

    st.markdown("---")

    # Load gender-specific scenarios
    scenarios_a = load_scenarios("female")  # girl
    scenarios_b = load_scenarios("male")    # boy

    total_a = len(scenarios_a)
    total_b = len(scenarios_b)

    # Session state
    if "responses_a" not in st.session_state:
        st.session_state.responses_a = {}
    if "responses_b" not in st.session_state:
        st.session_state.responses_b = {}

    completed_a = len(st.session_state.responses_a)
    completed_b = len(st.session_state.responses_b)

    # Demo mode
    with st.expander("⚡ Demo Mode — auto-fill both partners"):
        st.write("Load demo answers for both partners instantly.")
        col_da, col_db = st.columns(2)
        with col_da:
            if st.button(f"Load {name_a}'s demo answers", key="demo_a"):
                for i, sc in enumerate(scenarios_a):
                    st.session_state.responses_a[sc["id"]] = sc["choices"][0]
                st.rerun()
        with col_db:
            if st.button(f"Load {name_b}'s demo answers", key="demo_b"):
                for i, sc in enumerate(scenarios_b):
                    st.session_state.responses_b[sc["id"]] = sc["choices"][0]
                st.rerun()
        if st.button("🔄 Reset all answers"):
            st.session_state.responses_a = {}
            st.session_state.responses_b = {}
            st.rerun()

    st.markdown("---")

    # Two columns — one per partner
    col_a, col_b = st.columns(2)

    # ---- PARTNER A (GIRL) ----
    with col_a:
        st.markdown(f'<span class="gender-badge badge-female">💐 {name_a} — Her Scenarios</span>',
                    unsafe_allow_html=True)
        pct_a = completed_a / total_a if total_a else 0
        st.markdown(f"""
        <div class='progress-bar-bg'>
            <div class='progress-bar-fill' style='width:{pct_a*100:.0f}%'></div>
        </div>
        <p style="font-size:0.8rem;color:#8B4D6B;font-family:'Poppins',sans-serif;">
            {completed_a} / {total_a} completed
        </p>""", unsafe_allow_html=True)

        if completed_a >= total_a:
            st.markdown('<div class="complete-banner">✨ All scenarios complete!</div>', unsafe_allow_html=True)
        else:
            for sc in scenarios_a:
                if sc["id"] in st.session_state.responses_a:
                    continue
                st.markdown(f"""
                <div class="scenario-card">
                    <div class="scenario-num">Scenario · {domain_label(sc.get('domain',''))}</div>
                    <p class="scenario-q">{sc['text']}</p>
                </div>""", unsafe_allow_html=True)
                choice_labels = [c["text"] for c in sc["choices"]]
                sel = st.radio("Choose:", choice_labels, key=f"a_{sc['id']}", index=None,
                               label_visibility="collapsed")
                if sel:
                    chosen = next(c for c in sc["choices"] if c["text"] == sel)
                    st.session_state.responses_a[sc["id"]] = chosen
                    st.rerun()
                break  # show one at a time

    # ---- PARTNER B (BOY) ----
    with col_b:
        st.markdown(f'<span class="gender-badge badge-male">🌙 {name_b} — His Scenarios</span>',
                    unsafe_allow_html=True)
        pct_b = completed_b / total_b if total_b else 0
        st.markdown(f"""
        <div class='progress-bar-bg'>
            <div class='progress-bar-fill' style='width:{pct_b*100:.0f}%'></div>
        </div>
        <p style="font-size:0.8rem;color:#8B4D6B;font-family:'Poppins',sans-serif;">
            {completed_b} / {total_b} completed
        </p>""", unsafe_allow_html=True)

        if completed_b >= total_b:
            st.markdown('<div class="complete-banner">✨ All scenarios complete!</div>', unsafe_allow_html=True)
        else:
            for sc in scenarios_b:
                if sc["id"] in st.session_state.responses_b:
                    continue
                st.markdown(f"""
                <div class="scenario-card" style="border-color:#C9E0F5;">
                    <div class="scenario-num" style="color:#1A5C8B;">Scenario · {domain_label(sc.get('domain',''))}</div>
                    <p class="scenario-q">{sc['text']}</p>
                </div>""", unsafe_allow_html=True)
                choice_labels = [c["text"] for c in sc["choices"]]
                sel = st.radio("Choose:", choice_labels, key=f"b_{sc['id']}", index=None,
                               label_visibility="collapsed")
                if sel:
                    chosen = next(c for c in sc["choices"] if c["text"] == sel)
                    st.session_state.responses_b[sc["id"]] = chosen
                    st.rerun()
                break

    # ---- Save profiles when both done ----
    if completed_a >= total_a and completed_b >= total_b:
        st.markdown("---")
        st.markdown("### 🎉 Both partners have completed their scenarios!")

        if st.button("📊 Generate Profiles & Proceed to Results", type="primary"):
            profile_a = extract_profile_from_responses(st.session_state.responses_a)
            profile_b = extract_profile_from_responses(st.session_state.responses_b)
            profile_a["name"] = name_a
            profile_b["name"] = name_b
            st.session_state.profile_a = profile_a
            st.session_state.profile_b = profile_b
            st.session_state.names = {"a": name_a, "b": name_b}
            st.success(f"✅ Profiles saved for {name_a} and {name_b}! Go to Page 2 to complete the Family Assessment.")


main()
