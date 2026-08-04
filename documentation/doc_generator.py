from datetime import datetime


class DocumentationGenerator:

    def generate(
        self,
        title,
        content,
    ):

        return {
            "title": title,
            "content": content,
            "generated_at": str(
                datetime.utcnow()
            ),
        }
