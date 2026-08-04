class PromptBuilder:

    def build(
        self,
        project,
        task,
        architecture,
    ):

        return f"""
Project:

{project}

Task:

{task}

Architecture:

{architecture}

Requirements:

- Follow existing architecture.
- Preserve coding standards.
- Create tests.
- Update documentation.
"""
