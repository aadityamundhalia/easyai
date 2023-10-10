from Startegy.FilePocessor import FilePocessor
from Startegy.ImageProcessor import ImagePocessor
from repository.fileRepository import FileRepository
from helper.helper import Helper


class UploadService:
    def __init__(self, file, image=False):
        self.helper = Helper()
        self.file = file
        self.image = image
        if image is False:
            self.contentType = file.type
            self.filePath = self.getTempFilePath(file)
            self.fileProcessor = FilePocessor(self.filePath)
        else:
            self.filePath = self.file
            self.ImageProcessor = ImagePocessor(file)

        self.fileRepository = FileRepository()
        self.brainId = 1
        self._id = self.helper.createId(self.brainId, self.filePath)

    def embedFile(self):
        if self.checkIfDocumentExists() is False:
            files = []
            if self.image is False:
                files = self.fileProcessor.process(self.contentType)
            else:
                items = self.ImageProcessor.process().get('items')
                for row in items:
                    files.append(row['_id'])

            if type(files) == list:
                record = self.fileRepository.createRecord({
                    "filePath": self.filePath,
                    "brainId": self.brainId,
                    "documents": files,
                    "_id": self._id,
                })
                files.append(record)
                if self.image is False:
                    self.helper.deleteFile(self.filePath)

                return files

            return files

        return "document already exist"

    def getTempFilePath(self, file):
        return self.helper.createFile(file)

    def checkIfDocumentExists(self):
        return self.fileRepository.getRecord(self._id)
