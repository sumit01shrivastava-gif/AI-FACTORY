from security.security_manager import (
    SecurityManager,
)


def test_security():

    manager = SecurityManager()

    assert manager.authorize(
        "admin"
    )
