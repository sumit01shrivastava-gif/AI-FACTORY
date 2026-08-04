class Retriever:

    def retrieve(
        self,
        query,
        documents,
    ):

        results = []

        query = query.lower()

        for document in documents:

            if query in document.lower():

                results.append(
                    document
                )

        return results
