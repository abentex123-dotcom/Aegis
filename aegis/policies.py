class ResponsePolicy:
    """Post-processing policy for assistant responses."""

    def apply(self, response: str) -> str:
        return response.strip()
