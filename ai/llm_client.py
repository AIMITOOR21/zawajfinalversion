"""LLM client — supports Gemini API with fallback to mock responses.
   Maintains get_llm_response signature for backward compatibility.
"""

import os
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from config import OPENAI_API_KEY, OPENAI_MODEL
except Exception:
    OPENAI_API_KEY = ""
    OPENAI_MODEL = "gpt-3.5-turbo"


def _get_gemini_key():
    """Read GEMINI_API_KEY from Streamlit secrets first, then env vars."""
    # Try Streamlit secrets (most reliable on Streamlit Cloud)
    try:
        import streamlit as st
        if hasattr(st, "secrets") and "GEMINI_API_KEY" in st.secrets:
            key = st.secrets["GEMINI_API_KEY"]
            if key:
                return key
    except Exception as e:
        print(f"[llm_client] Couldn't read st.secrets: {e}")

    # Fall back to environment variable
    return os.environ.get("GEMINI_API_KEY", "")


_gemini_model = None


def _get_gemini():
    """Initialise and cache the Gemini model."""
    global _gemini_model
    if _gemini_model is not None:
        return _gemini_model

    api_key = _get_gemini_key()
    if not api_key:
        print("[llm_client] No GEMINI_API_KEY found in secrets or env")
        return None

    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        _gemini_model = genai.GenerativeModel("gemini-1.5-flash")
        print(f"[llm_client] Gemini initialised. Key starts with: {api_key[:8]}...")
        return _gemini_model
    except Exception as e:
        print(f"[llm_client] Gemini init error: {e}")
        return None


def get_llm_response(prompt, system_prompt=None, temperature=0.7, max_tokens=1000):
    """Get LLM response. Tries Gemini first, then OpenAI, then mock.

    Returns:
        tuple: (response_text, used_real_api: bool)
    """
    full_prompt = f"{system_prompt}\n\n{prompt}" if system_prompt else prompt

    # Try Gemini
    client = _get_gemini()
    if client:
        try:
            response = client.generate_content(
                full_prompt,
                generation_config={"max_output_tokens": max_tokens, "temperature": temperature}
            )
            return response.text.strip(), True
        except Exception as e:
            print(f"[llm_client] Gemini call error: {e}")

    # Try OpenAI
    if OPENAI_API_KEY:
        try:
            from openai import OpenAI
            oa = OpenAI(api_key=OPENAI_API_KEY)
            messages = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            messages.append({"role": "user", "content": prompt})
            resp = oa.chat.completions.create(
                model=OPENAI_MODEL,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return resp.choices[0].message.content, True
        except Exception as e:
            print(f"[llm_client] OpenAI error: {e}")

    print("[llm_client] Falling back to mock response")
    return _mock_response(prompt), False


# Alias
def call_llm(prompt: str, max_tokens: int = 800) -> str:
    text, _ = get_llm_response(prompt, max_tokens=max_tokens)
    return text


def _mock_response(prompt):
    p = prompt.lower()
    if "conflict" in p or "argument" in p:
        return _mock_conflict_response(prompt)
    elif "advice" in p or "improvement" in p:
        return _mock_advice_response(prompt)
    elif "scenario" in p:
        return _mock_scenario_response(prompt)
    else:
        return _mock_general_response(prompt)


def _mock_conflict_response(prompt):
    return """Based on the profile differences, here are the predicted conflict scenarios:

**Conflict 1: Career vs Family Expectations (Severity: HIGH)**
Partner A values career growth while Partner B expects a family-focused lifestyle. This creates tension around work hours, travel, and household responsibilities. Resolution will require honest discussion about compromises on both sides.

**Conflict 2: Living Arrangement Disagreement (Severity: HIGH)**
Different expectations about joint vs nuclear family living. One partner's family expects them to live together, while the other values independence. This is one of the most common sources of marital friction in Pakistani families.

**Conflict 3: Financial Management Style (Severity: MEDIUM)**
Different approaches to managing household finances. One prefers pooled income while the other wants financial independence. Establishing a clear financial plan early in marriage is critical.

**Resolution Assessment:**
- Conflict 1: Resolution probability 35% without intervention, 65% with counseling
- Conflict 2: Resolution probability 40% without intervention, 70% with mediation
- Conflict 3: Resolution probability 55% without intervention, 80% with discussion"""


def _mock_advice_response(prompt):
    return """## Compatibility Improvement Plan

Based on the counterfactual analysis, here are actionable steps to improve compatibility:

### High-Impact Changes:
1. **Career Flexibility Discussion** - If both partners agree on a balanced approach to career vs family time, the compatibility score could increase by approximately 15-18%.

2. **Family Structure Negotiation** - If the families can agree on a modified living arrangement (e.g., nuclear household with regular family visits), this could add 10-12% to the score.

3. **Financial Planning Session** - Establishing a joint financial plan with agreed-upon allocations for family support, savings, and personal spending could improve financial alignment by 8-10%.

### Moderate-Impact Changes:
4. **Religious Practice Alignment** - Finding common ground on religious observance level through mutual understanding and respect.

5. **Role Distribution Agreement** - Creating a written household responsibility plan that both partners find fair.

### Recommendation:
We suggest a facilitated pre-marital discussion covering these topics in order of priority. A trained counselor can help navigate sensitive cultural dynamics."""


def _mock_scenario_response(prompt):
    return """Here is a culturally relevant scenario for assessment:

**Scenario: The Job Transfer**
Your spouse receives a promotion that requires transferring to another city for 2 years.

**Choice A:** Support the transfer fully - career growth benefits the whole family
**Choice B:** Negotiate for a shorter assignment of 6 months to test it out
**Choice C:** Ask your spouse to decline - family stability is more important
**Choice D:** Suggest your spouse goes alone while you stay with the family"""


def _mock_general_response(prompt):
    return """Based on the analysis, the couple shows both areas of alignment and significant differences that need attention. The key areas of concern involve differing expectations about family structure and career priorities. With open communication and willingness to compromise, many of these differences can be addressed through structured pre-marital counseling and family discussions."""
