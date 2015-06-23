"""contains the result from a video analysis, extracted from the backup file"""
from target import Target


class Result:

    def __init__(self):
        self.targets = []

    def printMe(self):
        for t in self.targets:
            t.printMe()

    def printMe(self, f):
        for t in self.targets:
            t.printMe(f)

    def append(self, target):
        self.targets.append(target)

    def __iter__(self):
        return self.targets.__iter__()