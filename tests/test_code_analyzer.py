from analysis.code_analyzer import (
    CodeAnalyzer,
)


def test_analyzer():

    analyzer = CodeAnalyzer()

    result = analyzer.analyze(
        "print('hello')"
    )

    assert result["lines"] == 1
