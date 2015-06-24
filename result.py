"""contains the result from a video analysis, extracted from the backup file"""
from target import Target


class Result:

    def __init__(self):
        self.liste = []

    def printMe(self):
        for t in self.targets:
            t.printMe()

    def printMe(self, f):
        for t in self.targets:
            t.printMe(f)

    # def appendTarget(self, target):
    #     self.targets.append(target)
    
    def addListTarget(self, tt):
        self.liste.append(tt)

    def okcestbon(self):
        self.targets = [Target(id) for id in self.liste]
    
    def __iter__(self):
        return self.targets.__iter__()

    def addPoint(self, new):
        for t in self.targets:
            if t.getId() == new.target_id:
                t.addPoint(new)
