from dotenv import load_dotenv
import os
from github import Github
from linter import lint_repo
from fixer import fix_repo

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_OWNER = os.getenv("GITHUB_OWNER")

def run_lint_and_fix():
    gh = Github(GITHUB_TOKEN)
    user = gh.get_user(GITHUB_OWNER)
    repos = user.get_repos()

    for repo in repos:
        try:
            branch = repo.default_branch
            repo.get_commits()[0]
        except Exception:
            print(f"{repo.name} skipped: repo is empty (no commits)")
            continue

        problems = lint_repo(repo)

        if problems:
            print(f"{repo.name} has issues: {problems}")
            fix_repo(repo.name, problems, branch=branch)
        else:
            print(f"{repo.name} passed all checks.")

if __name__ == "__main__":
    run_lint_and_fix()
