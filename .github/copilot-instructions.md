# Copilot instructions for this repository

Purpose
- Help AI coding agents become productive quickly in this repository by documenting discovered structure, developer workflows, and explicit instructions to avoid guesswork.

Repository snapshot
- Repo name: `data-engineer` (small/early-stage). Current branch: `main`.
- Primary file present: `README.md` (contains project title only). No `src/`, `tests/`, `pyproject.toml`, or package manifests detected.

Big picture (what to assume and verify)
- This repo currently has minimal content. Before making non-trivial changes, verify with the human owner whether there are expected folders (e.g., `src/`, `notebooks/`, `data/`) or external artifacts not checked in.
- Do not assume a language, build system, or test framework until you find configuration files (`requirements.txt`, `pyproject.toml`, `package.json`, `setup.py`, `Makefile`, `.github/workflows/`). If none present, ask the user.

When exploring code
- Start with `README.md` for project intent (here it's minimal). Next, scan for common manifests: `requirements.txt`, `pyproject.toml`, `package.json`, `Dockerfile`, `.github/workflows/`, and any `src/` or `notebooks/` directories.
- Use these concrete repo checks in generated tasks or PR descriptions (example: "No tests found; confirm preferred test framework (pytest/tox) before adding tests").

Developer workflows (explicit)
- Branching: use `main` as default branch. Create feature branches for changes.
- Tests & build: none detected. Before adding CI or tests, confirm preferred tooling. If asked to add CI, propose a minimal GitHub Actions workflow and request approval.
- Running commands: avoid running non-existent build/test commands. If asked to execute code, request the environment details and dependency list.

Code and PR guidance for the agent
- Keep changes minimal and well-scoped. When adding new files (e.g., code, tests, CI), include a short note in `README.md` describing how to run them.
- Every PR should include:
  - A short summary of intent
  - Files changed and why
  - If new dependencies added, exact install commands
  - Manual verification steps (if automated tests are absent)

Patterns & conventions (project-specific)
- No project-specific code patterns were discoverable from repository contents. Default to idiomatic patterns for the language you are working in, but always confirm before enforcing them.

Integration points & dependencies
- No external integrations or dependencies are present in the repository metadata. If you add integrations (APIs, databases, cloud infra), document connection details, required secrets, and local dev stubs in `README.md`.

When you are unsure
- Pause and ask the repository owner a concise question. Example prompts:
  - "Are there expected source folders (e.g., `src/` or `notebooks/`) not checked in?"
  - "Which language and test framework should I use if I add code/tests?"

Files to check when starting work
- `README.md`
- Any of: `requirements.txt`, `pyproject.toml`, `package.json`, `setup.py`, `Pipfile`, `Dockerfile`, `.github/workflows/*`

Final note
- This file is intentionally conservative: the repository is minimal. Ask targeted questions rather than making broad assumptions. If you want, I can extend these instructions after you add more project files.
