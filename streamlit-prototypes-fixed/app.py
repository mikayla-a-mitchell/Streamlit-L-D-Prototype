"""Reviewer-facing host for two interactive mathematics learning prototypes."""

from html.parser import HTMLParser
from pathlib import Path
from typing import List, Optional, Tuple

import streamlit as st
import streamlit.components.v1 as components


BASE_DIR = Path(__file__).resolve().parent
PROTOTYPE_DIR = BASE_DIR / "prototypes"

PROTOTYPES = {
    "Split Decision": {
        "file": "split-decision.html",
        "eyebrow": "FEATURED PROTOTYPE  ·  GRADE 6",
        "title": "Split Decision",
        "description": (
            "A familiar pizza-ordering challenge that develops expression writing, "
            "grouping, the distributive property, and equivalence through prediction "
            "and immediate visual feedback."
        ),
        "focus": "Expressions & Equations · CCSS 6.EE.A.2 and 6.EE.A.3",
    },
    "Assembly X": {
        "file": "assembly-x.html",
        "eyebrow": "ALTERNATE PROTOTYPE  ·  GRADE 6",
        "title": "Assembly X",
        "description": (
            "An experimental expression factory in which a literal machine exposes "
            "ambiguous instructions and rewards precise mathematical reasoning."
        ),
        "focus": "Expressions & Equations · Structure, equivalence, and counterexamples",
    },
}


st.set_page_config(
    page_title="Mathematics Learning Design Prototypes",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        .stApp {
            background:
                radial-gradient(circle at 4% 0%, rgba(83, 171, 255, 0.11), transparent 26rem),
                #f7f8fa;
        }
        .block-container {
            max-width: 1260px;
            padding-top: 2.25rem;
            padding-bottom: 3rem;
        }
        .portfolio-kicker {
            color: #536172;
            font-size: 0.76rem;
            font-weight: 750;
            letter-spacing: 0.14em;
            margin-bottom: 0.55rem;
        }
        .portfolio-title {
            color: #151a21;
            font-size: clamp(2rem, 4vw, 3.25rem);
            font-weight: 780;
            letter-spacing: -0.045em;
            line-height: 1.02;
            margin: 0;
        }
        .portfolio-intro {
            color: #596574;
            font-size: 1.03rem;
            line-height: 1.62;
            max-width: 760px;
            margin: 0.9rem 0 1.5rem;
        }
        .prototype-card {
            background: rgba(255, 255, 255, 0.88);
            border: 1px solid #e1e6ec;
            border-radius: 18px;
            box-shadow: 0 14px 42px rgba(22, 32, 45, 0.07);
            margin: 1.1rem 0 0.75rem;
            padding: 1.25rem 1.4rem;
        }
        .prototype-eyebrow {
            color: #2773c7;
            font-size: 0.7rem;
            font-weight: 800;
            letter-spacing: 0.12em;
        }
        .prototype-name {
            color: #161b22;
            font-size: 1.55rem;
            font-weight: 750;
            letter-spacing: -0.025em;
            margin: 0.25rem 0 0.35rem;
        }
        .prototype-description {
            color: #525f6d;
            line-height: 1.55;
            margin: 0;
            max-width: 850px;
        }
        .prototype-focus {
            color: #31445a;
            font-size: 0.84rem;
            font-weight: 650;
            margin-top: 0.7rem;
        }
        div[data-testid="stRadio"] > label {
            color: #536172;
            font-size: 0.82rem;
            font-weight: 700;
        }
        div[data-testid="stExpander"] {
            background: rgba(255, 255, 255, 0.72);
            border-color: #e1e6ec;
        }
        iframe[title="streamlit.components.v1.html"] {
            background: white;
            border: 1px solid #dfe5ec;
            border-radius: 18px;
            box-shadow: 0 16px 48px rgba(22, 32, 45, 0.08);
        }
        footer { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)


class _SrcdocExtractor(HTMLParser):
    """Extract the interactive document from a standalone prototype wrapper."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.srcdoc: Optional[str] = None

    def handle_starttag(
        self, tag: str, attrs: List[Tuple[str, Optional[str]]]
    ) -> None:
        if tag != "iframe" or self.srcdoc is not None:
            return
        attributes = dict(attrs)
        if attributes.get("srcdoc"):
            self.srcdoc = attributes["srcdoc"]


@st.cache_data(show_spinner=False)
def load_prototype(filename: str) -> str:
    """Load a trusted local prototype and remove any redundant iframe wrapper."""
    candidates = (PROTOTYPE_DIR / filename, BASE_DIR / filename)
    prototype_path = next((path for path in candidates if path.is_file()), None)
    if prototype_path is None:
        checked = ", ".join(str(path.relative_to(BASE_DIR)) for path in candidates)
        raise FileNotFoundError(f"Missing {filename}. Checked: {checked}")

    standalone_html = prototype_path.read_text(encoding="utf-8")
    extractor = _SrcdocExtractor()
    extractor.feed(standalone_html)

    # The exported prototype is already a standalone page containing an iframe.
    # Streamlit supplies its own iframe, so render the inner document directly.
    return extractor.srcdoc or standalone_html


st.markdown(
    """
    <div class="portfolio-kicker">MATHEMATICS LEARNING DESIGN PORTFOLIO</div>
    <h1 class="portfolio-title">Interactive prototypes</h1>
    <p class="portfolio-intro">
        Two short explorations of how digital interaction can make mathematical
        structure visible, create productive surprise, and respond meaningfully to
        a learner's choices.
    </p>
    """,
    unsafe_allow_html=True,
)

selection = st.radio(
    "Choose an experience",
    options=list(PROTOTYPES),
    horizontal=True,
    index=0,
)

prototype = PROTOTYPES[selection]
st.markdown(
    f"""
    <section class="prototype-card">
        <div class="prototype-eyebrow">{prototype['eyebrow']}</div>
        <div class="prototype-name">{prototype['title']}</div>
        <p class="prototype-description">{prototype['description']}</p>
        <div class="prototype-focus">{prototype['focus']}</div>
    </section>
    """,
    unsafe_allow_html=True,
)

with st.expander("About these samples"):
    st.markdown(
        """
        These are independent, functional prototypes created to demonstrate an
        approach to mathematics learning design. They are not commissioned work
        and are not affiliated with Brilliant. Both experiences are designed for
        exploration on a laptop or tablet; they preserve learner choices only for
        the current session.

        **Suggested review:** Begin with **Split Decision**, then compare how
        **Assembly X** uses the same mathematical core in a more abstract setting.
        """
    )

try:
    prototype_html = load_prototype(prototype["file"])
except (FileNotFoundError, OSError) as error:
    st.error(f"The prototype could not be loaded. {error}")
else:
    components.html(prototype_html, height=1080, scrolling=True)

st.caption(
    "Independent portfolio samples · Grade 6 mathematics · Interactive prototype status"
)
