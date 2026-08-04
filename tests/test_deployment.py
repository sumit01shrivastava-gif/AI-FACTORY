from deployment.deployment_engine import (
    DeploymentEngine,
)


def test_deployment():

    engine = DeploymentEngine()

    result = engine.deploy(
        "1.0.0"
    )

    assert result["status"] == "success"
