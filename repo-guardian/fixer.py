import os
import pulumi.automation as auto


def fix_repo(repo_name, missing_items, branch="main"):
    def pulumi_program():
        import pulumi_github as github

        if "missing_readme" in missing_items:
            github.RepositoryFile(
                "readme-file",
                repository=repo_name,
                file="README.md",
                content="# Project\n\nThis is a default README.",
                branch=branch,
                commit_message="Add README via RepoGuardian",
            )

        if "missing_license" in missing_items:
            github.RepositoryFile(
                "license-file",
                repository=repo_name,
                file="LICENSE",
                content="""MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy...""",
                branch=branch,
                commit_message="Add LICENSE via RepoGuardian",
            )

    stack_name = f"fix-{repo_name.replace('/', '-')}"
    project_name = "repo-guardian"

    os.environ["PULUMI_ACCESS_TOKEN"] = os.getenv("PULUMI_ACCESS_TOKEN")
    os.environ["PULUMI_CONFIG_PASSPHRASE"] = os.getenv("PULUMI_CONFIG_PASSPHRASE", "")
    os.environ["GITHUB_OWNER"] = os.getenv("GITHUB_OWNER")

    stack = auto.create_or_select_stack(
        stack_name=stack_name,
        project_name=project_name,
        program=pulumi_program,
    )

    token = os.getenv("GITHUB_TOKEN")
    stack.set_config("github:token", auto.ConfigValue(value=token))

    print(f"Applying fixes to: {repo_name}")
    result = stack.up()
    print("Fix complete.")
