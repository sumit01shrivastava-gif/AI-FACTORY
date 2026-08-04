class ContextEngine:

    def build(self, project):

        return {
            "project": project,
            "repository": f"repositories/{project}",
        }
