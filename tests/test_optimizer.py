from autonomy.optimizer import Optimizer


def test_optimizer():

    optimizer = Optimizer()

    result = optimizer.optimize(
        {"score": 100}
    )

    assert result["status"] == "optimized"
