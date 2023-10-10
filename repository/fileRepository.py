import os
import marqo
import config


class FileRepository:
    def __init__(self):
        self.client = marqo.Client(os.getenv("MARQO_URL"))

    def createRecord(self, file, indexName=None):
        if indexName is None:
            indexName = config.file_index

        return self.client.index(indexName).add_documents(
            [file],
            tensor_fields=["filePath", "brainId"]
        )

    def getRecord(self, docId, indexName=None):
        if indexName is None:
            indexName = config.file_index

        try:
            self.client.index(indexName).get_document(
                document_id=docId,
                expose_facets=True
            )
            return True
        except Exception:
            return False
