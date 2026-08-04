from workflow.engine import WorkflowEngine


def test_workflow():

    workflow = WorkflowEngine()

    workflow.add_step(
        lambda: "hello"
    )

    result = workflow.execute()

    assert result[0] == "hello"
