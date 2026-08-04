from analytics.scoring_engine import (
    ScoringEngine,
)


def test_scoring():

    engine = ScoringEngine()

    result = engine.calculate(
        95,
    )

    assert result == "excellent"
