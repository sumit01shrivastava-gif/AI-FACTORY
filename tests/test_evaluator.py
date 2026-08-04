from autonomy.evaluator import Evaluator


def test_evaluator():

    evaluator = Evaluator()

    result = evaluator.evaluate(
        {"test": True}
    )

    assert result["score"] == 100
