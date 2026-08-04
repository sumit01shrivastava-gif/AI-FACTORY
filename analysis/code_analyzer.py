class CodeAnalyzer:

    def analyze(
        self,
        source,
    ):

        lines = source.splitlines()

        return {
            "lines": len(lines),
            "characters": len(source),
        }
