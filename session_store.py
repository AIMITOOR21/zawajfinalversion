"""
session_store.py — Persist session data across Streamlit pages via a temp JSON file.

Usage:
    from session_store import save_profiles, load_profiles

    # On assessment page after saving:
    save_profiles(person_a, person_b, name_a, name_b)

    # On any other page at the top of main():
    load_profiles()   # loads into st.session_state if not already there
"""

import json
import streamlit as st
from pathlib import Path

# Store in /tmp so it survives page navigation on Streamlit Cloud
_STORE_PATH = Path("/tmp/zawaj_session.json")


def save_profiles(person_a: dict, person_b: dict, name_a: str, name_b: str):
    """Persist profiles to disk and into session_state."""
    data = {
        "person_a": person_a,
        "person_b": person_b,
        "person_a_name": name_a,
        "person_b_name": name_b,
        "assessment_complete": True,
    }
    _STORE_PATH.write_text(json.dumps(data), encoding="utf-8")
    _apply_to_session(data)


def load_profiles() -> bool:
    """
    Load profiles from disk into session_state (if not already set).
    Returns True if data was available, False if assessment hasn't been done.
    """
    # Already in session state — nothing to do
    if st.session_state.get("assessment_complete") and st.session_state.get("person_a"):
        return True

    if not _STORE_PATH.exists():
        return False

    try:
        data = json.loads(_STORE_PATH.read_text(encoding="utf-8"))
        _apply_to_session(data)
        return True
    except Exception:
        return False


def _apply_to_session(data: dict):
    for key, value in data.items():
        st.session_state[key] = value
    # Also mirror under legacy keys used elsewhere
    st.session_state["profile_a"] = data["person_a"]
    st.session_state["profile_b"] = data["person_b"]
