from execution.repositories.repository_editor import (
    RepositoryEditor,
)


class RepositoryModifier:

    def __init__(self):

        self.editor = RepositoryEditor()

    def modify(
        self,
        filename,
        content,
    ):

        self.editor.append(
            filename,
            content,
        )
