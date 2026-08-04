from audit.audit_manager import (
    AuditManager,
)


def test_audit():

    manager = AuditManager()

    manager.log(
        "created",
    )

    assert len(
        manager.retrieve()
    ) == 1
