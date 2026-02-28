# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Collection of Project Euler solutions in Python 3. No external dependencies — all solutions use only the Python standard library.

## Running Solutions

```bash
python3 euler<N>.py    # e.g., python3 euler1.py
```

## Linting and Formatting

```bash
ruff check .          # lint
ruff format .         # format
ruff check --fix .    # auto-fix lint issues
```

Config is in `pyproject.toml`. Rules: E (pycodestyle errors), F (pyflakes), W (pycodestyle warnings).

## Code Structure

Flat layout — each file (`euler1.py` through `euler11.py`) is a standalone script solving one Project Euler problem. No shared modules or imports between files.

## Commit Convention

Use [Conventional Commits](https://www.conventionalcommits.org/): `<type>: <description>`

Types: `feat`, `fix`, `refactor`, `style`, `docs`, `chore`, `test`
