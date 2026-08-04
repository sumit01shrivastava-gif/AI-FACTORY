from runtime.sandboxes.sandbox_manager import (
    SandboxManager,
)


def test_sandbox():

    sandbox = SandboxManager()

    assert sandbox is not None
