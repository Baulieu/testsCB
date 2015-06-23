"""class for a target, contains a list of points"""


class Target:

    points = []

    def __init__(self, identity):
        self.id = identity

    def addPoint(self, point):
        self.points.append(point)

    def size(self):
        return self.points.__len__()

    def printMe(self):
        print(self.id)
        for p in self.points:
            p.printMe()

    def printMe(self, f):
        print(self.id, self.points.__len__(), file=f)
        # for p in self.points:
        #     p.printMe(f)

    def getId(self):
        return self.id

    def __iter__(self):
        return self.points.__iter__()