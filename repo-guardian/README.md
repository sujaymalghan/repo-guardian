# RepoGuardian – GitHub Repository Linter and Auto-Fixer

RepoGuardian is a Python-based automation tool that audits and fixes common hygiene issues across GitHub repositories. It scans all repositories in a GitHub account or organization, detects missing standard files (like README and LICENSE), and automatically commits them using Pulumi’s GitHub Provider and Automation API.

This project was built for the "Get Creative with Pulumi + GitHub" Hackathon.

---

## Overview

RepoGuardian addresses a common challenge in GitHub repository management: maintaining consistency and proper documentation across multiple repositories.

It uses Pulumi's infrastructure-as-code approach not for cloud resources, but to programmatically manage and correct GitHub repositories.

---

## Features

- Scans all repositories in a GitHub account or organization
- Detects:
  - Missing `README.md`
  - Missing `LICENSE`
- Automatically fixes the issues by committing files using Pulumi
- Skips empty repositories with no commits
- Fully automated using Pulumi Automation API
- Requires no Pulumi CLI usage

---

## Technology Stack

- Python 3.x
- Pulumi Automation API
- Pulumi GitHub Provider
- PyGitHub
- dotenv

---

## Installation Instructions

1. **Clone the repository**

```bash
git clone https://github.com/sujaymalghan/repo-guardian.git
cd repo-guardian

2. python -m venv venv
source venv/bin/activate  
# or venv\Scripts\activate on Windows

3.pip install -r requirements.txt

4. Add tokens to .env files give access to github account

5. python main.py

