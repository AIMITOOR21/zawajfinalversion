"""Page 2 — In-Laws Questionnaire. Styled to match zawaj5 original look."""

import streamlit as st
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

INLAW_SCENARIOS = {
    "sara_mother": {
        "label": "Sara's Mother", "emoji": "👩",
        "side": "Sara's Family",
        "scenarios": [
            {"id": "sm_1", "topic": "DESCRIBING HER IDEAL SON-IN-LAW",
             "question": "When you imagine the kind of man you'd want for your daughter, what comes to mind first?",
             "choices": [
                 {"text": "Someone she chooses for herself, that she can build a life with.", "score": 1.0},
                 {"text": "A man from a good, respectable family — with steady prospects.", "score": 0.45},
                 {"text": "Someone who would treat her well and adjust to our family's rhythm.", "score": 0.4},
                 {"text": "A man with character. Money and background are secondary.", "score": 0.7}]},
            {"id": "sm_2", "topic": "MOST IMPORTANT QUALITY",
             "question": "If you had to name the single most important quality in a son-in-law, what would it be?",
             "choices": [
                 {"text": "That my daughter feels respected by him.", "score": 1.0},
                 {"text": "That he comes from people we know and trust.", "score": 0.35},
                 {"text": "That he listens — to her, to us, to wisdom.", "score": 0.5},
                 {"text": "That he can stand on his own — emotionally, financially, socially.", "score": 0.7}]},
            {"id": "sm_3", "topic": "RELATIONSHIP WITH SON-IN-LAW",
             "question": "What kind of relationship would you ideally have with your daughter's husband?",
             "choices": [
                 {"text": "Close, like a son — someone we'd both lean on and support.", "score": 0.9},
                 {"text": "Respectful — we don't need to be close, just kind.", "score": 0.65},
                 {"text": "I'd want him to come to us when things get difficult.", "score": 0.4},
                 {"text": "Whatever feels natural. Some sons-in-law are close, some aren't.", "score": 0.5}]},
            {"id": "sm_4", "topic": "WHAT WOULD MAKE HER HESITATE",
             "question": "What would make you most uncomfortable about a potential son-in-law?",
             "choices": [
                 {"text": "If my daughter seemed unsure about him, even slightly.", "score": 1.0},
                 {"text": "If his family had a reputation or background we weren't sure of.", "score": 0.35},
                 {"text": "If he seemed the kind to dominate or shut her down.", "score": 0.8},
                 {"text": "If he was too independent — too much his own person.", "score": 0.2}]},
            {"id": "sm_5", "topic": "QUIET HOPE FOR THE MARRIAGE",
             "question": "What's the quiet hope you carry about your daughter's eventual marriage?",
             "choices": [
                 {"text": "That she stays herself — that marriage adds to her, doesn't shrink her.", "score": 1.0},
                 {"text": "That she's well-settled and never has to worry about anything.", "score": 0.55},
                 {"text": "That she doesn't drift too far from us.", "score": 0.4},
                 {"text": "That her husband becomes part of our family, fully.", "score": 0.5}]}]},

    "sara_father": {
        "label": "Sara's Father", "emoji": "👨",
        "side": "Sara's Family",
        "scenarios": [
            {"id": "sf_1", "topic": "SON-IN-LAW'S ROLE",
             "question": "What's the most important thing for a son-in-law to be for your daughter?",
             "choices": [
                 {"text": "A partner — someone who walks beside her, not ahead of her.", "score": 1.0},
                 {"text": "A protector — financially, socially, in every way.", "score": 0.5},
                 {"text": "A steady presence — someone who keeps her grounded.", "score": 0.45},
                 {"text": "Someone who genuinely values what she brings to the marriage.", "score": 0.8}]},
            {"id": "sf_2", "topic": "HANDLING DISAGREEMENTS",
             "question": "How should a son-in-law handle a disagreement with your daughter?",
             "choices": [
                 {"text": "Talk to her directly until they understand each other.", "score": 1.0},
                 {"text": "Know when to walk away and revisit later.", "score": 0.55},
                 {"text": "Be the calmer one — someone has to be.", "score": 0.5},
                 {"text": "Bring it to the family if they can't resolve it.", "score": 0.2}]},
            {"id": "sf_3", "topic": "FINANCIAL EXPECTATIONS",
             "question": "What do you expect from a son-in-law financially?",
             "choices": [
                 {"text": "That he and my daughter handle finances together as they see fit.", "score": 1.0},
                 {"text": "That he's stable and able to provide for the household.", "score": 0.6},
                 {"text": "That he's transparent — no surprises.", "score": 0.65},
                 {"text": "That my daughter never has to worry about money.", "score": 0.5}]},
            {"id": "sf_4", "topic": "AUTHORITY DYNAMIC",
             "question": "Do you see a son-in-law as someone who should defer to elders, or have his own standing?",
             "choices": [
                 {"text": "His own standing. He's not our subordinate.", "score": 1.0},
                 {"text": "Both — respect for elders, but his decisions are his.", "score": 0.7},
                 {"text": "He should listen — that's how a young man matures.", "score": 0.3},
                 {"text": "It depends on his family's culture. We'd adapt.", "score": 0.55}]},
            {"id": "sf_5", "topic": "PRIVATE WORRY",
             "question": "What's your private worry about your daughter's future husband?",
             "choices": [
                 {"text": "That he won't show up for her when she's struggling.", "score": 1.0},
                 {"text": "That his family will pull him away from her.", "score": 0.4},
                 {"text": "That she'll soften too much for him — lose her edge.", "score": 0.5},
                 {"text": "I don't worry. She's strong enough to choose well.", "score": 0.7}]}]},

    "ahmed_mother": {
        "label": "Ahmed's Mother", "emoji": "👩",
        "side": "Ahmed's Family",
        "scenarios": [
            {"id": "am_1", "topic": "DAUGHTER-IN-LAW'S PLACE",
             "question": "How do you see a daughter-in-law in your home?",
             "choices": [
                 {"text": "As my son's wife — her home is the one she builds with him.", "score": 1.0},
                 {"text": "As a daughter — fully part of the family from day one.", "score": 0.75},
                 {"text": "As family, with time. Trust is built.", "score": 0.5},
                 {"text": "Someone who'll bring her own ways — and we'll find a rhythm.", "score": 0.85}]},
            {"id": "am_2", "topic": "HER CAREER",
             "question": "What's your view on a daughter-in-law continuing her career after marriage?",
             "choices": [
                 {"text": "Her decision entirely.", "score": 1.0},
                 {"text": "Of course — we're a modern family.", "score": 0.7},
                 {"text": "As long as the home doesn't suffer for it.", "score": 0.35},
                 {"text": "It's between her and my son.", "score": 0.5}]},
            {"id": "am_3", "topic": "WHAT TO CALL HER",
             "question": "What would you ideally want your daughter-in-law to call you?",
             "choices": [
                 {"text": "Whatever she's comfortable with.", "score": 1.0},
                 {"text": "Mama, like a daughter.", "score": 0.6},
                 {"text": "Aunty initially — Mama if she comes to feel that way.", "score": 0.75},
                 {"text": "It's not the word, it's the relationship.", "score": 0.85}]},
            {"id": "am_4", "topic": "HER FAMILY RELATIONSHIP",
             "question": "What's your view on her relationship with her own parents after marriage?",
             "choices": [
                 {"text": "They raised her. She should be with them often.", "score": 1.0},
                 {"text": "Of course she'll see them. Balance is key.", "score": 0.6},
                 {"text": "They're family too — we'd visit together.", "score": 0.5},
                 {"text": "It'll adjust naturally over time.", "score": 0.3}]},
            {"id": "am_5", "topic": "QUIET HOPE",
             "question": "What's your quiet hope about the woman who'll marry your son?",
             "choices": [
                 {"text": "That she's happy with him. That's the foundation of everything.", "score": 1.0},
                 {"text": "That she fits well into our family.", "score": 0.4},
                 {"text": "That she makes him a better man.", "score": 0.6},
                 {"text": "That she has the patience for a long marriage.", "score": 0.35}]}]},

    "ahmed_father": {
        "label": "Ahmed's Father", "emoji": "👨",
        "side": "Ahmed's Family",
        "scenarios": [
            {"id": "af_1", "topic": "WHAT HE WANTS",
             "question": "What do you most want from your daughter-in-law?",
             "choices": [
                 {"text": "That she's good to my son and finds happiness with him.", "score": 1.0},
                 {"text": "That she respects the family and we respect her.", "score": 0.7},
                 {"text": "That she's the kind of woman my son needs.", "score": 0.45},
                 {"text": "That she contributes to the home in her own way.", "score": 0.55}]},
            {"id": "af_2", "topic": "HER INDEPENDENCE",
             "question": "How do you feel about a daughter-in-law who has strong opinions?",
             "choices": [
                 {"text": "Good — a thinking woman is a good partner.", "score": 1.0},
                 {"text": "Fine, as long as there's respect when she disagrees.", "score": 0.65},
                 {"text": "As long as she knows when to listen.", "score": 0.35},
                 {"text": "My son needs that. He's stubborn — she'll balance him.", "score": 0.6}]},
            {"id": "af_3", "topic": "CONFLICT BETWEEN WIFE AND DAUGHTER-IN-LAW",
             "question": "If there's ever friction between your wife and your daughter-in-law, what's your role?",
             "choices": [
                 {"text": "Let them work it out unless it becomes serious.", "score": 0.7},
                 {"text": "Quietly support my wife — she's been here longer.", "score": 0.2},
                 {"text": "Hear both sides honestly.", "score": 1.0},
                 {"text": "Ask my son to manage it.", "score": 0.3}]},
            {"id": "af_4", "topic": "HER FINANCES",
             "question": "Should a daughter-in-law contribute financially to the household?",
             "choices": [
                 {"text": "If she earns, she decides what to do with it.", "score": 1.0},
                 {"text": "Only if she wants to — no obligation.", "score": 0.7},
                 {"text": "It's expected — we all contribute.", "score": 0.4},
                 {"text": "That's between her and my son.", "score": 0.55}]},
            {"id": "af_5", "topic": "LONG-TERM RELATIONSHIP",
             "question": "In 10 years, how do you imagine your relationship with your daughter-in-law?",
             "choices": [
                 {"text": "Like a daughter — fully family by then.", "score": 0.85},
                 {"text": "Close, but with her own household.", "score": 1.0},
                 {"text": "Respectful, depending on how she's been with us.", "score": 0.3},
                 {"text": "It'll be what it'll be. I don't predict.", "score": 0.5}]}]},
}

