from ai.prompts.prompt_manager import (
    PromptManager,
)


def test_prompt():

    manager = PromptManager()

    result = manager.build(
        "system",
        "user",
    )

    assert result
