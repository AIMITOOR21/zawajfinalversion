"""Page 2 — In-Laws Questionnaire.

Psychologically complex pre-marriage expectation scenarios.
5 scenarios per family member × 8 members = 40 total.
Varied Google Fonts per section. No spouse-specific questions — all are
general standing values that can be matched against any partner's profile.
"""

import streamlit as st
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
from config import COLORS

# ══════════════════════════════════════════════
#  PSYCHOLOGICAL IN-LAW SCENARIOS
#  All general (no specific person named).
#  Every option sounds reasonable; bias hides in phrasing.
# ══════════════════════════════════════════════

INLAW_SCENARIOS = {

    # ─── GIRL'S SIDE ──────────────────────────────────────────────────────────

    "sara_mother": {
        "label": "Sara's Mother",
        "font_import": "https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Poppins:wght@300;400;500&display=swap",
        "heading_font": "Playfair Display",
        "body_font": "Poppins",
        "accent": "#D4577A",
        "bg": "#FDEEF2",
        "scenarios": [
            {
                "id": "sm_1", "topic": "Describing her ideal son-in-law",
                "question": "When you imagine the kind of man you'd want for your daughter, what comes to mind first?",
                "choices": [
                    {"text": "Someone she chooses for herself, that she can build a life with.", "score": 1.0},
                    {"text": "A man from a good, respectable family — with steady prospects.", "score": 0.45},
                    {"text": "Someone who would treat her well and adjust to our family's rhythm.", "score": 0.4},
                    {"text": "A man with character. Money and background are secondary.", "score": 0.7}
                ]
            },
            {
                "id": "sm_2", "topic": "Most important quality in a son-in-law",
                "question": "If you had to name the single most important quality, what would it be?",
                "choices": [
                    {"text": "That my daughter feels respected by him.", "score": 1.0},
                    {"text": "That he comes from people we know and trust.", "score": 0.35},
                    {"text": "That he's the kind of man who listens — to her, to us, to wisdom.", "score": 0.5},
                    {"text": "That he can stand on his own — emotionally, financially, socially.", "score": 0.7}
                ]
            },
            {
                "id": "sm_3", "topic": "Relationship with son-in-law",
                "question": "What kind of relationship would you ideally have with your daughter's husband?",
                "choices": [
                    {"text": "Close, like a son — someone we'd both lean on and support.", "score": 0.9},
                    {"text": "Respectful — we don't need to be close, just kind.", "score": 0.65},
                    {"text": "I'd want him to come to us when things get difficult.", "score": 0.4},
                    {"text": "Whatever feels natural. Some sons-in-law are close, some aren't.", "score": 0.5}
                ]
            },
            {
                "id": "sm_4", "topic": "What would make her hesitate",
                "question": "What would make you most uncomfortable about a potential son-in-law — even if everything else seemed fine?",
                "choices": [
                    {"text": "If my daughter seemed unsure about him, even slightly.", "score": 1.0},
                    {"text": "If his family had a reputation or background we weren't sure of.", "score": 0.35},
                    {"text": "If he seemed the kind to dominate or shut her down.", "score": 0.8},
                    {"text": "If he was too independent — too much his own person.", "score": 0.2}
                ]
            },
            {
                "id": "sm_5", "topic": "Quiet hope for the marriage",
                "question": "What's the quiet hope you carry about your daughter's eventual marriage?",
                "choices": [
                    {"text": "That she stays herself — that marriage adds to her, doesn't shrink her.", "score": 1.0},
                    {"text": "That she's well-settled and never has to worry about anything.", "score": 0.55},
                    {"text": "That she doesn't drift too far from us — that we remain part of her life.", "score": 0.4},
                    {"text": "That her husband becomes part of our family, fully.", "score": 0.5}
                ]
            }
        ]
    },

    "sara_father": {
        "label": "Sara's Father",
        "font_import": "https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=Inter:wght@300;400;500&display=swap",
        "heading_font": "Cormorant Garamond",
        "body_font": "Inter",
        "accent": "#7A4A2E",
        "bg": "#FDF5EF",
        "scenarios": [
            {
                "id": "sf_1", "topic": "Son-in-law's role",
                "question": "What's the most important thing for a son-in-law to be for your daughter?",
                "choices": [
                    {"text": "A partner — someone who walks beside her, not ahead of her.", "score": 1.0},
                    {"text": "A protector — financially, socially, in every way.", "score": 0.5},
                    {"text": "A steady presence — someone who keeps her grounded.", "score": 0.45},
                    {"text": "Someone who genuinely values what she brings to the marriage.", "score": 0.8}
                ]
            },
            {
                "id": "sf_2", "topic": "Handling disagreements",
                "question": "How should a son-in-law handle a disagreement with your daughter?",
                "choices": [
                    {"text": "He should talk to her directly until they understand each other.", "score": 1.0},
                    {"text": "He should know when to walk away and revisit later.", "score": 0.55},
                    {"text": "He should be the calmer one — someone has to be.", "score": 0.5},
                    {"text": "He should bring it to the family if they can't resolve it.", "score": 0.2}
                ]
            },
            {
                "id": "sf_3", "topic": "Financial expectations",
                "question": "What do you expect from a son-in-law financially?",
                "choices": [
                    {"text": "That he and my daughter handle their finances together as they see fit.", "score": 1.0},
                    {"text": "That he's stable and able to provide for the household.", "score": 0.6},
                    {"text": "That he's transparent — no surprises.", "score": 0.65},
                    {"text": "That my daughter never has to worry about money.", "score": 0.5}
                ]
            },
            {
                "id": "sf_4", "topic": "Authority dynamic",
                "question": "Do you see a son-in-law as someone who should defer to elders, or someone with his own standing?",
                "choices": [
                    {"text": "His own standing. He's not our subordinate.", "score": 1.0},
                    {"text": "Both — respect for elders, but his decisions are his.", "score": 0.7},
                    {"text": "He should listen — that's how a young man matures.", "score": 0.3},
                    {"text": "It depends on his own family's culture. We'd adapt.", "score": 0.55}
                ]
            },
            {
                "id": "sf_5", "topic": "Private worry",
                "question": "What's your private worry about your daughter's future husband?",
                "choices": [
                    {"text": "That he won't show up for her when she's struggling.", "score": 1.0},
                    {"text": "That his family will pull him away from her.", "score": 0.4},
                    {"text": "That she'll soften too much for him — lose her edge.", "score": 0.5},
                    {"text": "I don't worry. She's strong enough to choose well.", "score": 0.7}
                ]
            }
        ]
    },

    "sara_brother": {
        "label": "Sara's Brother",
        "font_import": "https://fonts.googleapis.com/css2?family=Lora:wght@400;600;700&family=Karla:wght@300;400;500&display=swap",
        "heading_font": "Lora",
        "body_font": "Karla",
        "accent": "#2E5E7A",
        "bg": "#EFF7FC",
        "scenarios": [
            {
                "id": "sb_1", "topic": "Relationship with brother-in-law",
                "question": "How close do you imagine being with your sister's husband?",
                "choices": [
                    {"text": "Like a brother. Someone I'd hang out with on my own.", "score": 1.0},
                    {"text": "Friendly — we don't need to be close to be respectful.", "score": 0.6},
                    {"text": "As close as he wants to be. I won't force it.", "score": 0.5},
                    {"text": "Cordial. The connection is really between him and my sister.", "score": 0.35}
                ]
            },
            {
                "id": "sb_2", "topic": "Sister's complaints about husband",
                "question": "If your sister comes to you complaining about her husband, what's your first instinct?",
                "choices": [
                    {"text": "Listen, then ask if she's talked to him directly.", "score": 1.0},
                    {"text": "Take her side until she calms down.", "score": 0.45},
                    {"text": "Ask what he did — I want to know.", "score": 0.4},
                    {"text": "Stay out of it. It's their marriage.", "score": 0.55}
                ]
            },
            {
                "id": "sb_3", "topic": "His decisions about sister",
                "question": "He's making a decision that affects your sister — moving cities, big career change. He didn't ask your family. How do you feel?",
                "choices": [
                    {"text": "Fine. It's their decision.", "score": 1.0},
                    {"text": "I'd wish my sister had told us first.", "score": 0.45},
                    {"text": "I'd want to know he thought it through.", "score": 0.6},
                    {"text": "As long as my sister agrees, that's enough.", "score": 0.9}
                ]
            },
            {
                "id": "sb_4", "topic": "Comparison and rivalry",
                "question": "Your brother-in-law is doing better than you financially or professionally. What's your honest reaction?",
                "choices": [
                    {"text": "Good for him. We're not in competition.", "score": 1.0},
                    {"text": "Happy for my sister — she chose well.", "score": 0.8},
                    {"text": "It motivates me. I'd want to match it.", "score": 0.65},
                    {"text": "It doesn't matter. We have different paths.", "score": 0.7}
                ]
            },
            {
                "id": "sb_5", "topic": "Where loyalty sits",
                "question": "If there's ever a serious conflict between your sister and her husband — where does your loyalty sit?",
                "choices": [
                    {"text": "With the truth. I'd back whoever's right.", "score": 1.0},
                    {"text": "With my sister — that's blood. But I'd hear him out.", "score": 0.65},
                    {"text": "With my sister always. He's not family the way she is.", "score": 0.25},
                    {"text": "With their marriage. I'd want them to work it out.", "score": 0.9}
                ]
            }
        ]
    },

    "sara_sister": {
        "label": "Sara's Sister",
        "font_import": "https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500&display=swap",
        "heading_font": "DM Serif Display",
        "body_font": "DM Sans",
        "accent": "#8A3A6A",
        "bg": "#FBF0F7",
        "scenarios": [
            {
                "id": "ss_1", "topic": "What she'd want for sister",
                "question": "What's the most important thing for your sister's husband to be for her?",
                "choices": [
                    {"text": "Her best friend.", "score": 1.0},
                    {"text": "A man who lets her be fully herself.", "score": 0.95},
                    {"text": "Someone who can handle her — she's not easy, I'd know.", "score": 0.3},
                    {"text": "Reliable. Someone she can count on.", "score": 0.7}
                ]
            },
            {
                "id": "ss_2", "topic": "Relationship with brother-in-law",
                "question": "What would you want with your sister's husband?",
                "choices": [
                    {"text": "Friendship — I'd like having him around.", "score": 1.0},
                    {"text": "Respect — he doesn't need to be a friend.", "score": 0.55},
                    {"text": "Whatever makes my sister comfortable.", "score": 0.8},
                    {"text": "I'd see him at family events. That's enough.", "score": 0.35}
                ]
            },
            {
                "id": "ss_3", "topic": "Sister venting about husband",
                "question": "Your sister vents about her husband to you regularly. How do you respond?",
                "choices": [
                    {"text": "I listen, then ask if she wants advice or just to be heard.", "score": 1.0},
                    {"text": "I always take her side — she needs that.", "score": 0.4},
                    {"text": "I ask her if she's being fair to him.", "score": 0.85},
                    {"text": "I tell her this is what marriage is.", "score": 0.3}
                ]
            },
            {
                "id": "ss_4", "topic": "Visible affection",
                "question": "Your sister and her husband are visibly affectionate around the family. How do you feel?",
                "choices": [
                    {"text": "Happy for them — that's a good marriage.", "score": 1.0},
                    {"text": "Fine, as long as it's appropriate.", "score": 0.55},
                    {"text": "A little awkward, but I get it.", "score": 0.6},
                    {"text": "It doesn't bother me — I'm glad she's loved.", "score": 0.9}
                ]
            },
            {
                "id": "ss_5", "topic": "Sister spending more time with in-laws",
                "question": "Your sister starts spending more time with his family than yours. How do you feel?",
                "choices": [
                    {"text": "That's how marriage works. She's building her new home.", "score": 1.0},
                    {"text": "I'd miss her, but I wouldn't say anything.", "score": 0.6},
                    {"text": "I'd hope she balances both sides.", "score": 0.5},
                    {"text": "I'd want her to remember where she came from.", "score": 0.2}
                ]
            }
        ]
    },

    # ─── BOY'S SIDE ───────────────────────────────────────────────────────────

    "ahmed_mother": {
        "label": "Ahmed's Mother",
        "font_import": "https://fonts.googleapis.com/css2?family=Libre+Caslon+Text:wght@400;700&family=Work+Sans:wght@300;400;500&display=swap",
        "heading_font": "Libre Caslon Text",
        "body_font": "Work Sans",
        "accent": "#5A7A3A",
        "bg": "#F0F7EC",
        "scenarios": [
            {
                "id": "am_1", "topic": "Daughter-in-law's place in the home",
                "question": "How do you see a daughter-in-law in your home?",
                "choices": [
                    {"text": "As my son's wife — her home is the one she builds with him.", "score": 1.0},
                    {"text": "As a daughter — fully part of the family from day one.", "score": 0.75},
                    {"text": "As family, with time. Trust is built.", "score": 0.5},
                    {"text": "Someone who'll bring her own ways — and we'll find a rhythm together.", "score": 0.85}
                ]
            },
            {
                "id": "am_2", "topic": "Daughter-in-law's career",
                "question": "What's your view on a daughter-in-law continuing her career after marriage?",
                "choices": [
                    {"text": "Her decision entirely.", "score": 1.0},
                    {"text": "Of course — we're a modern family.", "score": 0.7},
                    {"text": "As long as the home doesn't suffer for it.", "score": 0.35},
                    {"text": "It's between her and my son.", "score": 0.5}
                ]
            },
            {
                "id": "am_3", "topic": "What she'd want her to call her",
                "question": "What would you ideally want your daughter-in-law to call you?",
                "choices": [
                    {"text": "Whatever she's comfortable with.", "score": 1.0},
                    {"text": "Mama, like a daughter.", "score": 0.6},
                    {"text": "Aunty initially — Mama if she comes to feel that way.", "score": 0.75},
                    {"text": "It's not the word, it's the relationship.", "score": 0.85}
                ]
            },
            {
                "id": "am_4", "topic": "Her relationship with her own family",
                "question": "What's your view on her relationship with her own parents after marriage?",
                "choices": [
                    {"text": "They raised her. She should be with them often.", "score": 1.0},
                    {"text": "Of course she'll see them. Balance is the key.", "score": 0.6},
                    {"text": "They're family too — we'd visit together.", "score": 0.5},
                    {"text": "It'll adjust naturally over time.", "score": 0.3}
                ]
            },
            {
                "id": "am_5", "topic": "Quiet hope about son's wife",
                "question": "What's your quiet hope about the woman who'll marry your son?",
                "choices": [
                    {"text": "That she's happy with him. That's the foundation of everything.", "score": 1.0},
                    {"text": "That she fits well into our family.", "score": 0.4},
                    {"text": "That she makes him a better man.", "score": 0.6},
                    {"text": "That she has the patience for a long marriage.", "score": 0.35}
                ]
            }
        ]
    },

    "ahmed_father": {
        "label": "Ahmed's Father",
        "font_import": "https://fonts.googleapis.com/css2?family=Crimson+Pro:wght@400;600;700&family=Manrope:wght@300;400;500&display=swap",
        "heading_font": "Crimson Pro",
        "body_font": "Manrope",
        "accent": "#3A4A7A",
        "bg": "#EEF0FA",
        "scenarios": [
            {
                "id": "af_1", "topic": "What he wants from daughter-in-law",
                "question": "What do you most want from your daughter-in-law?",
                "choices": [
                    {"text": "That she's good to my son and finds happiness with him.", "score": 1.0},
                    {"text": "That she respects the family and we respect her.", "score": 0.7},
                    {"text": "That she's the kind of woman my son needs.", "score": 0.45},
                    {"text": "That she contributes to the home in her own way.", "score": 0.55}
                ]
            },
            {
                "id": "af_2", "topic": "Her independence",
                "question": "How do you feel about a daughter-in-law who has strong opinions?",
                "choices": [
                    {"text": "Good — a thinking woman is a good partner.", "score": 1.0},
                    {"text": "Fine, as long as there's respect when she disagrees.", "score": 0.65},
                    {"text": "As long as she knows when to listen.", "score": 0.35},
                    {"text": "My son needs that. He's stubborn — she'll balance him.", "score": 0.6}
                ]
            },
            {
                "id": "af_3", "topic": "Conflict between daughter-in-law and wife",
                "question": "If there's ever friction between your wife and your daughter-in-law, what's your role?",
                "choices": [
                    {"text": "I'd let them work it out unless it becomes serious.", "score": 0.7},
                    {"text": "I'd quietly support my wife — she's been here longer.", "score": 0.2},
                    {"text": "I'd hear both sides honestly.", "score": 1.0},
                    {"text": "I'd ask my son to manage it.", "score": 0.3}
                ]
            },
            {
                "id": "af_4", "topic": "Her career and finances",
                "question": "Should a daughter-in-law contribute financially to the household?",
                "choices": [
                    {"text": "If she earns, she decides what to do with it.", "score": 1.0},
                    {"text": "Only if she wants to — no obligation.", "score": 0.7},
                    {"text": "It's expected — we all contribute.", "score": 0.4},
                    {"text": "That's between her and my son.", "score": 0.55}
                ]
            },
            {
                "id": "af_5", "topic": "Long-term relationship",
                "question": "In 10 years, how do you imagine your relationship with your daughter-in-law?",
                "choices": [
                    {"text": "Like a daughter — fully family by then.", "score": 0.85},
                    {"text": "Close, but with her own household.", "score": 1.0},
                    {"text": "Respectful, depending on how she's been with us.", "score": 0.3},
                    {"text": "It'll be what it'll be. I don't predict.", "score": 0.5}
                ]
            }
        ]
    },

    "ahmed_brother": {
        "label": "Ahmed's Brother",
        "font_import": "https://fonts.googleapis.com/css2?family=Spectral:wght@400;600;700&family=Mulish:wght@300;400;500&display=swap",
        "heading_font": "Spectral",
        "body_font": "Mulish",
        "accent": "#2A6A5A",
        "bg": "#EDF7F5",
        "scenarios": [
            {
                "id": "abr_1", "topic": "What he'd want for his brother",
                "question": "What would you most want for your brother in his wife?",
                "choices": [
                    {"text": "A real partner — equal footing.", "score": 1.0},
                    {"text": "Someone who understands him deeply.", "score": 0.8},
                    {"text": "Someone who can keep him in line — he needs that.", "score": 0.35},
                    {"text": "Someone who makes him happier than I've seen him.", "score": 0.9}
                ]
            },
            {
                "id": "abr_2", "topic": "Closeness to sister-in-law",
                "question": "What kind of relationship do you imagine with your sister-in-law?",
                "choices": [
                    {"text": "Friendship — like a sibling.", "score": 1.0},
                    {"text": "Respectful, with healthy distance.", "score": 0.65},
                    {"text": "Whatever feels natural over time.", "score": 0.7},
                    {"text": "I'd see her as my brother's wife — that's enough.", "score": 0.35}
                ]
            },
            {
                "id": "abr_3", "topic": "Her differences from the family",
                "question": "If she's very different from your family in upbringing, values, or style — how would you respond?",
                "choices": [
                    {"text": "Curiosity — I'd want to learn about her world.", "score": 1.0},
                    {"text": "Tolerance — we don't need to be alike.", "score": 0.7},
                    {"text": "Hope she'd adapt — easier for everyone.", "score": 0.3},
                    {"text": "Wouldn't be my place to comment.", "score": 0.55}
                ]
            },
            {
                "id": "abr_4", "topic": "Brother spending more time with wife",
                "question": "After your brother marries, how do you feel about him spending more time with her than family?",
                "choices": [
                    {"text": "Normal and good — that's the marriage.", "score": 1.0},
                    {"text": "As long as he doesn't disappear.", "score": 0.55},
                    {"text": "It changes things, but we adapt.", "score": 0.65},
                    {"text": "I'd hope she encourages him to stay close to family.", "score": 0.35}
                ]
            },
            {
                "id": "abr_5", "topic": "Defending her",
                "question": "If a family member speaks badly about her behind her back, what would you do?",
                "choices": [
                    {"text": "I'd defend her openly.", "score": 1.0},
                    {"text": "I'd ask them to bring it up directly instead.", "score": 0.8},
                    {"text": "I'd listen — sometimes there's truth in concerns.", "score": 0.35},
                    {"text": "It's not my place to take sides in family talk.", "score": 0.3}
                ]
            }
        ]
    },

    "ahmed_sister": {
        "label": "Ahmed's Sister",
        "font_import": "https://fonts.googleapis.com/css2?family=Fraunces:wght@400;600;700&family=Geist:wght@300;400;500&display=swap",
        "heading_font": "Fraunces",
        "body_font": "Geist",
        "accent": "#7A3A5A",
        "bg": "#FAF0F5",
        "scenarios": [
            {
                "id": "asi_1", "topic": "Kind of woman for her brother",
                "question": "What kind of woman would you most want to see your brother marry?",
                "choices": [
                    {"text": "Someone who makes him a better version of himself.", "score": 0.8},
                    {"text": "Someone strong enough to handle him.", "score": 0.4},
                    {"text": "Someone we'd all genuinely like and welcome.", "score": 0.6},
                    {"text": "Someone who has her own life — not just absorbed into his.", "score": 1.0}
                ]
            },
            {
                "id": "asi_2", "topic": "Sharing her brother",
                "question": "What does it feel like imagining sharing your brother with another woman?",
                "choices": [
                    {"text": "It's a good thing — he gets to build something of his own.", "score": 1.0},
                    {"text": "It's bittersweet, but natural.", "score": 0.75},
                    {"text": "I'd want to make sure she values him properly.", "score": 0.4},
                    {"text": "I don't think about it that way — he was never just mine.", "score": 0.85}
                ]
            },
            {
                "id": "asi_3", "topic": "Her behavior at family events",
                "question": "At family events, how should a sister-in-law behave?",
                "choices": [
                    {"text": "However she's comfortable — she's family.", "score": 1.0},
                    {"text": "Engaged and warm — that's how relationships build.", "score": 0.8},
                    {"text": "Polite and aware of family norms.", "score": 0.45},
                    {"text": "She'll find her place over time.", "score": 0.55}
                ]
            },
            {
                "id": "asi_4", "topic": "Getting along despite differences",
                "question": "You and your sister-in-law are different in style and personality. How do you imagine getting along?",
                "choices": [
                    {"text": "Difference is interesting — I'd want to know her.", "score": 1.0},
                    {"text": "We don't need to be alike to be friends.", "score": 0.8},
                    {"text": "As long as there's mutual respect.", "score": 0.65},
                    {"text": "I wouldn't compare — we play different roles in the family.", "score": 0.5}
                ]
            },
            {
                "id": "asi_5", "topic": "Conflict with sister-in-law",
                "question": "If you and your sister-in-law have a disagreement, what's the right way to handle it?",
                "choices": [
                    {"text": "Direct conversation between us — no third party.", "score": 1.0},
                    {"text": "Through my brother if needed.", "score": 0.3},
                    {"text": "Time usually heals things.", "score": 0.4},
                    {"text": "We'd be expected to keep it civil — family is family.", "score": 0.55}
                ]
            }
        ]
    }
}


