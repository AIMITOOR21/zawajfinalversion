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

    "sara_brother": {
        "label": "Sara's Brother", "emoji": "🧑",
        "scenarios": [
            {"id": "sb_1", "topic": "Support for the Marriage",
             "question": "If your sister comes to you with doubts before the wedding, what's your first instinct?",
             "choices": [
                 {"text": "Ask what she'd want to happen — support any decision.", "score": 1.0},
                 {"text": "Listen carefully, help her think through both options.", "score": 0.85},
                 {"text": "Tell her doubts are normal, encourage her to push through.", "score": 0.45},
                 {"text": "Go straight to your parents about it.", "score": 0.2}]},
            {"id": "sb_2", "topic": "Involvement in Couple's Life",
             "question": "If your sister texts you venting about her husband, what do you do?",
             "choices": [
                 {"text": "Listen, then ask if she's talked to him directly.", "score": 1.0},
                 {"text": "Take her side until she calms down.", "score": 0.55},
                 {"text": "Ask what he did — I want to know.", "score": 0.4},
                 {"text": "Stay out of it. It's their marriage.", "score": 0.6}]},
            {"id": "sb_3", "topic": "Where Loyalty Sits",
             "question": "If there's ever a serious conflict between your sister and her husband, where does your loyalty sit?",
             "choices": [
                 {"text": "With the truth — I'd back whoever's right.", "score": 1.0},
                 {"text": "With my sister — that's blood. But I'd hear him out.", "score": 0.65},
                 {"text": "With my sister always. He's not family the way she is.", "score": 0.25},
                 {"text": "With their marriage. I'd want them to work it out.", "score": 0.9}]}]},

    "sara_sister": {
        "label": "Sara's Sister", "emoji": "👧",
        "scenarios": [
            {"id": "ss_1", "topic": "What She Wants for Sister",
             "question": "What's the most important thing for your sister's husband to be for her?",
             "choices": [
                 {"text": "Her best friend.", "score": 1.0},
                 {"text": "A man who lets her be fully herself.", "score": 0.95},
                 {"text": "Someone who can handle her — she's not easy, I'd know.", "score": 0.3},
                 {"text": "Reliable. Someone she can count on.", "score": 0.7}]},
            {"id": "ss_2", "topic": "Visible Affection",
             "question": "Your sister and her husband are visibly affectionate around the family. How do you feel?",
             "choices": [
                 {"text": "Happy for them — that's a good marriage.", "score": 1.0},
                 {"text": "Fine, as long as it's appropriate.", "score": 0.55},
                 {"text": "A little awkward, but I get it.", "score": 0.6},
                 {"text": "I'm glad she's loved.", "score": 0.9}]},
            {"id": "ss_3", "topic": "Sister Spending Time with In-Laws",
             "question": "Your sister starts spending more time with his family than yours. How do you feel?",
             "choices": [
                 {"text": "That's how marriage works. She's building her new home.", "score": 1.0},
                 {"text": "I'd miss her, but I wouldn't say anything.", "score": 0.6},
                 {"text": "I'd hope she balances both sides.", "score": 0.5},
                 {"text": "I'd want her to remember where she came from.", "score": 0.2}]}]},

    "ahmed_brother": {
        "label": "Ahmed's Brother", "emoji": "🧑",
        "scenarios": [
            {"id": "abr_1", "topic": "What He Wants for Brother",
             "question": "What would you most want for your brother in his wife?",
             "choices": [
                 {"text": "A real partner — equal footing.", "score": 1.0},
                 {"text": "Someone who understands him deeply.", "score": 0.8},
                 {"text": "Someone who can keep him in line — he needs that.", "score": 0.35},
                 {"text": "Someone who makes him happier than I've seen him.", "score": 0.9}]},
            {"id": "abr_2", "topic": "Brother Spending Time with Wife",
             "question": "After your brother marries, how do you feel about him spending more time with her than family?",
             "choices": [
                 {"text": "Normal and good — that's the marriage.", "score": 1.0},
                 {"text": "As long as he doesn't disappear.", "score": 0.55},
                 {"text": "It changes things, but we adapt.", "score": 0.65},
                 {"text": "I'd hope she encourages him to stay close to family.", "score": 0.35}]},
            {"id": "abr_3", "topic": "Defending Sister-in-Law",
             "question": "If a family member speaks badly about her behind her back, what would you do?",
             "choices": [
                 {"text": "Defend her openly.", "score": 1.0},
                 {"text": "Ask them to bring it up directly instead.", "score": 0.8},
                 {"text": "Listen — sometimes there's truth in concerns.", "score": 0.35},
                 {"text": "It's not my place to take sides in family talk.", "score": 0.3}]}]},

    "ahmed_sister": {
        "label": "Ahmed's Sister", "emoji": "👧",
        "scenarios": [
            {"id": "asi_1", "topic": "Kind of Woman for Brother",
             "question": "What kind of woman would you most want to see your brother marry?",
             "choices": [
                 {"text": "Someone who has her own life — not just absorbed into his.", "score": 1.0},
                 {"text": "Someone who makes him a better version of himself.", "score": 0.8},
                 {"text": "Someone we'd all genuinely like and welcome.", "score": 0.6},
                 {"text": "Someone strong enough to handle him.", "score": 0.4}]},
            {"id": "asi_2", "topic": "Conflict with Sister-in-Law",
             "question": "If you and your sister-in-law have a disagreement, what's the right way to handle it?",
             "choices": [
                 {"text": "Direct conversation between us — no third party.", "score": 1.0},
                 {"text": "Through my brother if needed.", "score": 0.3},
                 {"text": "Time usually heals things.", "score": 0.4},
                 {"text": "We'd be expected to keep it civil — family is family.", "score": 0.55}]},
            {"id": "asi_3", "topic": "Sharing Her Brother",
             "question": "What does it feel like imagining sharing your brother with another woman?",
             "choices": [
                 {"text": "It's a good thing — he gets to build something of his own.", "score": 1.0},
                 {"text": "It's bittersweet, but natural.", "score": 0.75},
                 {"text": "I'd want to make sure she values him properly.", "score": 0.4},
                 {"text": "He was never just mine.", "score": 0.85}]}]},
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

    /* Fix expander arrow showing as text */
    [data-testid="stExpander"] summary svg {
        display: inline-block !important;
        visibility: visible !important;
    }
    /* Fix expander */
    [data-testid="stExpander"] {
        background: white !important;
        border: 1px solid #F8D7DE !important;
        border-radius: 12px !important;
        margin: 0.8rem 0 !important;
    }
    [data-testid="stExpander"] summary {
        background: white !important;
        padding: 0.8rem 1rem !important;
        border-radius: 12px !important;
    }
    [data-testid="stExpander"] summary p,
    [data-testid="stExpander"] summary span {
        color: #5C2A3E !important;
        font-weight: 600 !important;
        font-family: 'Poppins', sans-serif !important;
        font-size: 0.95rem !important;
    }
    [data-testid="stExpander"] > div {
        background: white !important;
        padding: 0.5rem 0.8rem 1rem !important;
    }
    /* Fix ALL text inside expander */
    [data-testid="stExpander"] p,
    [data-testid="stExpander"] span,
    [data-testid="stExpander"] label {
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


def render_member(member_key, expanded=True, name_a="Sara", name_b="Ahmed"):
    m = INLAW_SCENARIOS[member_key]
    resp_key = f"il_{member_key}"
    if resp_key not in st.session_state:
        st.session_state[resp_key] = {}
    responses = st.session_state[resp_key]
    done = len(responses)
    total = len(m["scenarios"])

    # Member header — use dynamic name from session state
    raw_label = m["label"]
    dyn_label = raw_label.replace("Sara", name_a).replace("Ahmed", name_b)
    st.markdown(f"""
    <div style="background:#1a0a0e; border-radius:10px; padding:0.75rem 1rem;
         margin:0.8rem 0 0.3rem; cursor:pointer;">
        <span style="color:white; font-family:'Poppins',sans-serif;
              font-weight:600; font-size:0.95rem;">
            {m['emoji']} {dyn_label}
        </span>
    </div>
    """, unsafe_allow_html=True)

    st.progress(done / total if total else 0)
    st.caption(f"{done} of {total} answered")

    if done >= total:
        score = compute_score(responses, member_key)
        color = "#6BAF73" if score >= 70 else "#E8A846" if score >= 45 else "#D4577A"
        label = "Supportive ✓" if score >= 70 else "Mixed ◐" if score >= 45 else "Friction Risk ✗"
        st.markdown(f"""
        <div style="background:{color}15; border:1px solid {color}40;
             border-radius:10px; padding:0.8rem; text-align:center; margin:0.5rem 0;">
            <span style="color:{color}; font-weight:700; font-size:1.2rem;">{score}%</span><br>
            <span style="color:{color}; font-size:0.85rem;">{label}</span>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("---")
        return score

    for sc in m["scenarios"]:
        if sc["id"] in responses:
            continue

        st.markdown(f"""
        <div class="q-tile">
            <div class="q-topic">{sc["topic"]}</div>
            <div class="q-text">{sc["question"]}</div>
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
                    f"<div style='padding-top:0.4rem; color:#3E3E3E; "
                    f"font-family:Poppins,sans-serif; font-size:0.9rem;'>"
                    f"{choice['text']}</div>",
                    unsafe_allow_html=True)
        break

    st.markdown("---")
    return compute_score(responses, member_key) if done >= total else None


def main():
    st.set_page_config(page_title="Family Profile · Zawaj",
                       page_icon="👨‍👩‍👧", layout="wide")
    page_css()

    st.markdown('<div class="page-title">Family Profile</div>', unsafe_allow_html=True)
    st.markdown('<div class="divider-gold"></div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">Both families · Member-by-member · Optional siblings</div>', unsafe_allow_html=True)

    # Read names - check all possible locations Page 1 might have saved them
    name_a = (st.session_state.get("person_a_name") or 
              st.session_state.get("names", {}).get("a") or 
              st.session_state.get("profile_a", {}).get("name") or "Sara")
    name_b = (st.session_state.get("person_b_name") or 
              st.session_state.get("names", {}).get("b") or 
              st.session_state.get("profile_b", {}).get("name") or "Ahmed")

    # Demo buttons in a clean row
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button(f"⚡ Fill {name_a}'s family", use_container_width=True):
            for mk in ["sara_mother", "sara_father", "sara_brother", "sara_sister"]:
                m = INLAW_SCENARIOS[mk]
                st.session_state[f"il_{mk}"] = {sc["id"]: 0 for sc in m["scenarios"]}
            st.rerun()
    with c2:
        if st.button(f"⚡ Fill {name_b}'s family", use_container_width=True):
            for mk in ["ahmed_mother", "ahmed_father", "ahmed_brother", "ahmed_sister"]:
                m = INLAW_SCENARIOS[mk]
                st.session_state[f"il_{mk}"] = {sc["id"]: 0 for sc in m["scenarios"]}
            st.rerun()
    with c3:
        if st.button("🔄 Reset All", use_container_width=True):
            for mk in INLAW_SCENARIOS:
                if f"il_{mk}" in st.session_state:
                    del st.session_state[f"il_{mk}"]
            st.rerun()
    st.markdown("---")

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
        render_member("sara_brother", expanded=False)
        render_member("sara_sister", expanded=False)

    with tab2:
        st.markdown(f"""
        <div class='role-intro'>
            <div class='role-title'>{name_b}'s Family</div>
            <div class='role-sub'>Profile each member individually.</div>
        </div>
        """, unsafe_allow_html=True)
        render_member("ahmed_mother", expanded=True, name_a=name_a, name_b=name_b)
        render_member("ahmed_father", expanded=False, name_a=name_a, name_b=name_b)
        render_member("ahmed_brother", expanded=False, name_a=name_a, name_b=name_b)
        render_member("ahmed_sister", expanded=False, name_a=name_a, name_b=name_b)

    with tab3:
        st.markdown(f"""
        <div class="role-intro">
            <div class="role-title">Claims vs Hopes</div>
            <div class="role-sub">What {name_b} claims about his family · What {name_a} hopes for</div>
        </div>
        """, unsafe_allow_html=True)

        CLAIMS_QS = [
            {"id": "c1", "topic": "Mother's Warmth",
             "question": f"How does {name_b} describe his mother's attitude toward a future daughter-in-law?",
             "choices": [
                 {"text": "She'll treat her like her own daughter.", "score": 1.0},
                 {"text": "She's warm but it takes time to build trust.", "score": 0.7},
                 {"text": "She's traditional but fair.", "score": 0.45},
                 {"text": "She has strong opinions about how things should be done.", "score": 0.2}]},
            {"id": "c2", "topic": "Living Arrangement",
             "question": f"What does {name_b} say about living arrangements after marriage?",
             "choices": [
                 {"text": "We'll have our own home — full independence.", "score": 1.0},
                 {"text": "We'll start together then move later.", "score": 0.65},
                 {"text": "My family expects us nearby but not necessarily together.", "score": 0.45},
                 {"text": "Joint family is expected in our culture.", "score": 0.2}]},
            {"id": "c3", "topic": "Family Involvement",
             "question": f"How does {name_b} describe his family's involvement in the couple's decisions?",
             "choices": [
                 {"text": "They give us full space — our decisions are ours.", "score": 1.0},
                 {"text": "They advise when asked, but don't interfere.", "score": 0.7},
                 {"text": "They're involved in major decisions.", "score": 0.4},
                 {"text": "Family input is expected on most things.", "score": 0.15}]},
            {"id": "c4", "topic": "Wife's Career",
             "question": f"What does {name_b} claim his family thinks about his wife working?",
             "choices": [
                 {"text": "They're fully supportive — her career is her right.", "score": 1.0},
                 {"text": "They're okay with it as long as home duties are covered.", "score": 0.6},
                 {"text": "They'd prefer she focuses on family after children.", "score": 0.35},
                 {"text": "They expect a traditional home setup.", "score": 0.1}]},
        ]

        HOPES_QS = [
            {"id": "h1", "topic": "Mother-in-Law Warmth",
             "question": f"What does {name_a} hope her mother-in-law will be like?",
             "choices": [
                 {"text": "Like a second mother — warm and welcoming.", "score": 1.0},
                 {"text": "Kind and respectful of our boundaries.", "score": 0.8},
                 {"text": "Polite and not too involved in our life.", "score": 0.5},
                 {"text": "Present for big occasions but not in daily life.", "score": 0.3}]},
            {"id": "h2", "topic": "Living Arrangement",
             "question": f"What living arrangement does {name_a} hope for after marriage?",
             "choices": [
                 {"text": "Our own home with full independence.", "score": 1.0},
                 {"text": "Close to family but separate.", "score": 0.7},
                 {"text": "Flexible — we'd figure it out together.", "score": 0.55},
                 {"text": "Joint family if everyone gets along well.", "score": 0.3}]},
            {"id": "h3", "topic": "Family Involvement",
             "question": f"How involved does {name_a} hope his family will be in their decisions?",
             "choices": [
                 {"text": "Not at all — our life is ours to decide.", "score": 1.0},
                 {"text": "Advisory — we can choose whether to listen.", "score": 0.75},
                 {"text": "Involved in major decisions with mutual respect.", "score": 0.45},
                 {"text": "I'm okay with family involvement if it's respectful.", "score": 0.4}]},
            {"id": "h4", "topic": "Career Support",
             "question": f"What does {name_a} hope his family's attitude will be about her career?",
             "choices": [
                 {"text": "Fully supportive — they'll be proud of her work.", "score": 1.0},
                 {"text": "Neutral — it's between her and her husband.", "score": 0.7},
                 {"text": "Accepting as long as family comes first.", "score": 0.4},
                 {"text": "I hope they adjust their expectations over time.", "score": 0.3}]},
        ]

        col_l, col_r = st.columns(2)

        # Claims (Ahmed)
        with col_l:
            st.markdown(f"""
            <div style="background:#1a0a0e; border-radius:10px; padding:0.75rem 1rem; margin-bottom:0.8rem;">
                <span style="color:white; font-family:'Poppins',sans-serif; font-weight:600;">
                    🤵 {name_b}'s Claims about his family
                </span>
            </div>
            """, unsafe_allow_html=True)

            resp_key_c = "il_claims"
            if resp_key_c not in st.session_state:
                st.session_state[resp_key_c] = {}
            claims = st.session_state[resp_key_c]

            for sc in CLAIMS_QS:
                if sc["id"] in claims:
                    chosen = sc["choices"][claims[sc["id"]]]["text"]
                    st.markdown(f"""
                    <div style="background:#f0fdf4; border:1px solid #86efac; border-radius:8px;
                         padding:0.6rem 0.9rem; margin-bottom:0.4rem;">
                        <div style="font-size:0.7rem; color:#16a34a; font-weight:600; margin-bottom:0.2rem;">{sc['topic']} ✓</div>
                        <div style="font-size:0.85rem; color:#3A1A2B;">{chosen}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    continue

                st.markdown(f"""
                <div class="q-tile">
                    <div class="q-topic">{sc['topic']}</div>
                    <div class="q-text">{sc['question']}</div>
                </div>
                """, unsafe_allow_html=True)
                for i, choice in enumerate(sc["choices"]):
                    col_btn, col_txt = st.columns([0.1, 0.9])
                    with col_btn:
                        if st.button(LETTERS[i], key=f"claim_{sc['id']}_{i}", type="secondary"):
                            claims[sc["id"]] = i
                            st.session_state[resp_key_c] = claims
                            st.rerun()
                    with col_txt:
                        st.markdown(f"<div style='padding-top:0.4rem;color:#3E3E3E;font-size:0.88rem;'>{choice['text']}</div>", unsafe_allow_html=True)
                break

        # Hopes (Sara)
        with col_r:
            st.markdown(f"""
            <div style="background:#3a0a1e; border-radius:10px; padding:0.75rem 1rem; margin-bottom:0.8rem;">
                <span style="color:white; font-family:'Poppins',sans-serif; font-weight:600;">
                    👰 {name_a}'s Hopes about his family
                </span>
            </div>
            """, unsafe_allow_html=True)

            resp_key_h = "il_hopes"
            if resp_key_h not in st.session_state:
                st.session_state[resp_key_h] = {}
            hopes = st.session_state[resp_key_h]

            for sc in HOPES_QS:
                if sc["id"] in hopes:
                    chosen = sc["choices"][hopes[sc["id"]]]["text"]
                    st.markdown(f"""
                    <div style="background:#fdf2f8; border:1px solid #f0abfc; border-radius:8px;
                         padding:0.6rem 0.9rem; margin-bottom:0.4rem;">
                        <div style="font-size:0.7rem; color:#a21caf; font-weight:600; margin-bottom:0.2rem;">{sc['topic']} ✓</div>
                        <div style="font-size:0.85rem; color:#3A1A2B;">{chosen}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    continue

                st.markdown(f"""
                <div class="q-tile">
                    <div class="q-topic">{sc['topic']}</div>
                    <div class="q-text">{sc['question']}</div>
                </div>
                """, unsafe_allow_html=True)
                for i, choice in enumerate(sc["choices"]):
                    col_btn, col_txt = st.columns([0.1, 0.9])
                    with col_btn:
                        if st.button(LETTERS[i], key=f"hope_{sc['id']}_{i}", type="secondary"):
                            hopes[sc["id"]] = i
                            st.session_state[resp_key_h] = hopes
                            st.rerun()
                    with col_txt:
                        st.markdown(f"<div style='padding-top:0.4rem;color:#3E3E3E;font-size:0.88rem;'>{choice['text']}</div>", unsafe_allow_html=True)
                break

        # Show alignment if both complete
        if len(claims) >= len(CLAIMS_QS) and len(hopes) >= len(HOPES_QS):
            st.markdown("---")
            claim_avg = sum(CLAIMS_QS[i]["choices"][claims[CLAIMS_QS[i]["id"]]]["score"] for i in range(len(CLAIMS_QS)) if CLAIMS_QS[i]["id"] in claims) / len(CLAIMS_QS)
            hope_avg = sum(HOPES_QS[i]["choices"][hopes[HOPES_QS[i]["id"]]]["score"] for i in range(len(HOPES_QS)) if HOPES_QS[i]["id"] in hopes) / len(HOPES_QS)
            alignment = round((claim_avg + hope_avg) / 2 * 100, 1)
            color = "#6BAF73" if alignment >= 70 else "#E8A846" if alignment >= 45 else "#D4577A"
            st.markdown(f"""
            <div style="background:white; border-radius:14px; padding:1.2rem; text-align:center;
                 border:1px solid {color}40; box-shadow:0 4px 14px {color}20;">
                <div style="font-size:0.75rem; color:#8A6B7A; letter-spacing:2px; text-transform:uppercase; font-weight:600;">Claims vs Hopes Alignment</div>
                <div style="font-family:'Playfair Display',serif; font-size:2.5rem; font-weight:700; color:{color};">{alignment}%</div>
                <div style="font-size:0.85rem; color:#8A6B7A; margin-top:0.3rem;">How well {name_b}'s claims match {name_a}'s hopes</div>
            </div>
            """, unsafe_allow_html=True)

    with tab4:
        scores = {}
        for mk, lbl in [("sara_mother", f"{name_a}'s Mother"),
                        ("sara_father", f"{name_a}'s Father"),
                        ("sara_brother", f"{name_a}'s Brother"),
                        ("sara_sister", f"{name_a}'s Sister"),
                        ("ahmed_mother", f"{name_b}'s Mother"),
                        ("ahmed_father", f"{name_b}'s Father"),
                        ("ahmed_brother", f"{name_b}'s Brother"),
                        ("ahmed_sister", f"{name_b}'s Sister")]:
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