LETTERS = ["A", "B", "C", "D"]


def page_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400;1,700&family=Inter:wght@300;400;500;600&display=swap');

    .stApp {
        background: linear-gradient(160deg, #fbd8e6 0%, #f5bece 45%, #faccd8 75%, #f0b8c8 100%) !important;
        background-attachment: fixed !important;
    }
    .block-container { padding-top: 1rem !important; max-width: 900px !important; }

    .page-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.6rem; font-weight: 700; font-style: italic;
        color: #5a0c1e; text-align: center; margin-bottom: 0.2rem;
    }
    .page-sub {
        font-family: 'Inter', sans-serif; font-size: 0.88rem;
        color: rgba(90,12,30,0.55); text-align: center;
        letter-spacing: 0.3px; margin-bottom: 1rem;
    }
    .gold-line {
        width: 80px; height: 1px;
        background: linear-gradient(90deg, transparent, #c9a96e, transparent);
        margin: 0.5rem auto 1.5rem;
    }

    /* Member expander — dark header like screenshot */
    [data-testid="stExpander"] {
        border: none !important;
        border-radius: 12px !important;
        overflow: hidden !important;
        margin-bottom: 1rem !important;
        box-shadow: 0 2px 12px rgba(90,12,30,0.08) !important;
    }
    [data-testid="stExpander"] summary {
        background: #1a0a0e !important;
        border-radius: 10px !important;
        padding: 0.9rem 1.2rem !important;
    }
    [data-testid="stExpander"] summary span,
    [data-testid="stExpander"] summary p {
        color: white !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 500 !important;
        font-size: 0.95rem !important;
    }
    [data-testid="stExpander"] > div {
        background: white !important;
        border: 1px solid rgba(180,50,80,0.1) !important;
        border-top: none !important;
        padding: 1.2rem !important;
    }

    /* Question card */
    .q-card {
        background: white;
        border-radius: 12px;
        padding: 1.1rem 1.3rem;
        margin-bottom: 1rem;
        border: 1px solid rgba(180,50,80,0.1);
    }
    .q-topic {
        font-family: 'Inter', sans-serif;
        font-size: 0.68rem; font-weight: 600;
        letter-spacing: 2px; text-transform: uppercase;
        color: rgba(160,40,70,0.6); margin-bottom: 0.5rem;
    }
    .q-text {
        font-family: 'Inter', sans-serif;
        font-size: 0.95rem; color: #2a0a12; line-height: 1.55;
    }

    /* A/B/C/D option rows */
    .opt-row {
        display: flex; align-items: center; gap: 12px;
        background: white; border-radius: 10px;
        border: 1px solid rgba(180,50,80,0.12);
        padding: 0.7rem 1rem; margin-bottom: 0.5rem;
        cursor: pointer; transition: all 0.2s;
    }
    .opt-row:hover {
        background: rgba(255,240,246,0.8);
        border-color: rgba(184,48,80,0.3);
    }
    .opt-letter {
        width: 30px; height: 30px; flex-shrink: 0;
        border-radius: 50%;
        background: rgba(184,48,80,0.06);
        border: 1px solid rgba(184,48,80,0.2);
        display: flex; align-items: center; justify-content: center;
        font-family: 'Inter', sans-serif;
        font-size: 0.78rem; font-weight: 600;
        color: rgba(184,48,80,0.7);
    }
    .opt-text {
        font-family: 'Inter', sans-serif;
        font-size: 0.88rem; color: #3a1018; line-height: 1.45;
    }

    /* Hide default radio dot */
    div[data-testid="stRadio"] > div > label > div:first-child {
        display: none !important;
    }
    div[data-testid="stRadio"] > div {
        gap: 0.45rem !important;
        display: flex !important;
        flex-direction: column !important;
    }
    div[data-testid="stRadio"] > div > label {
        background: white !important;
        border: 1px solid rgba(180,50,80,0.15) !important;
        border-radius: 10px !important;
        padding: 0.7rem 1rem !important;
        margin: 0 !important;
        cursor: pointer !important;
        transition: all 0.2s !important;
    }
    div[data-testid="stRadio"] > div > label:hover {
        background: rgba(255,240,246,0.9) !important;
        border-color: rgba(184,48,80,0.35) !important;
    }
    div[data-testid="stRadio"] > div > label > div > p {
        color: #3a1018 !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.88rem !important;
        margin: 0 !important;
        line-height: 1.45 !important;
    }

    /* Progress bar */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #b83050, #c9a96e) !important;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab"] {
        background: rgba(255,255,255,0.55) !important;
        border-radius: 8px 8px 0 0 !important;
        padding: 0.5rem 1.2rem !important;
        color: rgba(90,12,30,0.6) !important;
        border: 1px solid rgba(180,50,80,0.1) !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.85rem !important;
        font-weight: 500 !important;
    }
    .stTabs [aria-selected="true"] {
        background: #b83050 !important;
        color: white !important;
        border-color: transparent !important;
    }

    /* Buttons */
    .stButton > button {
        background: #b83050 !important;
        color: white !important; border: none !important;
        border-radius: 50px !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 500 !important;
        box-shadow: 0 4px 14px rgba(184,48,80,0.25) !important;
    }

    .score-box {
        background: white; border-radius: 14px;
        padding: 1.2rem 1.5rem; text-align: center;
        border: 1px solid rgba(180,50,80,0.1);
        margin: 0.5rem 0;
    }
    .score-num {
        font-family: 'Playfair Display', serif;
        font-size: 2.5rem; font-weight: 700;
        font-style: italic; color: #b83050;
    }
    .score-lbl {
        font-family: 'Inter', sans-serif;
        font-size: 0.82rem; color: rgba(90,12,30,0.55);
        margin-top: 0.2rem;
    }
    </style>
    """, unsafe_allow_html=True)


def compute_score(responses, member_key):
    member = INLAW_SCENARIOS[member_key]
    scores = []
    for sc in member["scenarios"]:
        if sc["id"] in responses:
            idx = responses[sc["id"]]
            scores.append(sc["choices"][idx]["score"])
    if not scores:
        return None
    return round(sum(scores) / len(scores) * 100, 1)


def render_member(member_key):
    m = INLAW_SCENARIOS[member_key]
    resp_key = f"il_{member_key}"
    if resp_key not in st.session_state:
        st.session_state[resp_key] = {}
    responses = st.session_state[resp_key]
    done = len(responses)
    total = len(m["scenarios"])

    with st.expander(f"{m['emoji']} {m['label']}", expanded=True):
        # Progress
        st.progress(done / total if total else 0)
        st.caption(f"{done} of {total} answered")

        if done >= total:
            score = compute_score(responses, member_key)
            color = "#2e7d32" if score >= 70 else "#f57f17" if score >= 45 else "#c62828"
            label = "Supportive ✓" if score >= 70 else "Mixed ◐" if score >= 45 else "Friction Risk ✗"
            st.markdown(f"""
            <div class="score-box">
                <div class="score-num" style="color:{color};">{score}%</div>
                <div class="score-lbl">{label}</div>
            </div>
            """, unsafe_allow_html=True)
            return score

        # Show current question
        for sc in m["scenarios"]:
            if sc["id"] in responses:
                continue

            st.markdown(f"""
            <div class="q-card">
                <div class="q-topic">{sc['topic']}</div>
                <div class="q-text">{sc['question']}</div>
            </div>
            """, unsafe_allow_html=True)

            # Options with A/B/C/D prefix
            opts = [f"{LETTERS[i]}.  {c['text']}" for i, c in enumerate(sc["choices"])]
            sel = st.radio("", opts, key=f"r_{sc['id']}", index=None,
                           label_visibility="collapsed")
            if sel is not None:
                idx = opts.index(sel)
                responses[sc["id"]] = idx
                st.session_state[resp_key] = responses
                st.rerun()
            break

    return compute_score(responses, member_key) if done >= total else None


def main():
    st.set_page_config(page_title="Zawaj — Family Profile",
                       page_icon="🏠", layout="centered")
    page_css()

    st.markdown('<div class="page-title">Family Profile</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">Both families · Member-by-member · Optional siblings</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

    # Demo expander
    with st.expander("⚙️ Family Setup — toggle which siblings exist"):
        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("Fill Sara's family", use_container_width=True):
                for mk in ["sara_mother", "sara_father"]:
                    m = INLAW_SCENARIOS[mk]
                    st.session_state[f"il_{mk}"] = {sc["id"]: 0 for sc in m["scenarios"]}
                st.rerun()
        with c2:
            if st.button("Fill Ahmed's family", use_container_width=True):
                for mk in ["ahmed_mother", "ahmed_father"]:
                    m = INLAW_SCENARIOS[mk]
                    st.session_state[f"il_{mk}"] = {sc["id"]: 0 for sc in m["scenarios"]}
                st.rerun()
        with c3:
            if st.button("Reset All", use_container_width=True):
                for mk in INLAW_SCENARIOS:
                    if f"il_{mk}" in st.session_state:
                        del st.session_state[f"il_{mk}"]
                st.rerun()

    tab1, tab2, tab3, tab4 = st.tabs([
        "👰 Sara's Family", "🤵 Ahmed's Family",
        "💬 Claims vs Hopes", "🔺 Final Analysis"
    ])

    with tab1:
        st.markdown("#### Sara's Family")
        st.caption("Profile each member individually. Sibling sections appear if enabled above.")
        sm = render_member("sara_mother")
        sf = render_member("sara_father")

    with tab2:
        st.markdown("#### Ahmed's Family")
        st.caption("Profile each member individually. Sibling sections appear if enabled above.")
        am = render_member("ahmed_mother")
        af = render_member("ahmed_father")

    with tab3:
        st.markdown("#### Claims vs Hopes")
        st.info("This section compares what the boy claims about his family versus what his family actually said — and what the girl hopes for.")
        st.caption("Complete both family assessments first to unlock this analysis.")

    with tab4:
        st.markdown("#### Final Analysis")
        scores = {}
        for mk, lbl in [("sara_mother", "Sara's Mother"), ("sara_father", "Sara's Father"),
                        ("ahmed_mother", "Ahmed's Mother"), ("ahmed_father", "Ahmed's Father")]:
            if f"il_{mk}" in st.session_state:
                s = compute_score(st.session_state[f"il_{mk}"], mk)
                if s is not None:
                    scores[lbl] = s

        if len(scores) >= 2:
            c1, c2 = st.columns(2)
            sara = {k: v for k, v in scores.items() if "Sara" in k}
            ahmed = {k: v for k, v in scores.items() if "Ahmed" in k}

            with c1:
                st.markdown("**👰 Sara's Family**")
                for lbl, sc in sara.items():
                    color = "#2e7d32" if sc >= 70 else "#f57f17" if sc >= 45 else "#c62828"
                    st.markdown(f"""
                    <div style="display:flex;justify-content:space-between;
                         background:white;border-radius:8px;padding:0.6rem 1rem;
                         margin-bottom:0.4rem;border:1px solid rgba(180,50,80,0.1);">
                        <span style="font-family:'Inter',sans-serif;font-size:0.85rem;color:#3a1018;">{lbl}</span>
                        <span style="font-weight:700;color:{color};font-size:1rem;">{sc}%</span>
                    </div>""", unsafe_allow_html=True)

            with c2:
                st.markdown("**🤵 Ahmed's Family**")
                for lbl, sc in ahmed.items():
                    color = "#2e7d32" if sc >= 70 else "#f57f17" if sc >= 45 else "#c62828"
                    st.markdown(f"""
                    <div style="display:flex;justify-content:space-between;
                         background:white;border-radius:8px;padding:0.6rem 1rem;
                         margin-bottom:0.4rem;border:1px solid rgba(180,50,80,0.1);">
                        <span style="font-family:'Inter',sans-serif;font-size:0.85rem;color:#3a1018;">{lbl}</span>
                        <span style="font-weight:700;color:{color};font-size:1rem;">{sc}%</span>
                    </div>""", unsafe_allow_html=True)

            combined = round(sum(scores.values()) / len(scores), 1)
            verdict = "Strong Family Alignment" if combined >= 70 else \
                      "Moderate — Discuss Key Areas" if combined >= 45 else \
                      "Significant Friction — Open Conversations Needed"
            st.markdown(f"""
            <br>
            <div style="background:white;border-radius:16px;padding:1.5rem;
                 text-align:center;border:1px solid rgba(180,50,80,0.15);
                 box-shadow:0 4px 20px rgba(90,12,30,0.08);margin-top:1rem;">
                <div style="font-family:'Playfair Display',serif;font-size:3rem;
                     font-weight:700;font-style:italic;color:#b83050;">{combined}%</div>
                <div style="font-family:'Inter',sans-serif;font-size:1rem;
                     color:#5a0c1e;font-weight:600;margin-top:-0.3rem;">{verdict}</div>
                <div style="font-size:0.78rem;color:rgba(90,12,30,0.45);
                     margin-top:0.4rem;font-family:'Inter',sans-serif;">
                     Combined across {len(scores)} family members
                </div>
            </div>""", unsafe_allow_html=True)
            st.session_state["inlaw_score"] = combined
            st.session_state["inlaws_complete"] = True
            st.markdown("<br>", unsafe_allow_html=True)
            st.success("✅ Family scores saved! Go to Results Dashboard.")
        else:
            st.info("Complete Sara's and Ahmed's family assessments to see the final analysis.")


main()
