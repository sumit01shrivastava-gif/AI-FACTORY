from benchmarks.benchmarker import Benchmarker


def test_benchmarker():

    benchmarker = Benchmarker()

    result = benchmarker.benchmark(
        lambda: True
    )

    assert "duration" in result
