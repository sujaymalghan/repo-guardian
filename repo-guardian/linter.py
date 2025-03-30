def lint_repo(repo):
    issues = []

    try:
        default_branch = repo.default_branch
        print(f"{repo.name} default branch: {default_branch}")
    except:
        issues.append("missing_main_or_master")
    try:
        repo.get_readme()
    except:
        issues.append("missing_readme")

    try:
        repo.get_license()
    except:
        issues.append("missing_license")

    return issues
