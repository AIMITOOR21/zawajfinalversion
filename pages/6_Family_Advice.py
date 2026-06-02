"""Page 6 — Family Compatibility Advice & Letter to the Couple."""

import streamlit as st
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
from ai.llm_client import get_llm_response


# ── Domain label map ──
DOMAIN_LABELS = {
    "career":           "Career Orientation",
    "location":         "Location & Relocation",
    "family_structure": "Family Living Structure",
    "children":         "Children",
    "roles":            "Household Roles",
    "finances":         "Financial Management",
    "religion":         "Religious Practice",
}

DOMAIN_OPTIONS = {
    "career":           ["career_focused", "balanced", "family_focused", "no_work"],
    "location":         ["stay_local", "same_city", "willing_relocate", "go_abroad"],
    "family_structure": ["joint_family", "joint_nearby", "nuclear_visits", "fully_nuclear"],
    "children":         ["no_children", "one_child", "two_children", "three_plus"],
    "roles":            ["traditional", "mostly_traditional", "egalitarian", "role_reversal"],
    "finances":         ["separate", "partial_pool", "full_pool", "spouse_manages"],
    "religion":         ["very_strict", "moderate", "liberal", "secular"],
}


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

    /* Letter card */
    .letter-card {
        background: white;
        border-radius: 20px;
        padding: 2.2rem 2.6rem;
        box-shadow: 0 8px 32px rgba(92,42,62,0.12);
        border: 1.5px solid #F8D7DE;
        position: relative;
        margin: 1rem 0 1.5rem;
    }
    .letter-card::before {
        content: '"';
        font-family: 'Playfair Display', serif;
        font-size: 8rem;
        color: #F8D7DE;
        position: absolute;
        top: -1.5rem;
        left: 1.5rem;
        line-height: 1;
    }
    .letter-text {
        font-family: 'Poppins', sans-serif;
        font-size: 1rem;
        color: #3A1A2B;
        line-height: 1.9;
        white-space: pre-wrap;
    }
    .letter-sig {
        font-family: 'Playfair Display', serif;
        font-size: 1rem;
        color: #8A6B7A;
        font-style: italic;
        margin-top: 1.2rem;
        text-align: right;
    }

    /* Advice cards */
    .advice-section-header {
        background: #1a0a0e;
        border-radius: 12px;
        padding: 0.9rem 1.3rem;
        margin: 1.2rem 0 0.8rem;
    }
    .advice-section-header span {
        color: white;
        font-family: 'Playfair Display', serif;
        font-size: 1.1rem;
        font-weight: 600;
    }
    .advice-section-header small {
        color: #C9A96E;
        font-family: 'Poppins', sans-serif;
        font-size: 0.8rem;
        display: block;
        margin-top: 0.2rem;
    }

    .advice-card {
        background: white;
        border-radius: 14px;
        padding: 1.2rem 1.4rem;
        margin-bottom: 0.8rem;
        box-shadow: 0 3px 10px rgba(212,87,122,0.08);
        border-left: 4px solid #D4577A;
    }
    .advice-card-green { border-left-color: #6BAF73; }
    .advice-card-gold  { border-left-color: #C9A96E; }
    .advice-card-blue  { border-left-color: #1A5C8B; }

    .advice-topic {
        font-size: 0.7rem; font-weight: 600;
        letter-spacing: 2px; text-transform: uppercase;
        color: #D4577A; margin-bottom: 0.35rem;
    }
    .advice-topic-green { color: #6BAF73; }
    .advice-topic-gold  { color: #C9A96E; }
    .advice-topic-blue  { color: #1A5C8B; }

    .advice-title {
        font-family: 'Playfair Display', serif;
        font-size: 1rem; font-weight: 700;
        color: #3A1A2B; margin-bottom: 0.4rem;
    }
    .advice-body {
        font-family: 'Poppins', sans-serif;
        font-size: 0.88rem; color: #5A3A4A;
        line-height: 1.65;
    }

    .score-pill {
        display: inline-block;
        padding: 0.2rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    .conversation-card {
        background: linear-gradient(135deg, #FDEEF2, #FFFFFF);
        border: 1px solid #F8D7DE;
        border-radius: 12px;
        padding: 1rem 1.2rem;
        margin-bottom: 0.6rem;
    }
    .conversation-q {
        font-family: 'Playfair Display', serif;
        font-size: 0.95rem;
        color: #5C2A3E;
        font-style: italic;
    }

    .stButton > button {
        background: linear-gradient(135deg, #5C2A3E, #D4577A) !important;
        color: white !important; border: none !important;
        border-radius: 50px !important;
        font-family: 'Poppins', sans-serif !important;
        font-weight: 500 !important;
        padding: 0.65rem 2.2rem !important;
        box-shadow: 0 4px 14px rgba(212,87,122,0.3) !important;
    }

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(16px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    </style>
    """, unsafe_allow_html=True)


def score_color(s):
    return "#6BAF73" if s >= 70 else "#E8A846" if s >= 45 else "#D4577A"


def score_label(s):
    return "Strong" if s >= 70 else "Moderate" if s >= 45 else "Needs Attention"


def build_domain_gap_list(person_a, person_b, domain_scores, name_a, name_b):
    """Return list of (domain, score, val_a, val_b) sorted by score asc."""
    gaps = []
    for domain, score in domain_scores.items():
        val_a = str(person_a.get(domain, "N/A")).replace("_", " ")
        val_b = str(person_b.get(domain, "N/A")).replace("_", " ")
        gaps.append((DOMAIN_LABELS.get(domain, domain), score, val_a, val_b))
    gaps.sort(key=lambda x: x[1])
    return gaps


def generate_letter(name_a, name_b, results, domain_gaps,
                    inlaw_girl, inlaw_boy, honesty_score,
                    conflicts, used_real_api_ref):
    """Generate the personal letter via LLM."""

    final = results["final_score"]
    label = results["label"]
    top_gaps = [g for g in domain_gaps if g[1] < 70][:3]
    top_strengths = [g for g in reversed(domain_gaps) if g[1] >= 70][:2]

    gap_text = "\n".join(
        f"- {g[0]}: {name_a} prefers '{g[2]}', {name_b} prefers '{g[3]}' (alignment: {g[1]:.0f}%)"
        for g in top_gaps
    ) or "None significant"

    strength_text = "\n".join(
        f"- {g[0]}: both aligned at {g[1]:.0f}%"
        for g in top_strengths
    ) or "Still building"

    honesty_line = ""
    if honesty_score is not None:
        if honesty_score < 55:
            honesty_line = f"There is also a notable gap ({honesty_score:.0f}%) between what {name_b} has described about his family and what his family members actually indicated — this warrants an honest conversation."
        elif honesty_score < 70:
            honesty_line = f"Some gaps exist between {name_b}'s description of his family and their actual responses ({honesty_score:.0f}% alignment) — worth clarifying before committing."

    inlaw_line = ""
    if inlaw_boy is not None:
        if inlaw_boy < 55:
            inlaw_line = f"{name_b}'s family compatibility for {name_a} scores {inlaw_boy:.0f}% — there are real expectations to discuss openly."
        elif inlaw_boy >= 70:
            inlaw_line = f"{name_b}'s family appears largely compatible with what {name_a} is looking for ({inlaw_boy:.0f}%)."

    system_prompt = """You are a warm, wise, and culturally sensitive marriage counselor writing a personal letter to a Pakistani couple considering marriage.
Your tone is like a trusted elder — honest but kind, direct but respectful.
You write in English. You never use bullet points. Write in flowing paragraphs.
You are not dramatic. You do not exaggerate. You speak plainly about real things.
Do not use generic phrases like 'journey' or 'embark'. Be specific to their actual data."""

    prompt = f"""Write a personal letter to {name_a} and {name_b} based on their compatibility assessment.

Overall Score: {final:.1f}% ({label})

Their key mismatches (lowest scoring areas):
{gap_text}

Their key strengths (highest scoring areas):
{strength_text}

Family context:
{name_a}'s family readiness: {f"{inlaw_girl:.0f}%" if inlaw_girl else "not assessed"}
{name_b}'s family fit for {name_a}: {f"{inlaw_boy:.0f}%" if inlaw_boy else "not assessed"}
{honesty_line}
{inlaw_line}

Write 3 paragraphs:
1. Open warmly using their names, acknowledge their score honestly — neither dismiss it nor catastrophize it.
2. Name the 1-2 most important things they need to talk about before moving forward. Be specific about what exactly to discuss.
3. Close with a genuine, grounded encouragement — not a cliché. Something real.

Do not use bullet points. Do not use headers. Write as a letter."""

    response, used_real = get_llm_response(prompt, system_prompt, temperature=0.65, max_tokens=600)
    used_real_api_ref.append(used_real)
    return response


def generate_family_advice(name_a, name_b, inlaw_girl, inlaw_boy,
                           honesty_score, claims_avg, hopes_avg):
    """Generate specific family compatibility advice via LLM."""

    system_prompt = """You are a culturally sensitive Pakistani marriage counselor.
Give concrete, specific advice about family dynamics. Be direct. No bullet points — write in short paragraphs per topic.
Respect Pakistani cultural norms while encouraging healthy boundaries."""

    sections = []
    if inlaw_girl is not None:
        sections.append(f"- {name_a}'s own family readiness score: {inlaw_girl:.0f}%")
    if inlaw_boy is not None:
        sections.append(f"- {name_b}'s family fit for {name_a}: {inlaw_boy:.0f}%")
    if honesty_score is not None:
        sections.append(f"- Honesty score (how well {name_b}'s claims about his family match reality): {honesty_score:.0f}%")
        sections.append(f"  ({name_b}'s claims scored {claims_avg:.0f}%, {name_a}'s hopes scored {hopes_avg:.0f}%)")

    data_block = "\n".join(sections) if sections else "Family data not yet complete."

    prompt = f"""Based on this family compatibility data for {name_a} and {name_b}:

{data_block}

Write 3 short advice sections (one paragraph each, with a bold heading):

1. **For {name_a}** — What should she specifically watch for or clarify about {name_b}'s family before committing? Be honest if the honesty score is low.
2. **For {name_b}** — What expectations does he need to set clearly with his own family to protect the marriage?
3. **For both families** — What conversation should the two families have before the wedding to prevent friction later?

Be specific. Name real topics (living arrangements, career support, visits to {name_a}'s parents, financial expectations). Do not be vague."""

    response, _ = get_llm_response(prompt, system_prompt, temperature=0.6, max_tokens=700)
    return response


def generate_domain_advice(name_a, name_b, domain_gaps):
    """Generate targeted advice for the weakest domains."""
    weak = [g for g in domain_gaps if g[1] < 65][:4]
    if not weak:
        return None

    lines = "\n".join(
        f"- {g[0]}: {name_a} prefers '{g[2]}', {name_b} prefers '{g[3]}' — {g[1]:.0f}% aligned"
        for g in weak
    )

    system_prompt = """You are a practical Pakistani marriage counselor.
For each mismatch, give one concrete action or conversation the couple can take.
Write in short tight paragraphs. Use bold headings for each domain. No bullet points inside paragraphs."""

    prompt = f"""These are the weakest compatibility areas for {name_a} and {name_b}:

{lines}

For each area, write one short paragraph (3-4 sentences) with a bold heading like **Career Orientation**.
Tell them exactly what to discuss and what a reasonable compromise might look like in a Pakistani family context.
Be specific. Be direct."""

    response, _ = get_llm_response(prompt, system_prompt, temperature=0.6, max_tokens=700)
    return response


def render_score_snapshot(name_a, name_b, results, inlaw_girl, inlaw_boy, honesty_score):
    """Small summary bar at top of page."""
    final = results["final_score"]
    col1, col2, col3, col4 = st.columns(4)

    def mini(label, val, pending=""):
        if val is not None:
            c = score_color(val)
            return f"""<div style="background:white;border-radius:12px;padding:0.9rem 1rem;
                     border-top:3px solid {c};box-shadow:0 2px 8px rgba(212,87,122,0.08);">
                <div style="font-size:0.7rem;color:#8A6B7A;letter-spacing:1.5px;
                     text-transform:uppercase;font-weight:600;">{label}</div>
                <div style="font-family:'Playfair Display',serif;font-size:1.8rem;
                     font-weight:700;color:{c};">{val:.1f}%</div>
            </div>"""
        return f"""<div style="background:white;border-radius:12px;padding:0.9rem 1rem;
                 border-top:3px solid #E0C8D0;box-shadow:0 2px 8px rgba(212,87,122,0.04);">
            <div style="font-size:0.7rem;color:#8A6B7A;letter-spacing:1.5px;
                 text-transform:uppercase;font-weight:600;">{label}</div>
            <div style="font-size:0.8rem;color:#C9A96E;margin-top:0.3rem;">{pending}</div>
        </div>"""

    with col1:
        st.markdown(mini("Overall", final), unsafe_allow_html=True)
    with col2:
        st.markdown(mini(f"{name_a}'s Family", inlaw_girl, "Not assessed"), unsafe_allow_html=True)
    with col3:
        st.markdown(mini(f"{name_b}'s Family Fit", inlaw_boy, "Not assessed"), unsafe_allow_html=True)
    with col4:
        st.markdown(mini(f"{name_b}'s Honesty", honesty_score, "Not assessed"), unsafe_allow_html=True)


def main():
    st.set_page_config(page_title="Family Advice · Zawaj", page_icon="💌", layout="wide")
    page_css()

    st.markdown('<p class="page-title">💌 Advice & Letter to the Couple</p>', unsafe_allow_html=True)
    st.markdown('<div class="divider-gold"></div>', unsafe_allow_html=True)
    st.markdown('<p class="page-sub">Personalised family compatibility advice — and a letter written just for you</p>', unsafe_allow_html=True)

    # ── Guard: need results ──
    person_a = st.session_state.get("person_a") or st.session_state.get("profile_a")
    person_b = st.session_state.get("person_b") or st.session_state.get("profile_b")
    results  = st.session_state.get("results")

    if not person_a or not person_b or not results:
        st.warning("⚠️ Please complete the Scenario Assessment and view the Results Dashboard first.")
        st.info("Path: Scenario Assessment → In-Laws Questionnaire → Results Dashboard → come here.")
        st.stop()

    name_a = st.session_state.get("person_a_name") or person_a.get("name", "Sara")
    name_b = st.session_state.get("person_b_name") or person_b.get("name", "Ahmed")

    domain_scores  = st.session_state.get("domain_scores", {})
    conflicts      = st.session_state.get("conflicts", [])
    inlaw_girl     = st.session_state.get("inlaw_girl_score")
    inlaw_boy      = st.session_state.get("inlaw_boy_score")
    honesty_score  = st.session_state.get("inlaw_honesty_score")
    claims_avg     = st.session_state.get("claims_avg", 0)
    hopes_avg      = st.session_state.get("hopes_avg", 0)

    domain_gaps = build_domain_gap_list(person_a, person_b, domain_scores, name_a, name_b)

    # ── Score snapshot ──
    st.markdown("<br>", unsafe_allow_html=True)
    render_score_snapshot(name_a, name_b, results, inlaw_girl, inlaw_boy, honesty_score)
    st.markdown("<br>", unsafe_allow_html=True)

    # ── Generate button ──
    if "advice_generated" not in st.session_state:
        st.session_state.advice_generated = False

    col_btn, _ = st.columns([1, 2])
    with col_btn:
        if st.button("✨ Generate Personalised Advice & Letter", use_container_width=True):
            with st.spinner("Writing your personalised advice..."):
                used_real_ref = []

                letter = generate_letter(
                    name_a, name_b, results, domain_gaps,
                    inlaw_girl, inlaw_boy, honesty_score,
                    conflicts, used_real_ref
                )
                family_advice = generate_family_advice(
                    name_a, name_b, inlaw_girl, inlaw_boy,
                    honesty_score, claims_avg, hopes_avg
                )
                domain_advice = generate_domain_advice(name_a, name_b, domain_gaps)

                st.session_state["advice_letter"]        = letter
                st.session_state["advice_family"]        = family_advice
                st.session_state["advice_domain"]        = domain_advice
                st.session_state["advice_used_real_api"] = used_real_ref[0] if used_real_ref else False
                st.session_state.advice_generated        = True
            st.rerun()

    if not st.session_state.advice_generated:
        st.markdown("""
        <div style="background:white;border-radius:14px;padding:1.4rem 1.6rem;
             border:1px solid #F8D7DE;color:#8A6B7A;font-size:0.9rem;margin-top:1rem;">
            Click the button above to generate personalised advice based on all scores —
            partner compatibility, family dynamics, and the honesty gap.
            This uses AI and takes about 10 seconds.
        </div>
        """, unsafe_allow_html=True)
        st.stop()

    # ── Letter ──
    letter       = st.session_state.get("advice_letter", "")
    family_adv   = st.session_state.get("advice_family", "")
    domain_adv   = st.session_state.get("advice_domain", "")
    used_real    = st.session_state.get("advice_used_real_api", False)

    api_badge = ("🟢 Written by AI" if used_real
                 else "🟡 Written using built-in templates (no API key configured)")

    st.markdown(f"""
    <div class="advice-section-header">
        <span>💌 A Letter to {name_a} & {name_b}</span>
        <small>{api_badge}</small>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="letter-card">
        <div class="letter-text">{letter}</div>
        <div class="letter-sig">— Zawaj Compatibility System</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Family Advice ──
    has_family_data = any(x is not None for x in [inlaw_girl, inlaw_boy, honesty_score])
    if has_family_data and family_adv:
        st.markdown(f"""
        <div class="advice-section-header">
            <span>👨‍👩‍👧 Family Compatibility Advice</span>
            <small>Based on in-law questionnaire scores</small>
        </div>
        """, unsafe_allow_html=True)

        # Score pills
        pcol1, pcol2, pcol3 = st.columns(3)
        with pcol1:
            if inlaw_girl is not None:
                c = score_color(inlaw_girl)
                st.markdown(f"<span class='score-pill' style='background:{c}20;color:{c};border:1px solid {c}40;'>{name_a}'s Family: {inlaw_girl:.0f}% — {score_label(inlaw_girl)}</span>", unsafe_allow_html=True)
        with pcol2:
            if inlaw_boy is not None:
                c = score_color(inlaw_boy)
                st.markdown(f"<span class='score-pill' style='background:{c}20;color:{c};border:1px solid {c}40;'>{name_b}'s Family Fit: {inlaw_boy:.0f}% — {score_label(inlaw_boy)}</span>", unsafe_allow_html=True)
        with pcol3:
            if honesty_score is not None:
                c = score_color(honesty_score)
                st.markdown(f"<span class='score-pill' style='background:{c}20;color:{c};border:1px solid {c}40;'>Honesty Score: {honesty_score:.0f}% — {score_label(honesty_score)}</span>", unsafe_allow_html=True)

        st.markdown(f"""
        <div class="advice-card advice-card-blue">
            <div class="advice-topic advice-topic-blue">Family Dynamics</div>
            <div class="advice-body">{family_adv.replace(chr(10), '<br>')}</div>
        </div>
        """, unsafe_allow_html=True)

    # ── Honesty gap alert ──
    if honesty_score is not None and honesty_score < 60:
        gap = claims_avg - hopes_avg if claims_avg and hopes_avg else None
        st.markdown(f"""
        <div style="background:#FFF3CD;border:1px solid #FFC107;border-radius:12px;
             padding:1rem 1.3rem;margin:0.5rem 0;">
            <div style="font-weight:600;color:#856404;font-size:0.9rem;">
                ⚠️ Honesty Gap Alert — {name_b}'s claims vs his family's actual answers: {honesty_score:.0f}%
            </div>
            <div style="color:#664D03;font-size:0.85rem;margin-top:0.4rem;">
                {name_b} described his family in a way that doesn't fully match what they said.
                Before moving forward, {name_a} should verify these topics directly with {name_b}'s family:
                living arrangements, career support, and family involvement in daily decisions.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ── Domain Advice ──
    weak_domains = [g for g in domain_gaps if g[1] < 65]
    if weak_domains and domain_adv:
        st.markdown(f"""
        <div class="advice-section-header">
            <span>🎯 Where to Focus — Lowest Scoring Areas</span>
            <small>{len(weak_domains)} domains below 65% alignment</small>
        </div>
        """, unsafe_allow_html=True)

        # Show the gaps as pills first
        gap_cols = st.columns(min(len(weak_domains), 4))
        for i, g in enumerate(weak_domains[:4]):
            c = score_color(g[1])
            with gap_cols[i]:
                st.markdown(f"""
                <div style="background:{c}12;border:1px solid {c}40;border-radius:10px;
                     padding:0.6rem 0.8rem;margin-bottom:0.6rem;">
                    <div style="font-size:0.68rem;color:#8A6B7A;letter-spacing:1.5px;
                         text-transform:uppercase;font-weight:600;">{g[0]}</div>
                    <div style="font-weight:700;color:{c};font-size:1.1rem;">{g[1]:.0f}%</div>
                    <div style="font-size:0.75rem;color:#5A3A4A;">{name_a}: {g[2]}</div>
                    <div style="font-size:0.75rem;color:#5A3A4A;">{name_b}: {g[3]}</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="advice-card advice-card-gold">
            <div class="advice-topic advice-topic-gold">Actionable Guidance</div>
            <div class="advice-body">{domain_adv.replace(chr(10), '<br>')}</div>
        </div>
        """, unsafe_allow_html=True)

    # ── Conversation starters ──
    st.markdown(f"""
    <div class="advice-section-header">
        <span>💬 Conversation Starters</span>
        <small>Questions {name_a} and {name_b} should ask each other — and their families</small>
    </div>
    """, unsafe_allow_html=True)

    starters = []

    # Domain-based starters
    for g in domain_gaps[:3]:
        if g[1] < 70:
            starters.append((
                f"On {g[0]}",
                f"We currently see this differently — you lean toward '{g[3]}' and I lean toward '{g[2]}'. "
                f"Can we talk about what a workable middle ground looks like for us specifically?"
            ))

    # Honesty gap starter
    if honesty_score is not None and honesty_score < 70:
        starters.append((
            f"For {name_b} to ask his family",
            f"I want us to have an honest conversation about what your expectations are for my wife — "
            f"around living arrangements, her career, and her relationship with her own parents. "
            f"I need to make sure what I've told her matches what you actually expect."
        ))

    # Family starter for Sara
    if inlaw_boy is not None and inlaw_boy < 70:
        starters.append((
            f"For {name_a} to ask {name_b}",
            f"Your family scored {inlaw_boy:.0f}% fit for what I'm looking for. "
            f"Can we sit down specifically and talk about living arrangements and how involved your family expects to be in our daily decisions?"
        ))

    # Always add one general
    starters.append((
        "For both",
        "What does a good marriage look like to each of us — not in theory, but in the daily routine? "
        "Who handles what, how do we make big decisions, and how do we handle it when our families disagree with us?"
    ))

    for topic, question in starters[:5]:
        st.markdown(f"""
        <div class="conversation-card">
            <div style="font-size:0.7rem;color:#C9A96E;letter-spacing:2px;
                 text-transform:uppercase;font-weight:600;margin-bottom:0.35rem;">{topic}</div>
            <div class="conversation-q">"{question}"</div>
        </div>
        """, unsafe_allow_html=True)

    # ── Regenerate button ──
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 Regenerate Advice", key="regen_btn"):
        for k in ["advice_letter", "advice_family", "advice_domain", "advice_generated"]:
            if k in st.session_state:
                del st.session_state[k]
        st.rerun()


main()