# ══════════════════════════════════════════════
#  PAGE CSS
# ══════════════════════════════════════════════

def page_base_css():
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #FDEEF2 0%, #FFFFFF 50%, #FDEEF2 100%);
        background-attachment: fixed;
    }
    .block-container { padding-top: 1.2rem; max-width: 1100px; }

    .page-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.5rem; font-weight: 700; font-style: italic;
        background: linear-gradient(135deg, #5C2A3E, #D4577A);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        background-clip: text; text-align: center; margin-bottom: 0.2rem;
    }
    .page-subtitle {
        text-align: center; color: #8B4D6B;
        font-family: 'Poppins', sans-serif; font-size: 0.95rem;
    }
    .member-header {
        border-radius: 12px; padding: 1rem 1.4rem;
        margin: 0.8rem 0 0.5rem;
    }
    .member-name {
        font-size: 1.4rem; font-weight: 700; margin: 0;
    }
    .scenario-card {
        background: #fff; border-radius: 12px;
        padding: 1.2rem 1.5rem; margin-bottom: 0.8rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.06);
        border-left: 4px solid #ddd;
        animation: fadeIn 0.4s ease-out;
    }
    .topic-tag {
        font-size: 0.72rem; font-weight: 600; text-transform: uppercase;
        letter-spacing: 1px; margin-bottom: 0.4rem;
    }
    .scenario-q {
        font-size: 1.05rem; font-style: italic; line-height: 1.5;
        color: #2A1018; margin: 0.3rem 0 0.8rem;
    }
    .score-card {
        border-radius: 10px; padding: 1rem 1.4rem;
        text-align: center; margin: 0.6rem 0;
    }
    .score-num {
        font-size: 2.2rem; font-weight: 700;
    }
    .progress-bg {
        background: #f0e0e8; border-radius: 8px; height: 6px;
        margin: 0.4rem 0; overflow: hidden;
    }
    .progress-fill {
        height: 100%; border-radius: 8px;
        background: linear-gradient(90deg, #D4577A, #C9A96E);
        transition: width 0.4s;
    }
    [data-testid="stExpander"] details summary span,
    [data-testid="stExpander"] details summary p,
    [data-testid="stExpander"] > div > div > div,
    [data-testid="stExpander"] label,
    [data-testid="stExpander"] p {
        color: #2A1A2B !important;
        font-family: 'Poppins', sans-serif !important;
    }
    [data-testid="stExpander"] details summary {
        color: #3A1A2B !important;
        font-weight: 600 !important;
    }
    @keyframes fadeIn {
        from { opacity:0; transform: translateY(10px); }
        to   { opacity:1; transform: translateY(0); }
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Poppins:wght@300;400;500&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)


def member_font_css(member_key):
    m = INLAW_SCENARIOS[member_key]
    st.markdown(f"""
    <link href="{m['font_import']}" rel="stylesheet">
    <style>
    .mh-{member_key} {{ background: {m['bg']}; }}
    .mh-{member_key} .member-name {{ color: {m['accent']}; font-family: '{m['heading_font']}', serif; }}
    .sc-{member_key} {{ border-left-color: {m['accent']}; }}
    .sc-{member_key} .topic-tag {{ color: {m['accent']}; }}
    .sc-{member_key} .scenario-q {{ font-family: '{m['heading_font']}', serif; }}
    </style>
    """, unsafe_allow_html=True)


def compute_member_score(responses, member_key):
    member = INLAW_SCENARIOS[member_key]
    scores = []
    for sc in member["scenarios"]:
        if sc["id"] in responses:
            idx = responses[sc["id"]]
            scores.append(sc["choices"][idx]["score"])
    if not scores:
        return None
    return round(sum(scores) / len(scores) * 100, 1)


def render_member(member_key, side_label, sibling=False):
    m = INLAW_SCENARIOS[member_key]
    member_font_css(member_key)

    key_prefix = member_key

    # Sibling toggle
    if sibling:
        has = st.checkbox(f"Include {m['label']} in assessment", value=True, key=f"has_{key_prefix}")
        if not has:
            return None

    # Header
    st.markdown(f"""
    <div class="member-header mh-{member_key}">
        <p class="member-name">👤 {m['label']}</p>
        <p style="margin:0;font-size:0.85rem;color:#666;font-family:'{m['body_font']}',sans-serif;">
            {side_label} · {len(m['scenarios'])} scenarios
        </p>
    </div>""", unsafe_allow_html=True)

    # Session state
    resp_key = f"inlaw_resp_{key_prefix}"
    if resp_key not in st.session_state:
        st.session_state[resp_key] = {}

    responses = st.session_state[resp_key]
    done = len(responses)
    total = len(m["scenarios"])

    # Progress
    pct = done / total if total else 0
    st.markdown(f"""
    <div class="progress-bg">
        <div class="progress-fill" style="width:{pct*100:.0f}%"></div>
    </div>
    <p style="font-size:0.75rem;color:#888;font-family:'Poppins',sans-serif;">{done}/{total} answered</p>
    """, unsafe_allow_html=True)

    # Scenarios
    for sc in m["scenarios"]:
        sid = sc["id"]
        if sid in responses:
            idx = responses[sid]
            chosen_text = sc["choices"][idx]["text"]
            with st.expander(f"✅ {sc['topic']}", expanded=False):
                st.markdown(f'<p class="scenario-q sc-{member_key}">{sc["question"]}</p>', unsafe_allow_html=True)
                st.success(f"Selected: {chosen_text}")
                if st.button("Change", key=f"chg_{sid}"):
                    del responses[sid]
                    st.rerun()
        else:
            st.markdown(f"""
            <div class="scenario-card sc-{member_key}">
                <div class="topic-tag">{sc['topic']}</div>
                <p class="scenario-q">{sc['question']}</p>
            </div>""", unsafe_allow_html=True)

            labels = [c["text"] for c in sc["choices"]]
            sel = st.radio("", labels, key=f"radio_{sid}", index=None, label_visibility="collapsed")
            if sel is not None:
                idx = labels.index(sel)
                responses[sid] = idx
                st.session_state[resp_key] = responses
                st.rerun()
            break  # one at a time

    # Score card if complete
    score = compute_member_score(responses, member_key)
    if score is not None and done == total:
        color = "#6BAF73" if score >= 70 else "#E8A846" if score >= 45 else "#D4577A"
        label = "Supportive" if score >= 70 else "Mixed" if score >= 45 else "Friction Risk"
        st.markdown(f"""
        <div class="score-card" style="background:{color}15;border:1px solid {color}40;">
            <div class="score-num" style="color:{color}">{score}%</div>
            <div style="color:{color};font-weight:600;font-family:'Poppins',sans-serif;">{label}</div>
        </div>""", unsafe_allow_html=True)

    return score


# ══════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════

def main():
    page_base_css()

    st.markdown('<p class="page-title">🏠 Family Compatibility Assessment</p>', unsafe_allow_html=True)
    st.markdown('<p class="page-subtitle">Pre-marriage family values · Member-by-member · Both sides</p>',
                unsafe_allow_html=True)

    names = st.session_state.get("names", {"a": "Sara", "b": "Ahmed"})
    name_a = names.get("a", "Sara")
    name_b = names.get("b", "Ahmed")

    # Demo mode
    with st.expander("⚡ Demo Mode — auto-fill all family members"):
        if st.button("Auto-fill ALL family members"):
            for mk, md in INLAW_SCENARIOS.items():
                resp_key = f"inlaw_resp_{mk}"
                st.session_state[resp_key] = {sc["id"]: 0 for sc in md["scenarios"]}
            st.success("All family members auto-filled with demo answers!")
            st.rerun()
        if st.button("🔄 Reset all family answers"):
            for mk in INLAW_SCENARIOS:
                resp_key = f"inlaw_resp_{mk}"
                if resp_key in st.session_state:
                    del st.session_state[resp_key]
            st.rerun()

    st.markdown("---")

    # Tabs
    tab_sara, tab_ahmed, tab_analysis = st.tabs([
        f"💐 {name_a}'s Family", f"🌙 {name_b}'s Family", "🔺 Combined Analysis"
    ])

    with tab_sara:
        st.markdown(f"### {name_a}'s family expectations of her future husband")
        st.info("These questions capture what each family member values in a son-in-law — general standing values, not about a specific person.")

        sm_score = render_member("sara_mother", f"{name_a}'s side")
        st.markdown("---")
        sf_score = render_member("sara_father", f"{name_a}'s side")
        st.markdown("---")
        sb_score = render_member("sara_brother", f"{name_a}'s side", sibling=True)
        st.markdown("---")
        ss_score = render_member("sara_sister", f"{name_a}'s side", sibling=True)

    with tab_ahmed:
        st.markdown(f"### {name_b}'s family expectations of his future wife")
        st.info("These questions reveal what each family member truly expects from a daughter-in-law — values they'd apply to any match.")

        am_score = render_member("ahmed_mother", f"{name_b}'s side")
        st.markdown("---")
        af_score = render_member("ahmed_father", f"{name_b}'s side")
        st.markdown("---")
        abr_score = render_member("ahmed_brother", f"{name_b}'s side", sibling=True)
        st.markdown("---")
        asi_score = render_member("ahmed_sister", f"{name_b}'s side", sibling=True)

    with tab_analysis:
        st.markdown("### 🔺 Combined Family Compatibility Analysis")

        # Collect scores
        sara_scores = {}
        ahmed_scores = {}
        all_members = {
            "sara_mother": "Mother", "sara_father": "Father",
            "sara_brother": "Brother", "sara_sister": "Sister"
        }
        ahmed_members = {
            "ahmed_mother": "Mother", "ahmed_father": "Father",
            "ahmed_brother": "Brother", "ahmed_sister": "Sister"
        }

        for mk, label in all_members.items():
            resp_key = f"inlaw_resp_{mk}"
            if resp_key in st.session_state:
                s = compute_member_score(st.session_state[resp_key], mk)
                if s is not None:
                    sara_scores[label] = s

        for mk, label in ahmed_members.items():
            resp_key = f"inlaw_resp_{mk}"
            if resp_key in st.session_state:
                s = compute_member_score(st.session_state[resp_key], mk)
                if s is not None:
                    ahmed_scores[label] = s

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"#### 💐 {name_a}'s Family Scores")
            if sara_scores:
                for label, score in sara_scores.items():
                    color = "#6BAF73" if score >= 70 else "#E8A846" if score >= 45 else "#D4577A"
                    st.markdown(f"""
                    <div style="display:flex;justify-content:space-between;align-items:center;
                         background:{color}12;border-radius:8px;padding:0.5rem 1rem;margin:0.3rem 0;">
                        <span style="font-family:'Poppins',sans-serif;font-weight:500;">{label}</span>
                        <span style="color:{color};font-weight:700;font-size:1.1rem;">{score}%</span>
                    </div>""", unsafe_allow_html=True)
                sara_avg = round(sum(sara_scores.values()) / len(sara_scores), 1)
                st.markdown(f"**{name_a}'s family average: {sara_avg}%**")
            else:
                st.info(f"Complete {name_a}'s family assessment to see scores.")

        with col2:
            st.markdown(f"#### 🌙 {name_b}'s Family Scores")
            if ahmed_scores:
                for label, score in ahmed_scores.items():
                    color = "#6BAF73" if score >= 70 else "#E8A846" if score >= 45 else "#D4577A"
                    st.markdown(f"""
                    <div style="display:flex;justify-content:space-between;align-items:center;
                         background:{color}12;border-radius:8px;padding:0.5rem 1rem;margin:0.3rem 0;">
                        <span style="font-family:'Poppins',sans-serif;font-weight:500;">{label}</span>
                        <span style="color:{color};font-weight:700;font-size:1.1rem;">{score}%</span>
                    </div>""", unsafe_allow_html=True)
                ahmed_avg = round(sum(ahmed_scores.values()) / len(ahmed_scores), 1)
                st.markdown(f"**{name_b}'s family average: {ahmed_avg}%**")
            else:
                st.info(f"Complete {name_b}'s family assessment to see scores.")

        # Combined verdict
        if sara_scores and ahmed_scores:
            st.markdown("---")
            combined = round((sum(sara_scores.values()) + sum(ahmed_scores.values())) /
                             (len(sara_scores) + len(ahmed_scores)), 1)

            color = "#6BAF73" if combined >= 70 else "#E8A846" if combined >= 45 else "#D4577A"
            verdict = "Strong Family Alignment" if combined >= 70 else \
                      "Moderate Family Alignment — Discuss Key Areas" if combined >= 45 else \
                      "Significant Family Friction — Open Conversations Needed"

            st.markdown(f"""
            <div style="background:{color}18;border:2px solid {color}50;border-radius:14px;
                 padding:1.5rem;text-align:center;margin:1rem 0;">
                <div style="font-family:'Playfair Display',serif;font-size:2.5rem;
                     font-weight:700;color:{color};">{combined}%</div>
                <div style="font-family:'Poppins',sans-serif;font-size:1rem;
                     color:{color};font-weight:600;margin-top:0.3rem;">{verdict}</div>
                <div style="font-family:'Poppins',sans-serif;font-size:0.82rem;
                     color:#666;margin-top:0.5rem;">
                    Combined across {len(sara_scores) + len(ahmed_scores)} family members
                </div>
            </div>""", unsafe_allow_html=True)

            # Save to session state for ensemble
            st.session_state["inlaw_score"] = combined
            st.success("✅ Family scores saved — proceed to Results Dashboard!")


main()
