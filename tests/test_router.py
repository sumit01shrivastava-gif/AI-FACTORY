from ai.router.model_router import (
    ModelRouter,
)


def test_router():

    router = ModelRouter()

    result = router.route(
        "openai",
        "hello",
    )

    assert (
        result["provider"]
        == "openai"
    )
