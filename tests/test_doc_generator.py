from documentation.doc_generator import (
    DocumentationGenerator,
)


def test_documentation():

    generator = (
        DocumentationGenerator()
    )

    result = generator.generate(
        "test",
        "content",
    )

    assert result["title"] == "test"
