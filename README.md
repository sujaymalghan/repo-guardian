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

## Installation & Usage

Follow these steps to install and run **RepoGuardian**:

---

### 1. Clone the Repository

```bash
git clone https://github.com/sujaymalghan/repo-guardian.git
cd repo-guardian
```

---

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate           # macOS/Linux
# OR
venv\Scripts\activate              # Windows
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file in the root directory with the following content:

```env
GITHUB_TOKEN=your_github_token
GITHUB_OWNER=your_github_username
PULUMI_ACCESS_TOKEN=your_pulumi_token
PULUMI_CONFIG_PASSPHRASE=
```

> Note: Make sure the GitHub token has access to your repos, and the Pulumi token is valid.

---

### 5. Run the Tool

```bash
python main.py
```

This will:

- Scan all repositories under your GitHub account or organization
- Detect missing `README.md` or `LICENSE` files
- Automatically commit those files using Pulumi

---


