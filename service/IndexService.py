from repository.IndexRepository import IndexRepository
from helper.helper import Helper
import config


class IndexService:
    def __init__(self, indexName=''):
        self.index_name = indexName
        self.helper = Helper()
        self.indexRepository = IndexRepository(self.index_name)

    def deleteIndex(self):
        return self.indexRepository.deleteIndex()

    def createIndex(self):
        return self.indexRepository.createIndex()

    def listIndex(self):
        return self.indexRepository.listIndex()

    def getDocuments(self, query):
        return self.indexRepository.getAllItems(query)

    def deleteDocument(self, fileName):
        fileHash = self.helper.createId(1, fileName)
        fileIds = self.indexRepository.getdocumentIds(
            fileHash,
            config.file_index
        )
        self.indexRepository.deleteDocument(fileIds, self.index_name)
        self.indexRepository.deleteDocument([fileHash], config.file_index)

        return "file deleted"
