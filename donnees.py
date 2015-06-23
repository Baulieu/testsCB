""" contains all the data collected during the tests """


from result import Result


class Donnees:

    def __init__(self, name):
        self.name = name
        self.data = []

    def appendResult(self, name, result):
        self.data.append((name, result))
        self.last = (name, result)

    def printMe(self, f):
        print(self.name, file=f)
        for d in self.data:
            i = 0
            for x in d:
                if i == 0:
                    print(x, file=f)
                else:
                    x.printMe(f)
                i += 1

    def printLast(self, f):
        i = 0
        for x in self.last:
            if i == 0:
                print(x, file=f)
            else:
                x.printMe(f)
            i += 1