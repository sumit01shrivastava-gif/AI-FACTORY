from core.context import Context


def test_context():

    context = Context()

    context.set(
        "name",
        "sumit",
    )

    assert (
        context.get("name")
        == "sumit"
    )
