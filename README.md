
# 🧭 AI-based Career Guidance — Starter Project

Minimal, resume-ready project that recommends career roles based on your skills, with a rule-based engine and optional LLM refinement.

## What it does
- Input: your skills + interests
- Output: top 3 matching roles, missing core skills, starter resources, beginner projects
- Plus: a simple 30/60/90-day learning plan, and (optional) LLM coaching

## Quick Start
1. **Install**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run**
   ```bash
   streamlit run app.py
   ```

3. **(Optional) Enable LLM Coaching**
   - Set environment variables:
     - `OPENAI_API_KEY="your_key"`
     - For **Azure OpenAI**, also set:
       - `OPENAI_BASE_URL="https://<your-azure-endpoint>/openai/deployments/<your-deployment>/chat/completions?api-version=<YYYY-MM-DD>"`
       - `OPENAI_MODEL="<your-deployment-name>"`
   - The app will use the OpenAI-compatible client. If unset, the app still works with rule-based logic.

## Files
- `data/roles.csv` — small curated dataset of roles/skills/resources
- `app.py` — Streamlit app (rule-based ranking + optional LLM)
- `prompts/` — space for your custom prompt templates
- `requirements.txt` — minimal dependencies

## Customize (5–10 minutes)
- Add/remove roles or refine skills in `data/roles.csv`
- Edit the scoring formula in `app.py` (e.g., weight your target role more heavily)
- Update the learning plan text in `make_learning_plan()`
- Swap in your own resources or portfolio ideas

## Safe to demo
- Works entirely offline using rule-based scoring
- LLM is strictly optional (for richer career coaching text)

## Resume blurb (example)
> Built an AI-based career guidance app using Python and Streamlit. Implemented a rule-based engine to recommend roles from a curated skills dataset and generated 30/60/90-day learning plans. Added optional LLM refinement via an OpenAI-compatible API (including Azure OpenAI).

