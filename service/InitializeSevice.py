from repository.IndexRepository import IndexRepository
import config


class InitializeSevice:
    def __init__(self):
        self.indexRepository = IndexRepository()

    def initialize(self):
        print("Creating {}".format(config.index_name))
        self.indexRepository.createIndex(config.index_name)

        print("Creating {}".format(config.file_index))
        self.indexRepository.createIndex(config.file_index)

    def reset(self):
        print("Deleting {}".format(config.index_name))
        self.indexRepository.deleteIndex(config.index_name)

        print("Deleting {}".format(config.file_index))
        self.indexRepository.deleteIndex(config.file_index)
