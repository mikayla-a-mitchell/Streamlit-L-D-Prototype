# Mathematics Learning Design Prototypes

This Streamlit app presents two independent, interactive Grade 6 mathematics
learning-design prototypes in one reviewer-friendly portfolio experience.

- **Split Decision** — the featured, familiar-context experience
- **Assembly X** — an alternate, more abstract expression-factory experience

Both prototypes explore expression writing, grouping, the distributive property,
equivalence, and mathematical precision. They are original portfolio samples and
are not commissioned by or affiliated with Brilliant.

## Project structure

```text
streamlit-prototypes/
├── app.py
├── requirements.txt
└── prototypes/
    ├── assembly-x.html
    └── split-decision.html
```

Keep this structure intact: `app.py` reads the two local HTML files at runtime.

## Run locally

From this folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run app.py
```

Streamlit will print a local address, usually `http://localhost:8501`.

## Deploy on Streamlit Community Cloud

1. Copy this entire folder into the GitHub repository you want to deploy and
   commit all four files.
2. Sign in at [share.streamlit.io](https://share.streamlit.io/).
3. Select **Create app**, then choose the repository and branch.
4. For the entrypoint, use `app.py` if these files are at the repository root, or
   `streamlit-prototypes/app.py` if you kept this folder inside an existing repo.
5. Deploy and share the generated public URL with reviewers.

The dependency version is pinned to a verified, installable release so the
prototypes continue to use Streamlit's HTML component API consistently. If the
prototype files change, commit and push the updated files; Community Cloud will
redeploy the app.

Official references:

- [Deploy an app](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy)
- [Organize files for Community Cloud](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/file-organization)
