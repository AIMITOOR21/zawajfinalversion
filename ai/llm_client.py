"""LLM client — Google Gemini API with fallback to mock responses."""

import os
import json
from pathlib import Path

# Try loading .env for local dev
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Read API key from environment (set in Streamlit Cloud secrets or .env)
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")

_gemini_client = None

def _get_client():
    global _gemini_client
    if _gemini_client is not None:
        return _gemini_client
    if not GEMINI_API_KEY:
        return None
    try:
        import google.generativeai as genai
        genai.configure(api_key=GEMINI_API_KEY)
        _gemini_client = genai.GenerativeModel("gemini-1.5-flash")
        return _gemini_client
    except Exception as e:
        print(f"Gemini init error: {e}")
        return None


def call_llm(prompt: str, max_tokens: int = 800) -> str:
    """Call Gemini API. Falls back to mock if key not available."""
    client = _get_client()
    if client is None:
        return _mock_response(prompt)
    try:
        response = client.generate_content(
            prompt,
            generation_config={"max_output_tokens": max_tokens, "temperature": 0.8}
        )
        return response.text.strip()
    except Exception as e:
        print(f"Gemini API error: {e}")
        return _mock_response(prompt)


def _mock_response(prompt: str) -> str:
    """Intelligent mock responses based on prompt context."""
    p = prompt.lower()
    if "conflict" in p or "simulation" in p or "disagree" in p:
        return (
            "In this scenario, the couple faces a meaningful difference in expectations. "
            "Sara tends to approach the situation with an emphasis on open communication and "
            "finding common ground, while Ahmed's background leads him to balance personal goals "
            "with family expectations. The key friction point centres on timing and compromise — "
            "both partners would benefit from a structured conversation where each outlines their "
            "core priorities. Research in relationship psychology suggests that couples who name "
            "their underlying needs (rather than positions) resolve these tensions far more effectively. "
            "Resolution probability improves significantly when both partners practice active listening "
            "and treat the disagreement as a shared problem rather than a competition."
        )
    elif "improvement" in p or "plan" in p or "advice" in p:
        return (
            "**Personalised Improvement Plan**\n\n"
            "Based on the compatibility assessment, here are the most impactful steps:\n\n"
            "1. **Schedule a values conversation** — Set aside uninterrupted time to discuss your top three "
            "non-negotiables in the areas where alignment was lower. Use 'I need' language rather than 'you should'.\n\n"
            "2. **Family alignment session** — Invite a trusted elder from each side for a single, focused "
            "conversation about expectations. Transparency early prevents assumptions later.\n\n"
            "3. **Build shared rituals** — Couples with consistent shared activities (a weekly dinner, a walk, "
            "a shared project) report 40% higher long-term satisfaction. Start small.\n\n"
            "4. **Revisit in 3 months** — Compatibility is not static. Reassess these areas after spending "
            "more intentional time together and note what has naturally converged.\n\n"
            "Strong foundations are built through consistent small actions, not dramatic gestures."
        )
    elif "inlaw" in p or "family" in p or "contradiction" in p:
        return (
            "The family assessment reveals some areas worth discussing before the wedding. "
            "Both families hold broadly supportive values, though there are differences in how "
            "much autonomy they expect the couple to have versus how involved they expect to remain. "
            "These differences are navigable with early, honest conversations — particularly around "
            "where the couple will live and how financial decisions will be made. Cultural differences "
            "in family involvement are among the most common sources of post-marriage friction in "
            "South Asian marriages, but they are also among the most resolvable when addressed proactively."
        )
    else:
        return (
            "The AI-generated analysis will appear here. This system uses Google Gemini to provide "
            "personalised, context-aware insights based on both partners' full profiles and family assessments. "
            "Configure the GEMINI_API_KEY in your Streamlit secrets to enable live AI responses."
        )


# Alias for backward compatibility
def get_llm_response(prompt: str, max_tokens: int = 800) -> str:
    return call_llm(prompt, max_tokens)
