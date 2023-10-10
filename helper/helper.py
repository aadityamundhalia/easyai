import os
import hashlib


class Helper:
    def createFile(self, file):
        fileLocation = f"temp/{file.name}"
        with open(fileLocation, "wb+") as fileObject:
            fileObject.write(file.getbuffer())

        return fileLocation

    def deleteFile(self, filePath):
        os.remove(filePath)

    def createId(self, brainId, filepath):
        return str(
            hashlib.md5(
                str(
                    str(brainId)+"-"+filepath
                ).encode()
            ).hexdigest()
        )
