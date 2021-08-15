import os

class InstallerWindowModel:
    pathToSkyrim: str
    skyrimVersion: str
    skseVersion: str
    canInstall: bool

    def __init__(self):
        pass

    def getCanInstall(self):
        return self.canInstall

    def setCanInstall(self, value: bool):
        self.canInstall = value


    def getSKSEVersion(self):
        return self.skseVersion

    def setSKSEVerion(self, value: str):
        self.skseVersion = value


    def getSkyrimVersion(self):
        return self.skyrimVersion

    def setSkyrimVersion(self, value: str):
        self.skyrimVersion = value


    def getPathToSkyrim(self):
        return self.pathToSkyrim

    def setPathToSkyrim(self, value: str):
        self.pathToSkyrim = value

    # def onPropertyChanged(self, propertyName: str = null):
    #     PropertyChanged.Invoke