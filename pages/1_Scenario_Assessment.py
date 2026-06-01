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


def main():
    st.set_page_config(page_title="Zawaj — Assessment", page_icon="💑", layout="centered")

    st.title("Partner Compatibility Assessment")
    st.caption("Answer scenario-based questions to reveal your true values. One question at a time.")

    name_a = st.text_input("Girl's name", value="Sara")
    name_b = st.text_input("Boy's name", value="Ahmed")

    scenarios_a = load_scenarios("female")
    scenarios_b = load_scenarios("male")

    if "responses_a" not in st.session_state:
        st.session_state.responses_a = {}
    if "responses_b" not in st.session_state:
        st.session_state.responses_b = {}

    # Demo buttons
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button(f"Auto-fill {name_a}", use_container_width=True):
            for sc in scenarios_a:
                sid = str(sc["id"])
                chosen = dict(sc["choices"][0])
                chosen["domain"] = sc["domain"]
                st.session_state.responses_a[sid] = chosen
            st.rerun()
    with c2:
        if st.button(f"Auto-fill {name_b}", use_container_width=True):
            for sc in scenarios_b:
                sid = str(sc["id"])
                chosen = dict(sc["choices"][0])
                chosen["domain"] = sc["domain"]
                st.session_state.responses_b[sid] = chosen
            st.rerun()
    with c3:
        if st.button("Reset All", use_container_width=True):
            st.session_state.responses_a = {}
            st.session_state.responses_b = {}
            st.rerun()

    st.markdown("---")

    done_a = len(st.session_state.responses_a)
    done_b = len(st.session_state.responses_b)
    total = len(scenarios_a)

    # ── SARA TAB / AHMED TAB ──
    tab_a, tab_b = st.tabs([f"Sara — {done_a}/{total} done", f"Ahmed — {done_b}/{total} done"])

    with tab_a:
        st.progress(done_a / total)
        if done_a >= total:
            st.success("All scenarios complete!")
        else:
            for sc in scenarios_a:
                sid = str(sc["id"])
                if sid in st.session_state.responses_a:
                    continue
                title = sc.get("title", sc.get("domain", "").replace("_", " ").title())
                text = get_text(sc)
                st.subheader(title)
                st.info(text)
                opts = [c["text"] for c in sc["choices"]]
                sel = st.radio("Choose one:", opts, key=f"ra_{sid}", index=None)
                if sel is not None:
                    chosen = dict(next(c for c in sc["choices"] if c["text"] == sel))
                    chosen["domain"] = sc["domain"]
                    st.session_state.responses_a[sid] = chosen
                    st.rerun()
                break

    with tab_b:
        st.progress(done_b / total)
        if done_b >= total:
            st.success("All scenarios complete!")
        else:
            for sc in scenarios_b:
                sid = str(sc["id"])
                if sid in st.session_state.responses_b:
                    continue
                title = sc.get("title", sc.get("domain", "").replace("_", " ").title())
                text = get_text(sc)
                st.subheader(title)
                st.info(text)
                opts = [c["text"] for c in sc["choices"]]
                sel = st.radio("Choose one:", opts, key=f"rb_{sid}", index=None)
                if sel is not None:
                    chosen = dict(next(c for c in sc["choices"] if c["text"] == sel))
                    chosen["domain"] = sc["domain"]
                    st.session_state.responses_b[sid] = chosen
                    st.rerun()
                break

    # ── SAVE ──
    if done_a >= total and done_b >= total:
        st.markdown("---")
        st.success("Both partners completed all scenarios!")
        if st.button("Save Profiles and Continue", type="primary"):
            pa = extract_profile(st.session_state.responses_a)
            pb = extract_profile(st.session_state.responses_b)
            pa["name"] = name_a
            pb["name"] = name_b
            st.session_state.profile_a = pa
            st.session_state.profile_b = pb
            st.session_state.names = {"a": name_a, "b": name_b}
            st.session_state.assessment_complete = True
            st.success("Saved! Go to Family Assessment in the sidebar.")


main()
