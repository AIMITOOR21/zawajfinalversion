"""Page 2 — In-Laws Questionnaire."""

import streamlit as st
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

INLAW_SCENARIOS = {
    "sara_mother": {
        "label": "Sara's Mother",
        "side": "Sara's side",
        "scenarios": [
            {"id": "sm_1", "topic": "Describing her ideal son-in-law",
             "question": "When you imagine the kind of man you'd want for your daughter, what comes to mind first?",
             "choices": [
                 {"text": "Someone she chooses for herself, that she can build a life with.", "score": 1.0},
                 {"text": "A man from a good, respectable family — with steady prospects.", "score": 0.45},
                 {"text": "Someone who would treat her well and adjust to our family's rhythm.", "score": 0.4},
                 {"text": "A man with character. Money and background are secondary.", "score": 0.7}]},
            {"id": "sm_2", "topic": "Most important quality",
             "question": "If you had to name the single most important quality in a son-in-law, what would it be?",
             "choices": [
                 {"text": "That my daughter feels respected by him.", "score": 1.0},
                 {"text": "That he comes from people we know and trust.", "score": 0.35},
                 {"text": "That he listens — to her, to us, to wisdom.", "score": 0.5},
                 {"text": "That he can stand on his own — emotionally, financially, socially.", "score": 0.7}]},
            {"id": "sm_3", "topic": "Relationship with son-in-law",
             "question": "What kind of relationship would you ideally have with your daughter's husband?",
             "choices": [
                 {"text": "Close, like a son — someone we'd both support.", "score": 0.9},
                 {"text": "Respectful — we don't need to be close, just kind.", "score": 0.65},
                 {"text": "I'd want him to come to us when things get difficult.", "score": 0.4},
                 {"text": "Whatever feels natural. Some sons-in-law are close, some aren't.", "score": 0.5}]},
            {"id": "sm_4", "topic": "What would make her hesitate",
             "question": "What would make you most uncomfortable about a potential son-in-law?",
             "choices": [
                 {"text": "If my daughter seemed unsure about him, even slightly.", "score": 1.0},
                 {"text": "If his family had a reputation we weren't sure of.", "score": 0.35},
                 {"text": "If he seemed the kind to dominate or shut her down.", "score": 0.8},
                 {"text": "If he was too independent — too much his own person.", "score": 0.2}]},
            {"id": "sm_5", "topic": "Quiet hope",
             "question": "What's the quiet hope you carry about your daughter's eventual marriage?",
             "choices": [
                 {"text": "That she stays herself — that marriage adds to her, doesn't shrink her.", "score": 1.0},
                 {"text": "That she's well-settled and never has to worry.", "score": 0.55},
                 {"text": "That she doesn't drift too far from us.", "score": 0.4},
                 {"text": "That her husband becomes part of our family, fully.", "score": 0.5}]}
        ]
    },
    "sara_father": {
        "label": "Sara's Father",
        "side": "Sara's side",
        "scenarios": [
            {"id": "sf_1", "topic": "Son-in-law's role",
             "question": "What's the most important thing for a son-in-law to be for your daughter?",
             "choices": [
                 {"text": "A partner — someone who walks beside her, not ahead of her.", "score": 1.0},
                 {"text": "A protector — financially, socially, in every way.", "score": 0.5},
                 {"text": "A steady presence — someone who keeps her grounded.", "score": 0.45},
                 {"text": "Someone who genuinely values what she brings.", "score": 0.8}]},
            {"id": "sf_2", "topic": "Handling disagreements",
             "question": "How should a son-in-law handle a disagreement with your daughter?",
             "choices": [
                 {"text": "Talk to her directly until they understand each other.", "score": 1.0},
                 {"text": "Know when to walk away and revisit later.", "score": 0.55},
                 {"text": "Be the calmer one — someone has to be.", "score": 0.5},
                 {"text": "Bring it to the family if they can't resolve it.", "score": 0.2}]},
            {"id": "sf_3", "topic": "Financial expectations",
             "question": "What do you expect from a son-in-law financially?",
             "choices": [
                 {"text": "That he and my daughter handle finances together as they see fit.", "score": 1.0},
                 {"text": "That he's stable and able to provide for the household.", "score": 0.6},
                 {"text": "That he's transparent — no surprises.", "score": 0.65},
                 {"text": "That my daughter never has to worry about money.", "score": 0.5}]},
            {"id": "sf_4", "topic": "Authority dynamic",
             "question": "Do you see a son-in-law as someone who should defer to elders, or have his own standing?",
             "choices": [
                 {"text": "His own standing. He's not our subordinate.", "score": 1.0},
                 {"text": "Both — respect for elders, but his decisions are his.", "score": 0.7},
                 {"text": "He should listen — that's how a young man matures.", "score": 0.3},
                 {"text": "It depends on his family's culture. We'd adapt.", "score": 0.55}]},
            {"id": "sf_5", "topic": "Private worry",
             "question": "What's your private worry about your daughter's future husband?",
             "choices": [
                 {"text": "That he won't show up for her when she's struggling.", "score": 1.0},
                 {"text": "That his family will pull him away from her.", "score": 0.4},
                 {"text": "That she'll soften too much for him — lose her edge.", "score": 0.5},
                 {"text": "I don't worry. She's strong enough to choose well.", "score": 0.7}]}
        ]
    },
    "ahmed_mother": {
        "label": "Ahmed's Mother",
        "side": "Ahmed's side",
        "scenarios": [
            {"id": "am_1", "topic": "Daughter-in-law's place",
             "question": "How do you see a daughter-in-law in your home?",
             "choices": [
                 {"text": "As my son's wife — her home is the one she builds with him.", "score": 1.0},
                 {"text": "As a daughter — fully part of the family from day one.", "score": 0.75},
                 {"text": "As family, with time. Trust is built.", "score": 0.5},
                 {"text": "Someone who'll bring her own ways and we'll find a rhythm.", "score": 0.85}]},
            {"id": "am_2", "topic": "Her career",
             "question": "What's your view on a daughter-in-law continuing her career after marriage?",
             "choices": [
                 {"text": "Her decision entirely.", "score": 1.0},
                 {"text": "Of course — we're a modern family.", "score": 0.7},
                 {"text": "As long as the home doesn't suffer for it.", "score": 0.35},
                 {"text": "It's between her and my son.", "score": 0.5}]},
            {"id": "am_3", "topic": "What to call her",
             "question": "What would you ideally want your daughter-in-law to call you?",
             "choices": [
                 {"text": "Whatever she's comfortable with.", "score": 1.0},
                 {"text": "Mama, like a daughter.", "score": 0.6},
                 {"text": "Aunty initially — Mama if she comes to feel that way.", "score": 0.75},
                 {"text": "It's not the word, it's the relationship.", "score": 0.85}]},
            {"id": "am_4", "topic": "Her family relationship",
             "question": "What's your view on her relationship with her own parents after marriage?",
             "choices": [
                 {"text": "They raised her. She should be with them often.", "score": 1.0},
                 {"text": "Of course she'll see them. Balance is key.", "score": 0.6},
                 {"text": "They're family too — we'd visit together.", "score": 0.5},
                 {"text": "It'll adjust naturally over time.", "score": 0.3}]},
            {"id": "am_5", "topic": "Quiet hope",
             "question": "What's your quiet hope about the woman who'll marry your son?",
             "choices": [
                 {"text": "That she's happy with him. That's the foundation of everything.", "score": 1.0},
                 {"text": "That she fits well into our family.", "score": 0.4},
                 {"text": "That she makes him a better man.", "score": 0.6},
                 {"text": "That she has the patience for a long marriage.", "score": 0.35}]}
        ]
    },
    "ahmed_father": {
        "label": "Ahmed's Father",
        "side": "Ahmed's side",
        "scenarios": [
            {"id": "af_1", "topic": "What he wants",
             "question": "What do you most want from your daughter-in-law?",
             "choices": [
                 {"text": "That she's good to my son and finds happiness with him.", "score": 1.0},
                 {"text": "That she respects the family and we respect her.", "score": 0.7},
                 {"text": "That she's the kind of woman my son needs.", "score": 0.45},
                 {"text": "That she contributes to the home in her own way.", "score": 0.55}]},
            {"id": "af_2", "topic": "Her independence",
             "question": "How do you feel about a daughter-in-law who has strong opinions?",
             "choices": [
                 {"text": "Good — a thinking woman is a good partner.", "score": 1.0},
                 {"text": "Fine, as long as there's respect when she disagrees.", "score": 0.65},
                 {"text": "As long as she knows when to listen.", "score": 0.35},
                 {"text": "My son needs that. He's stubborn — she'll balance him.", "score": 0.6}]},
            {"id": "af_3", "topic": "Conflict between wife and daughter-in-law",
             "question": "If there's ever friction between your wife and your daughter-in-law, what's your role?",
             "choices": [
                 {"text": "Let them work it out unless it becomes serious.", "score": 0.7},
                 {"text": "Quietly support my wife — she's been here longer.", "score": 0.2},
                 {"text": "Hear both sides honestly.", "score": 1.0},
                 {"text": "Ask my son to manage it.", "score": 0.3}]},
            {"id": "af_4", "topic": "Her finances",
             "question": "Should a daughter-in-law contribute financially to the household?",
             "choices": [
                 {"text": "If she earns, she decides what to do with it.", "score": 1.0},
                 {"text": "Only if she wants to — no obligation.", "score": 0.7},
                 {"text": "It's expected — we all contribute.", "score": 0.4},
                 {"text": "That's between her and my son.", "score": 0.55}]},
            {"id": "af_5", "topic": "Long-term relationship",
             "question": "In 10 years, how do you imagine your relationship with your daughter-in-law?",
             "choices": [
                 {"text": "Like a daughter — fully family by then.", "score": 0.85},
                 {"text": "Close, but with her own household.", "score": 1.0},
                 {"text": "Respectful, depending on how she's been with us.", "score": 0.3},
                 {"text": "It'll be what it'll be. I don't predict.", "score": 0.5}]}
        ]
    },
}


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

    st.markdown(f"### {m['label']} ({m['side']})")
    st.progress(done / total)
    st.caption(f"{done}/{total} answered")

    if done >= total:
        score = compute_score(responses, member_key)
        color = "green" if score >= 70 else "orange" if score >= 45 else "red"
        label = "Supportive" if score >= 70 else "Mixed" if score >= 45 else "Friction Risk"
        st.success(f"Complete! Score: {score}% — {label}")
        return score

    for sc in m["scenarios"]:
        sid = sc["id"]
        if sid in responses:
            continue
        st.info(f"**{sc['topic']}**\n\n{sc['question']}")
        opts = [c["text"] for c in sc["choices"]]
        sel = st.radio("Choose:", opts, key=f"radio_{sid}", index=None)
        if sel is not None:
            idx = opts.index(sel)
            responses[sid] = idx
            st.session_state[resp_key] = responses
            st.rerun()
        break

    return None


