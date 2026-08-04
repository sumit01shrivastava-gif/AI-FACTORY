class SecurityManager:

    def authorize(
        self,
        role,
    ):

        return role == "admin"
