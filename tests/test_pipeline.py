from execution.pipeline.pipeline import (
    ExecutionPipeline,
)


def test_pipeline():

    pipeline = ExecutionPipeline()

    pipeline.add_stage(
        lambda: True
    )

    result = pipeline.execute()

    assert result[0]
