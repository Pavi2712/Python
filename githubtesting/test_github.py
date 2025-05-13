# import click
import pytest
# from typing import List
from playwright.sync_api import APIRequestContext

# Fixture to create APIRequestContext
@pytest.fixture(scope="session")
def api_context(playwright) -> APIRequestContext:
    context = playwright.request.new_context(
        base_url="https://api.github.com",
        extra_http_headers={"Authorization": "Bearer"}
        # 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
        # http_credentials={
        #     "username": "Pavi2712",  
        #     "password": "Pavi@2712",
        #     "send": "unauthorized"
        # }
    )
    yield context
    context.dispose()

def test_repo_list(api_context: APIRequestContext):
    response = api_context.get(f"/user/repos")
    assert response.ok
    assert len(response.json()) == 3
































# # Test function
# @pytest.mark.parametrize("repo_urls", [
#     [
#         "https://github.com/Pavi2712/Python",
#         "https://github.com/Pavi2712/jenkins_sample",
#         "https://github.com/Pavi2712/helloworld"
#     ]
# ])
# def test_repo_names(api_context: APIRequestContext, repo_urls: List[str]):
#     repo_names = []

    # for repo_url in repo_urls:
    #     try:
    #         _, _, username, repo_name = repo_url.rstrip('/').split('/')[-4:]
    #     except ValueError:
    #         pytest.fail(f"Invalid URL format: {repo_url}")

    #     response = api_context.get(f"/repos/{username}/{repo_name}")

    #     if response.status == 200:
    #         repo_names.append(repo_name)
    #     else:
    #         pytest.fail(f"Failed to fetch {repo_name} for user {username}. HTTP Status: {response.status}. Response: {response.text()}")

    # assert len(repo_names) > 0, "No repositories were fetched."

    # # Print the fetched repository names using click.echo
    # click.echo(f"\n Repository Names: {repo_names}\n")
