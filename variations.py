""" contains the list of interesting parameters to be tested, extracted from the variations.txt file"""


class Variations:

    def __init__(self):
        self.parameters = []
        # order:
        # 0 -> name
        # 1 -> standard value
        # 2 -> starting value
        # 3 -> iteration
        # 4 -> number of iterations

    def importation(self):
        with open("variations.txt") as f:
            temp = f.readlines()
        f.close()
        for line in temp:
            line = line.split(" ")
            self.parameters.append((line[0], line[1], line[2], line[3], line[4], line[5]))


    def __iter__(self):
        return iter(self.parameters)