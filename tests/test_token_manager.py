from ai.tokens.token_manager import (
    TokenManager,
)


def test_tokens():

    manager = TokenManager()

    result = manager.estimate(
        "hello world",
    )

    assert result == 2
