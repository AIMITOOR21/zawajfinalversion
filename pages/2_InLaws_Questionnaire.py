"""Page 2 — In-Laws Questionnaire. Fixed version matching original style."""

import streamlit as st
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

INLAW_SCENARIOS = {
    "sara_mother": {
        "label": "Sara's Mother", "emoji": "👩",
        "scenarios": [
            {"id": "sm_1", "topic": "Cultural Outlook",
             "question": "When you imagine the kind of man you'd want for your daughter, what comes to mind first?",
             "choices": [
                 {"text": "Someone she chooses for herself, that she can build a life with.", "score": 1.0},
                 {"text": "A man from a good, respectable family — with steady prospects.", "score": 0.45},
                 {"text": "Someone who would treat her well and adjust to our family's rhythm.", "score": 0.4},
                 {"text": "A man with character. Money and background are secondary.", "score": 0.7}]},
            {"id": "sm_2", "topic": "Most Important Quality",
             "question": "If you had to name the single most important quality in a son-in-law, what would it be?",
             "choices": [
                 {"text": "That my daughter feels respected by him.", "score": 1.0},
                 {"text": "That he comes from people we know and trust.", "score": 0.35},
                 {"text": "That he listens — to her, to us, to wisdom.", "score": 0.5},
                 {"text": "That he can stand on his own — emotionally, financially, socially.", "score": 0.7}]},
            {"id": "sm_3", "topic": "Relationship with Son-in-Law",
             "question": "What kind of relationship would you ideally have with your daughter's husband?",
             "choices": [
                 {"text": "Close, like a son — someone we'd both lean on and support.", "score": 0.9},
                 {"text": "Respectful — we don't need to be close, just kind.", "score": 0.65},
                 {"text": "I'd want him to come to us when things get difficult.", "score": 0.4},
                 {"text": "Whatever feels natural. Some sons-in-law are close, some aren't.", "score": 0.5}]},
            {"id": "sm_4", "topic": "Hesitation",
             "question": "What would make you most uncomfortable about a potential son-in-law?",
             "choices": [
                 {"text": "If my daughter seemed unsure about him, even slightly.", "score": 1.0},
                 {"text": "If his family had a reputation or background we weren't sure of.", "score": 0.35},
                 {"text": "If he seemed the kind to dominate or shut her down.", "score": 0.8},
                 {"text": "If he was too independent — too much his own person.", "score": 0.2}]},
            {"id": "sm_5", "topic": "Quiet Hope",
             "question": "What's the quiet hope you carry about your daughter's eventual marriage?",
             "choices": [
                 {"text": "That she stays herself — that marriage adds to her, doesn't shrink her.", "score": 1.0},
                 {"text": "That she's well-settled and never has to worry about anything.", "score": 0.55},
                 {"text": "That she doesn't drift too far from us.", "score": 0.4},
                 {"text": "That her husband becomes part of our family, fully.", "score": 0.5}]}]},
    "sara_father": {
        "label": "Sara's Father", "emoji": "👨",
        "scenarios": [
            {"id": "sf_1", "topic": "Son-in-Law's Role",
             "question": "What's the most important thing for a son-in-law to be for your daughter?",
             "choices": [
                 {"text": "A partner — someone who walks beside her, not ahead of her.", "score": 1.0},
                 {"text": "A protector — financially, socially, in every way.", "score": 0.5},
                 {"text": "A steady presence — someone who keeps her grounded.", "score": 0.45},
                 {"text": "Someone who genuinely values what she brings to the marriage.", "score": 0.8}]},
            {"id": "sf_2", "topic": "Handling Disagreements",
             "question": "How should a son-in-law handle a disagreement with your daughter?",
             "choices": [
                 {"text": "Talk to her directly until they understand each other.", "score": 1.0},
                 {"text": "Know when to walk away and revisit later.", "score": 0.55},
                 {"text": "Be the calmer one — someone has to be.", "score": 0.5},
                 {"text": "Bring it to the family if they can't resolve it.", "score": 0.2}]},
            {"id": "sf_3", "topic": "Financial Expectations",
             "question": "What do you expect from a son-in-law financially?",
             "choices": [
                 {"text": "That he and my daughter handle finances together as they see fit.", "score": 1.0},
                 {"text": "That he's stable and able to provide for the household.", "score": 0.6},
                 {"text": "That he's transparent — no surprises.", "score": 0.65},
                 {"text": "That my daughter never has to worry about money.", "score": 0.5}]},
            {"id": "sf_4", "topic": "Authority Dynamic",
             "question": "Do you see a son-in-law as someone who should defer to elders, or have his own standing?",
             "choices": [
                 {"text": "His own standing. He's not our subordinate.", "score": 1.0},
                 {"text": "Both — respect for elders, but his decisions are his.", "score": 0.7},
                 {"text": "He should listen — that's how a young man matures.", "score": 0.3},
                 {"text": "It depends on his family's culture. We'd adapt.", "score": 0.55}]},
            {"id": "sf_5", "topic": "Private Worry",
             "question": "What's your private worry about your daughter's future husband?",
             "choices": [
                 {"text": "That he won't show up for her when she's struggling.", "score": 1.0},
                 {"text": "That his family will pull him away from her.", "score": 0.4},
                 {"text": "That she'll soften too much for him — lose her edge.", "score": 0.5},
                 {"text": "I don't worry. She's strong enough to choose well.", "score": 0.7}]}]},
    "ahmed_mother": {
        "label": "Ahmed's Mother", "emoji": "👩",
        "scenarios": [
            {"id": "am_1", "topic": "Daughter-in-Law's Place",
             "question": "How do you see a daughter-in-law in your home?",
             "choices": [
                 {"text": "As my son's wife — her home is the one she builds with him.", "score": 1.0},
                 {"text": "As a daughter — fully part of the family from day one.", "score": 0.75},
                 {"text": "As family, with time. Trust is built.", "score": 0.5},
                 {"text": "Someone who'll bring her own ways — and we'll find a rhythm.", "score": 0.85}]},
            {"id": "am_2", "topic": "Her Career",
             "question": "What's your view on a daughter-in-law continuing her career after marriage?",
             "choices": [
                 {"text": "Her decision entirely.", "score": 1.0},
                 {"text": "Of course — we're a modern family.", "score": 0.7},
                 {"text": "As long as the home doesn't suffer for it.", "score": 0.35},
                 {"text": "It's between her and my son.", "score": 0.5}]},
            {"id": "am_3", "topic": "What to Call Her",
             "question": "What would you ideally want your daughter-in-law to call you?",
             "choices": [
                 {"text": "Whatever she's comfortable with.", "score": 1.0},
                 {"text": "Mama, like a daughter.", "score": 0.6},
                 {"text": "Aunty initially — Mama if she comes to feel that way.", "score": 0.75},
                 {"text": "It's not the word, it's the relationship.", "score": 0.85}]},
            {"id": "am_4", "topic": "Her Family Relationship",
             "question": "What's your view on her relationship with her own parents after marriage?",
             "choices": [
                 {"text": "They raised her. She should be with them often.", "score": 1.0},
                 {"text": "Of course she'll see them. Balance is key.", "score": 0.6},
                 {"text": "They're family too — we'd visit together.", "score": 0.5},
                 {"text": "It'll adjust naturally over time.", "score": 0.3}]},
            {"id": "am_5", "topic": "Quiet Hope",
             "question": "What's your quiet hope about the woman who'll marry your son?",
             "choices": [
                 {"text": "That she's happy with him. That's the foundation of everything.", "score": 1.0},
                 {"text": "That she fits well into our family.", "score": 0.4},
                 {"text": "That she makes him a better man.", "score": 0.6},
                 {"text": "That she has the patience for a long marriage.", "score": 0.35}]}]},
    "ahmed_father": {
        "label": "Ahmed's Father", "emoji": "👨",
        "scenarios": [
            {"id": "af_1", "topic": "What He Wants",
             "question": "What do you most want from your daughter-in-law?",
             "choices": [
                 {"text": "That she's good to my son and finds happiness with him.", "score": 1.0},
                 {"text": "That she respects the family and we respect her.", "score": 0.7},
                 {"text": "That she's the kind of woman my son needs.", "score": 0.45},
                 {"text": "That she contributes to the home in her own way.", "score": 0.55}]},
            {"id": "af_2", "topic": "Her Independence",
             "question": "How do you feel about a daughter-in-law who has strong opinions?",
             "choices": [
                 {"text": "Good — a thinking woman is a good partner.", "score": 1.0},
                 {"text": "Fine, as long as there's respect when she disagrees.", "score": 0.65},
                 {"text": "As long as she knows when to listen.", "score": 0.35},
                 {"text": "My son needs that. He's stubborn — she'll balance him.", "score": 0.6}]},
            {"id": "af_3", "topic": "Conflict Role",
             "question": "If there's ever friction between your wife and your daughter-in-law, what's your role?",
             "choices": [
                 {"text": "Let them work it out unless it becomes serious.", "score": 0.7},
                 {"text": "Quietly support my wife — she's been here longer.", "score": 0.2},
                 {"text": "Hear both sides honestly.", "score": 1.0},
                 {"text": "Ask my son to manage it.", "score": 0.3}]},
            {"id": "af_4", "topic": "Her Finances",
             "question": "Should a daughter-in-law contribute financially to the household?",
             "choices": [
                 {"text": "If she earns, she decides what to do with it.", "score": 1.0},
                 {"text": "Only if she wants to — no obligation.", "score": 0.7},
                 {"text": "It's expected — we all contribute.", "score": 0.4},
                 {"text": "That's between her and my son.", "score": 0.55}]},
            {"id": "af_5", "topic": "Long-Term",
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
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;900&family=Poppins:wght@300;400;500;600&display=swap');

    .stApp {
        background: linear-gradient(135deg, #FDEEF2 0%, #FFFFFF 50%, #FDEEF2 100%);
        background-attachment: fixed;
    }
    .block-container { padding-top: 1.5rem; max-width: 1100px; }
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

    .role-intro {
        background: linear-gradient(135deg, #FDEEF2, #FFFFFF);
        padding: 1.2rem 1.4rem; border-radius: 16px;
        border: 1px solid #F8D7DE; margin-bottom: 1rem;
    }
    .role-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.4rem; color: #5C2A3E; font-weight: 600; margin: 0;
    }
    .role-sub { color: #8A6B7A; font-size: 0.9rem; font-style: italic; margin-top: 0.2rem; }

    .q-tile {
        background: white; padding: 1.2rem 1.4rem;
        border-radius: 14px; margin: 0.7rem 0;
        border: 1px solid #F8D7DE;
        box-shadow: 0 2px 8px rgba(212,87,122,0.06);
    }
    .q-topic {
        color: #D4577A; font-size: 0.72rem;
        letter-spacing: 2.5px; text-transform: uppercase;
        font-weight: 600; margin-bottom: 0.4rem;
    }
    .q-text { color: #5C2A3E; font-size: 1rem; font-weight: 500; }

    /* Fix expander */
    [data-testid="stExpander"] {
        background: white !important;
        border: 1px solid #F8D7DE !important;
        border-radius: 12px !important;
        margin: 0.5rem 0 !important;
    }
    [data-testid="stExpander"] summary,
    [data-testid="stExpander"] summary p,
    [data-testid="stExpander"] summary span {
        color: #5C2A3E !important;
        font-weight: 600 !important;
        font-family: 'Poppins', sans-serif !important;
    }
    [data-testid="stExpander"] > div > div {
        background: white !important;
    }

    /* Fix ALL text inside expander */
    [data-testid="stExpander"] p,
    [data-testid="stExpander"] span,
    [data-testid="stExpander"] label,
    [data-testid="stExpander"] div {
        color: #3E3E3E !important;
        font-family: 'Poppins', sans-serif !important;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 24px !important;
        font-family: 'Poppins', sans-serif !important;
        font-weight: 500 !important;
    }
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #D4577A, #5C2A3E) !important;
        color: white !important; border: none !important;
    }
    .stButton > button[kind="secondary"] {
        background: white !important;
        color: #5C2A3E !important;
        border: 1.5px solid #F8D7DE !important;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab"] {
        background: white; border-radius: 10px 10px 0 0;
        padding: 0.6rem 1.2rem; color: #8A6B7A;
        border: 1px solid #F8D7DE; border-bottom: none;
        font-family: 'Poppins', sans-serif; font-weight: 500;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #D4577A, #5C2A3E) !important;
        color: white !important;
    }

    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #D4577A, #C9A96E) !important;
    }

    .verdict-card {
        background: white; border-radius: 20px; padding: 2rem;
        text-align: center; border: 2px solid #F8D7DE;
        box-shadow: 0 8px 28px rgba(212,87,122,0.15); margin: 1rem 0;
    }
    .verdict-score {
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem; font-weight: 700; margin: 0.3rem 0;
    }

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(16px); }
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


def render_member(member_key, expanded=True):
    m = INLAW_SCENARIOS[member_key]
    resp_key = f"il_{member_key}"
    if resp_key not in st.session_state:
        st.session_state[resp_key] = {}
    responses = st.session_state[resp_key]
    done = len(responses)
    total = len(m["scenarios"])

    with st.expander(f"{m['emoji']} {m['label']}", expanded=expanded):
        st.progress(done / total if total else 0)
        st.caption(f"{done} of {total} answered")

        if done >= total:
            score = compute_score(responses, member_key)
            color = "#6BAF73" if score >= 70 else "#E8A846" if score >= 45 else "#D4577A"
            label = "Supportive ✓" if score >= 70 else "Mixed ◐" if score >= 45 else "Friction Risk ✗"
            st.markdown(f"<div style='background:{color}15; border:1px solid {color}40; border-radius:10px; padding:0.8rem; text-align:center; margin:0.5rem 0;'><span style='color:{color}; font-weight:700; font-size:1.2rem;'>{score}%</span><br><span style='color:{color}; font-size:0.85rem;'>{label}</span></div>", unsafe_allow_html=True)
            return score

        for sc in m["scenarios"]:
            if sc["id"] in responses:
                continue

            st.markdown(f"""
            <div class='q-tile'>
                <div class='q-topic'>{sc['topic']}</div>
                <div class='q-text'>{sc['question']}</div>
            </div>
            """, unsafe_allow_html=True)

            for i, choice in enumerate(sc["choices"]):
                col_btn, col_txt = st.columns([0.08, 0.92])
                with col_btn:
                    if st.button(LETTERS[i], key=f"{member_key}_{sc['id']}_{i}",
                                 type="secondary"):
                        responses[sc["id"]] = i
                        st.session_state[resp_key] = responses
                        st.rerun()
                with col_txt:
                    st.markdown(
                        f"<div style='padding-top:0.4rem; color:#3E3E3E; font-family:Poppins,sans-serif; font-size:0.9rem;'>{choice['text']}</div>",
                        unsafe_allow_html=True)
            break

    return compute_score(responses, member_key) if done >= total else None


def main():
    st.set_page_config(page_title="Family Profile · Zawaj",
                       page_icon="👨‍👩‍👧", layout="wide")
    page_css()

    st.markdown('<div class="page-title">Family Profile</div>', unsafe_allow_html=True)
    st.markdown('<div class="divider-gold"></div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">Both families · Member-by-member · Optional siblings</div>', unsafe_allow_html=True)

    name_a = st.session_state.get("names", {}).get("a", "Sara")
    name_b = st.session_state.get("names", {}).get("b", "Ahmed")

    with st.expander("⚙️ Family Setup — toggle which siblings exist"):
        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("⚡ Fill Sara's family demo", use_container_width=True):
                for mk in ["sara_mother", "sara_father"]:
                    m = INLAW_SCENARIOS[mk]
                    st.session_state[f"il_{mk}"] = {sc["id"]: 0 for sc in m["scenarios"]}
                st.rerun()
        with c2:
            if st.button("⚡ Fill Ahmed's family demo", use_container_width=True):
                for mk in ["ahmed_mother", "ahmed_father"]:
                    m = INLAW_SCENARIOS[mk]
                    st.session_state[f"il_{mk}"] = {sc["id"]: 0 for sc in m["scenarios"]}
                st.rerun()
        with c3:
            if st.button("🔄 Reset All", use_container_width=True):
                for mk in INLAW_SCENARIOS:
                    if f"il_{mk}" in st.session_state:
                        del st.session_state[f"il_{mk}"]
                st.rerun()

    tab1, tab2, tab3, tab4 = st.tabs([
        f"👰 {name_a}'s Family",
        f"🤵 {name_b}'s Family",
        "💬 Claims vs Hopes",
        "🔺 Final Analysis"
    ])

    with tab1:
        st.markdown(f"""
        <div class='role-intro'>
            <div class='role-title'>{name_a}'s Family</div>
            <div class='role-sub'>Profile each member individually. Sibling sections appear if enabled above.</div>
        </div>
        """, unsafe_allow_html=True)
        render_member("sara_mother", expanded=True)
        render_member("sara_father", expanded=False)

    with tab2:
        st.markdown(f"""
        <div class='role-intro'>
            <div class='role-title'>{name_b}'s Family</div>
            <div class='role-sub'>Profile each member individually.</div>
        </div>
        """, unsafe_allow_html=True)
        render_member("ahmed_mother", expanded=True)
        render_member("ahmed_father", expanded=False)

    with tab3:
        st.info("This section compares what the boy claims about his family versus what his family actually said — and what the girl hopes for. Complete both family tabs first.")

    with tab4:
        scores = {}
        for mk, lbl in [("sara_mother", f"{name_a}'s Mother"),
                        ("sara_father", f"{name_a}'s Father"),
                        ("ahmed_mother", f"{name_b}'s Mother"),
                        ("ahmed_father", f"{name_b}'s Father")]:
            if f"il_{mk}" in st.session_state:
                s = compute_score(st.session_state[f"il_{mk}"], mk)
                if s is not None:
                    scores[lbl] = s

        if len(scores) >= 2:
            c1, c2 = st.columns(2)
            sara_s = {k: v for k, v in scores.items() if name_a in k}
            ahmed_s = {k: v for k, v in scores.items() if name_b in k}

            with c1:
                st.markdown(f"**👰 {name_a}'s Family**")
                for lbl, sc in sara_s.items():
                    color = "#6BAF73" if sc >= 70 else "#E8A846" if sc >= 45 else "#D4577A"
                    st.markdown(f"<div style='display:flex;justify-content:space-between;background:white;border-radius:8px;padding:0.6rem 1rem;margin-bottom:0.4rem;border:1px solid #F8D7DE;'><span style='color:#3E3E3E;'>{lbl}</span><span style='font-weight:700;color:{color};'>{sc}%</span></div>", unsafe_allow_html=True)

            with c2:
                st.markdown(f"**🤵 {name_b}'s Family**")
                for lbl, sc in ahmed_s.items():
                    color = "#6BAF73" if sc >= 70 else "#E8A846" if sc >= 45 else "#D4577A"
                    st.markdown(f"<div style='display:flex;justify-content:space-between;background:white;border-radius:8px;padding:0.6rem 1rem;margin-bottom:0.4rem;border:1px solid #F8D7DE;'><span style='color:#3E3E3E;'>{lbl}</span><span style='font-weight:700;color:{color};'>{sc}%</span></div>", unsafe_allow_html=True)

            combined = round(sum(scores.values()) / len(scores), 1)
            color = "#6BAF73" if combined >= 70 else "#E8A846" if combined >= 45 else "#D4577A"
            verdict = "Strong Family Alignment" if combined >= 70 else "Moderate — Discuss Key Areas" if combined >= 45 else "Significant Friction — Open Conversations Needed"

            st.markdown(f"""
            <div class='verdict-card'>
                <div style='color:#8A6B7A;font-size:0.8rem;letter-spacing:3px;text-transform:uppercase;font-weight:600;'>Combined Family Score</div>
                <div class='verdict-score' style='color:{color};'>{combined}%</div>
                <div style='color:{color};font-family:"Playfair Display",serif;font-size:1.25rem;font-weight:600;'>{verdict}</div>
                <div style='color:#8A6B7A;margin-top:0.5rem;font-size:0.85rem;'>Combined across {len(scores)} family members</div>
            </div>
            """, unsafe_allow_html=True)
            st.session_state["inlaw_score"] = combined
            st.session_state["inlaws_complete"] = True
            st.success("✅ Family scores saved! Go to Results Dashboard.")
        else:
            st.info("Complete Sara's and Ahmed's family assessments to see the final analysis here.")


main()
