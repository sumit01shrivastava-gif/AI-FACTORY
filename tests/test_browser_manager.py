from integrations.browser.browser_manager import (
    BrowserManager,
)


def test_browser():

    browser = BrowserManager()

    result = browser.open(
        "https://example.com"
    )

    assert result["status"] == "success"
