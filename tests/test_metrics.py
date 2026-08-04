from metrics.metrics_manager import (
    MetricsManager,
)


def test_metrics():

    manager = MetricsManager()

    manager.record(
        "score",
        100,
    )

    assert manager.fetch()["score"] == 100
