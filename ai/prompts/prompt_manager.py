class PromptManager:

    def build(
        self,
        system,
        user,
    ):

        return f"{system}\n{user}"
