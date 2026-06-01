"""Page 2 — In-Laws Questionnaire. Fresh build matching app theme."""

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
             "question": "What would make you most uncomfortable about a potential son-in-law — even if everything else seemed fine?",
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
                 {"text": "That she doesn't drift too far from us — that we remain part of her life.", "score": 0.4},
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
                 {"text": "He should talk to her directly until they understand each other.", "score": 1.0},
                 {"text": "He should know when to walk away and revisit later.", "score": 0.55},
                 {"text": "He should be the calmer one — someone has to be.", "score": 0.5},
                 {"text": "He should bring it to the family if they can't resolve it.", "score": 0.2}]},
            {"id": "sf_3", "topic": "FINANCIAL EXPECTATIONS",
             "question": "What do you expect from a son-in-law financially?",
             "choices": [
                 {"text": "That he and my daughter handle their finances together as they see fit.", "score": 1.0},
                 {"text": "That he's stable and able to provide for the household.", "score": 0.6},
                 {"text": "That he's transparent — no surprises.", "score": 0.65},
                 {"text": "That my daughter never has to worry about money.", "score": 0.5}]},
            {"id": "sf_4", "topic": "AUTHORITY DYNAMIC",
             "question": "Do you see a son-in-law as someone who should defer to elders, or someone with his own standing?",
             "choices": [
                 {"text": "His own standing. He's not our subordinate.", "score": 1.0},
                 {"text": "Both — respect for elders, but his decisions are his.", "score": 0.7},
                 {"text": "He should listen — that's how a young man matures.", "score": 0.3},
                 {"text": "It depends on his own family's culture. We'd adapt.", "score": 0.55}]},
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
            {"id": "am_1", "topic": "DAUGHTER-IN-LAW'S PLACE IN THE HOME",
             "question": "How do you see a daughter-in-law in your home?",
             "choices": [
                 {"text": "As my son's wife — her home is the one she builds with him.", "score": 1.0},
                 {"text": "As a daughter — fully part of the family from day one.", "score": 0.75},
                 {"text": "As family, with time. Trust is built.", "score": 0.5},
                 {"text": "Someone who'll bring her own ways — and we'll find a rhythm together.", "score": 0.85}]},
            {"id": "am_2", "topic": "HER CAREER AFTER MARRIAGE",
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
            {"id": "am_4", "topic": "HER RELATIONSHIP WITH HER OWN FAMILY",
             "question": "What's your view on her relationship with her own parents after marriage?",
             "choices": [
                 {"text": "They raised her. She should be with them often.", "score": 1.0},
                 {"text": "Of course she'll see them. Balance is the key.", "score": 0.6},
                 {"text": "They're family too — we'd visit together.", "score": 0.5},
                 {"text": "It'll adjust naturally over time.", "score": 0.3}]},
            {"id": "am_5", "topic": "QUIET HOPE ABOUT SON'S WIFE",
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
            {"id": "af_1", "topic": "WHAT HE WANTS FROM DAUGHTER-IN-LAW",
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
                 {"text": "I'd let them work it out unless it becomes serious.", "score": 0.7},
                 {"text": "I'd quietly support my wife — she's been here longer.", "score": 0.2},
                 {"text": "I'd hear both sides honestly.", "score": 1.0},
                 {"text": "I'd ask my son to manage it.", "score": 0.3}]},
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

OPTION_LABELS = ["A", "B", "C", "D"]


def page_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;900&family=Poppins:wght@300;400;500;600&display=swap');

    .stApp {
        background: linear-gradient(135deg, #FDEEF2 0%, #FFFFFF 50%, #FDEEF2 100%);
        background-attachment: fixed;
    }
    .block-container { padding-top: 1.5rem; max-width: 1050px; }
    h1,h2,h3,h4 { font-family: 'Playfair Display', serif !important; color: #5C2A3E !important; }
    p, div, span, label, .stMarkdown { font-family: 'Poppins', sans-serif; color: #3A1A2B; }

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
        font-family: 'Poppins', sans-serif;
    }
    .divider-gold {
        width: 120px; height: 2px;
        background: linear-gradient(90deg, transparent, #C9A96E, transparent);
        margin: 1rem auto;
    }

    .member-card {
        background: white;
        border-radius: 18px;
        padding: 1.6rem 1.8rem;
        box-shadow: 0 4px 20px rgba(212,87,122,0.1);
        margin-bottom: 1.5rem;
        border-top: 3px solid #D4577A;
    }
    .member-name {
        font-family: 'Playfair Display', serif;
        font-size: 1.3rem; font-weight: 700;
        color: #5C2A3E; margin-bottom: 0.2rem;
    }
    .member-side {
        font-size: 0.78rem; color: #8A6B7A;
        text-transform: uppercase; letter-spacing: 2px;
        font-family: 'Poppins', sans-serif;
    }

    .q-card {
        background: #FDF5F7;
        border-radius: 14px;
        padding: 1.2rem 1.5rem;
        margin: 1rem 0 0.8rem;
        border-left: 3px solid #D4577A;
    }
    .q-topic {
        font-size: 0.68rem; font-weight: 600;
        letter-spacing: 2.5px; text-transform: uppercase;
        color: #D4577A; margin-bottom: 0.5rem;
        font-family: 'Poppins', sans-serif;
    }
    .q-text {
        font-family: 'Playfair Display', serif;
        font-size: 1.05rem; font-style: italic;
        color: #3A1A2B; line-height: 1.55;
    }

    .option-btn {
        display: flex; align-items: center; gap: 14px;
        background: white;
        border: 1.5px solid #F0D0DC;
        border-radius: 12px;
        padding: 0.75rem 1.1rem;
        margin-bottom: 0.55rem;
        cursor: pointer;
        transition: all 0.2s;
        width: 100%;
    }
    .option-btn:hover {
        background: #FFF0F4;
        border-color: #D4577A;
        transform: translateX(4px);
    }
    .option-letter {
        width: 32px; height: 32px;
        background: linear-gradient(135deg, #F8D7DE, #FDEEF2);
        border: 1.5px solid #D4577A;
        border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-family: 'Poppins', sans-serif;
        font-size: 0.8rem; font-weight: 600;
        color: #D4577A; flex-shrink: 0;
    }
    .option-text {
        font-family: 'Poppins', sans-serif;
        font-size: 0.9rem; color: #3A1A2B; line-height: 1.4;
    }

    .score-badge {
        display: inline-block;
        padding: 0.4rem 1.2rem;
        border-radius: 20px;
        font-family: 'Poppins', sans-serif;
        font-size: 0.85rem; font-weight: 600;
        margin-top: 0.5rem;
    }
    .score-green { background: #E8F5E9; color: #2E7D32; border: 1px solid #A5D6A7; }
    .score-amber { background: #FFF8E1; color: #F57F17; border: 1px solid #FFE082; }
    .score-red   { background: #FFEBEE; color: #C62828; border: 1px solid #EF9A9A; }

    .answered-row {
        display: flex; align-items: center; gap: 10px;
        background: white; border-radius: 10px;
        padding: 0.6rem 1rem; margin-bottom: 0.4rem;
        border: 1px solid #F0D0DC;
    }
    .answered-check { color: #6BAF73; font-size: 1rem; }
    .answered-text  { font-size: 0.82rem; color: #5A3A4A; font-family: 'Poppins', sans-serif; }

    .stTabs [data-baseweb="tab"] {
        background: white; border-radius: 10px 10px 0 0;
        padding: 0.6rem 1.4rem; color: #8A6B7A;
        border: 1px solid #F8D7DE; border-bottom: none;
        font-family: 'Poppins', sans-serif; font-weight: 500;
        font-size: 0.9rem;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #5C2A3E, #D4577A) !important;
        color: white !important; border-color: transparent !important;
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
        box-shadow: 0 4px 14px rgba(212,87,122,0.3) !important;
    }
    .complete-card {
        background: linear-gradient(135deg, #6BAF73, #4A8A52);
        border-radius: 14px; padding: 1rem 1.5rem;
        text-align: center; color: white;
        font-family: 'Playfair Display', serif;
        font-size: 1.1rem; font-weight: 600;
        box-shadow: 0 4px 16px rgba(107,175,115,0.3);
        margin: 0.5rem 0;
    }
    .combined-card {
        background: white; border-radius: 18px;
        padding: 2rem; text-align: center;
        box-shadow: 0 6px 24px rgba(212,87,122,0.12);
        border-top: 3px solid #C9A96E;
    }
    .combined-score {
        font-family: 'Playfair Display', serif;
        font-size: 4rem; font-weight: 700;
        background: linear-gradient(135deg, #5C2A3E, #D4577A);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .combined-label {
        font-family: 'Playfair Display', serif;
        font-size: 1.3rem; color: #5C2A3E;
        font-weight: 600; margin-top: -0.5rem;
    }

    [data-testid="stExpander"] details summary span {
        color: #5C2A3E !important;
        font-family: 'Poppins', sans-serif !important;
        font-weight: 600 !important;
    }

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(14px); }
        to   { opacity: 1; transform: translateY(0); }
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

    # Member header card
    st.markdown(f"""
    <div class="member-card">
        <div class="member-name">{m['emoji']} {m['label']}</div>
        <div class="member-side">{m['side']} · {total} scenarios</div>
    </div>
    """, unsafe_allow_html=True)

    st.progress(done / total if total else 0)
    st.caption(f"{done} of {total} answered")

    if done >= total:
        score = compute_score(responses, member_key)
        if score is not None:
            if score >= 70:
                badge = f'<span class="score-badge score-green">✓ {score}% — Supportive</span>'
            elif score >= 45:
                badge = f'<span class="score-badge score-amber">◐ {score}% — Mixed</span>'
            else:
                badge = f'<span class="score-badge score-red">✗ {score}% — Friction Risk</span>'
            st.markdown(f'<div class="complete-card">✨ Complete! {badge}</div>', unsafe_allow_html=True)
        return score

    # Show answered questions summary
    if done > 0:
        with st.expander(f"✅ {done} answered — click to review"):
            for sc in m["scenarios"]:
                if sc["id"] in responses:
                    idx = responses[sc["id"]]
                    chosen_text = sc["choices"][idx]["text"]
                    st.markdown(f"""
                    <div class="answered-row">
                        <span class="answered-check">✓</span>
                        <span class="answered-text"><b>{sc['topic']}</b> — {chosen_text}</span>
                    </div>
                    """, unsafe_allow_html=True)

    # Show next unanswered question
    for sc in m["scenarios"]:
        if sc["id"] in responses:
            continue

        st.markdown(f"""
        <div class="q-card">
            <div class="q-topic">{sc['topic']}</div>
            <div class="q-text">{sc['question']}</div>
        </div>
        """, unsafe_allow_html=True)

        # Render A/B/C/D options
        for i, choice in enumerate(sc["choices"]):
            letter = OPTION_LABELS[i]
            btn_key = f"opt_{sc['id']}_{i}"
            col_l, col_r = st.columns([1, 12])
            with col_l:
                st.markdown(f'<div class="option-letter">{letter}</div>', unsafe_allow_html=True)
            with col_r:
                if st.button(choice["text"], key=btn_key, use_container_width=True):
                    responses[sc["id"]] = i
                    st.session_state[resp_key] = responses
                    st.rerun()
        break

    return None


def main():
    st.set_page_config(page_title="Zawaj — Family Profile", page_icon="🏠", layout="centered")
    page_css()

    st.markdown('<p class="page-title">🏠 Family Profile</p>', unsafe_allow_html=True)
    st.markdown('<p class="page-sub">Both families · Member-by-member · Optional siblings</p>', unsafe_allow_html=True)
    st.markdown('<div class="divider-gold"></div>', unsafe_allow_html=True)

    # Demo / Reset
    with st.expander("⚡ Demo Mode — auto-fill all family members"):
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

    st.markdown("<br>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["💐 Sara's Family", "🌙 Ahmed's Family", "🔺 Combined Analysis"])

    with tab1:
        st.markdown("#### Sara's family expectations of her future husband")
        st.info("These questions reveal what each family member truly values — general standing values, not about a specific person.")
        sm_score = render_member("sara_mother")
        st.markdown("---")
        sf_score = render_member("sara_father")

    with tab2:
        st.markdown("#### Ahmed's family expectations of his future wife")
        st.info("These questions reveal what each family member truly values — general standing values, not about a specific person.")
        am_score = render_member("ahmed_mother")
        st.markdown("---")
        af_score = render_member("ahmed_father")

    with tab3:
        st.markdown("#### Combined Family Compatibility")

        scores = {}
        for mk, lbl in [("sara_mother", "Sara's Mother"), ("sara_father", "Sara's Father"),
                        ("ahmed_mother", "Ahmed's Mother"), ("ahmed_father", "Ahmed's Father")]:
            resp_key = f"il_{mk}"
            if resp_key in st.session_state:
                s = compute_score(st.session_state[resp_key], mk)
                if s is not None:
                    scores[lbl] = s

        if scores:
            col1, col2 = st.columns(2)
            sara_scores = {k: v for k, v in scores.items() if "Sara" in k}
            ahmed_scores = {k: v for k, v in scores.items() if "Ahmed" in k}

            with col1:
                st.markdown("**💐 Sara's Family**")
                for lbl, sc in sara_scores.items():
                    color = "#6BAF73" if sc >= 70 else "#E8A846" if sc >= 45 else "#D4577A"
                    st.markdown(f"""
                    <div style="display:flex;justify-content:space-between;align-items:center;
                         background:white;border-radius:10px;padding:0.6rem 1rem;
                         margin-bottom:0.4rem;border:1px solid #F0D0DC;">
                        <span style="font-family:'Poppins',sans-serif;font-size:0.88rem;color:#3A1A2B;">{lbl}</span>
                        <span style="font-weight:700;color:{color};font-family:'Playfair Display',serif;font-size:1.1rem;">{sc}%</span>
                    </div>""", unsafe_allow_html=True)

            with col2:
                st.markdown("**🌙 Ahmed's Family**")
                for lbl, sc in ahmed_scores.items():
                    color = "#6BAF73" if sc >= 70 else "#E8A846" if sc >= 45 else "#D4577A"
                    st.markdown(f"""
                    <div style="display:flex;justify-content:space-between;align-items:center;
                         background:white;border-radius:10px;padding:0.6rem 1rem;
                         margin-bottom:0.4rem;border:1px solid #F0D0DC;">
                        <span style="font-family:'Poppins',sans-serif;font-size:0.88rem;color:#3A1A2B;">{lbl}</span>
                        <span style="font-weight:700;color:{color};font-family:'Playfair Display',serif;font-size:1.1rem;">{sc}%</span>
                    </div>""", unsafe_allow_html=True)

            if len(scores) >= 2:
                combined = round(sum(scores.values()) / len(scores), 1)
                verdict = "Strong Family Alignment" if combined >= 70 else "Moderate Alignment — Discuss Key Areas" if combined >= 45 else "Significant Friction — Open Conversations Needed"
                color = "#6BAF73" if combined >= 70 else "#E8A846" if combined >= 45 else "#D4577A"
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown(f"""
                <div class="combined-card">
                    <div class="combined-score">{combined}%</div>
                    <div class="combined-label">{verdict}</div>
                    <div style="font-size:0.8rem;color:#8A6B7A;margin-top:0.5rem;font-family:'Poppins',sans-serif;">
                        Combined across {len(scores)} family members
                    </div>
                </div>
                """, unsafe_allow_html=True)
                st.session_state["inlaw_score"] = combined
                st.session_state["inlaws_complete"] = True
                st.markdown("<br>", unsafe_allow_html=True)
                st.success("✅ Family scores saved! Go to Results Dashboard.")
        else:
            st.info("Complete the family assessments in Sara's and Ahmed's tabs to see the combined score here.")


main()
