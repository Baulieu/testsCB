"""container for little tools, to prevent v1.py explosion"""
from yaml import load_all

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
from target import Target
from point import Point
from result import Result


class Tools:
    def __init__(self):
        self.alive = True

    def openYml(self, name):
        source = open(name, "r")
        return load_all(source)  # load_all function from pyYaml package
        source.close()

    def openBackup(self):  # WARNING -> obsolete, use targets and performance
        result = Result()
        tarTemp = Target(0)
        with open("backup.txt") as f:
            temp = f.readlines()
        f.close()
        # open("backup.txt", "w").close()  # TODO uncomment to activate backup refresh
        for index, line in enumerate(temp):  # on parcourt toutes les lignes du fichier
            if line.__len__() > 10 and line[:1] == "|":  # la ligne ne contient pas qu'un |
                if index < temp.__len__() - 1 and temp[index + 1][:13] != line[:13]: # on est pas sur une ligne partielle
                    line = line.split(",")
                    tarTemp = Target(line[0][1:])
                    lineb = line[1].split("/")
                    print(lineb.__len__())
                    for p in lineb:
                        tempPoint = Point(line[0][1:], p)
                        tarTemp.addPoint(tempPoint)
                        del tempPoint
                    result.append(tarTemp)
        return result

    # def targets(self):
    #     result = Result()
    #     return 0