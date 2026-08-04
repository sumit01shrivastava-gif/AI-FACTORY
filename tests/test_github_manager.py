from integrations.github.github_manager import (
    GithubManager,
)


def test_github():

    manager = GithubManager()

    files = manager.list_repository_files()

    assert isinstance(
        files,
        list,
    )