def main():
    st.set_page_config(page_title="Zawaj — Family", page_icon="🏠", layout="centered")

    st.title("Family Compatibility Assessment")
    st.caption("Pre-marriage family values · Member-by-member · Both sides")

    # Demo mode
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Auto-fill Sara's family", use_container_width=True):
            for mk in ["sara_mother", "sara_father"]:
                m = INLAW_SCENARIOS[mk]
                resp_key = f"il_{mk}"
                st.session_state[resp_key] = {sc["id"]: 0 for sc in m["scenarios"]}
            st.rerun()
    with col2:
        if st.button("Auto-fill Ahmed's family", use_container_width=True):
            for mk in ["ahmed_mother", "ahmed_father"]:
                m = INLAW_SCENARIOS[mk]
                resp_key = f"il_{mk}"
                st.session_state[resp_key] = {sc["id"]: 0 for sc in m["scenarios"]}
            st.rerun()
    with col3:
        if st.button("Reset All", use_container_width=True):
            for mk in INLAW_SCENARIOS:
                if f"il_{mk}" in st.session_state:
                    del st.session_state[f"il_{mk}"]
            st.rerun()

    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(["Sara's Family", "Ahmed's Family", "Combined Score"])

    with tab1:
        st.subheader("Sara's family expectations of her future husband")
        sm = render_member("sara_mother")
        st.markdown("---")
        sf = render_member("sara_father")

    with tab2:
        st.subheader("Ahmed's family expectations of his future wife")
        am = render_member("ahmed_mother")
        st.markdown("---")
        af = render_member("ahmed_father")

    with tab3:
        scores = []
        labels = []
        for mk, label in [("sara_mother", "Sara's Mother"), ("sara_father", "Sara's Father"),
                          ("ahmed_mother", "Ahmed's Mother"), ("ahmed_father", "Ahmed's Father")]:
            resp_key = f"il_{mk}"
            if resp_key in st.session_state:
                s = compute_score(st.session_state[resp_key], mk)
                if s is not None:
                    scores.append(s)
                    labels.append(label)
                    st.metric(label, f"{s}%")

        if scores:
            combined = round(sum(scores) / len(scores), 1)
            st.markdown("---")
            verdict = "Strong Family Alignment" if combined >= 70 else "Moderate — Discuss Key Areas" if combined >= 45 else "Significant Friction — Open Conversations Needed"
            st.metric("Combined Family Score", f"{combined}%", delta=verdict)
            st.session_state["inlaw_score"] = combined
            st.session_state["inlaws_complete"] = True
            st.success("Family assessment saved! Go to Results Dashboard.")
        else:
            st.info("Complete family assessments to see combined score.")


main()
