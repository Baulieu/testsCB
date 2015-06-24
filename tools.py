"""container for little tools, to prevent v1.py explosion"""
from yaml import load_all

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
from target import Target
from point import Point, Point2
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
        # open("backup.txt", "w").close()  # uncomment to activate backup refresh
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

    def import_targets(self):
        result = Result()
        with open("1435075953418_target.txt") as f:
            temp = f.readlines()
        f.close()
        # open ("1435075953418_target.txt", "w").close()  # TODO uncomment to activate backup refresh
        targets = {}
        for index, line in enumerate(temp):
            n1 = line.split(" | ")  # structure : 0^serial -- 1^information
            n2 = n1[1].split(" ; ")  # structure : 0^detectionTime -- 1^values -- 2^confiance -- 3^1 -- 4^affinite -- 5^bruit -- 6^id_target or 0^detectionTime -- 1^values -- 2^confiance -- 3^1 -- 4^time -- 5^0
            n3 = n2[1].split(" * ")  # structure : 0^x -- 1^y -- 2^z -- 3^length -- 4^width -- 5^area -- 6^H -- 7^S -- 8^V
            if n2[5] == "0":  # new target here
                point = Point2()
                point.time = n2[4]
                point.length = n3[3]
                # point.affinite -> not in this kind of point!
                point.area = n3[3]
                # point.bruit -> not in this kind of point!
                point.confiance = n2[2]
                point.S = n3[7]
                point.H = n3[6]
                point.V = n3[8]
                point.x = n3[0]
                point.y = n3[1]
                point.z = n3[2]
                point.width = n3[4]
                point.target_id = n2[4]
                targets [n2[4]] = Target(n2[4])
                targets [n2[4]].addPoint(point)
            else:
                point = Point2()
                point.time = n2[0]
                point.length = n3[3]
                point.affinite = n2[4]
                point.area = n3[3]
                point.bruit = n2[6]
                point.confiance = n2[2]
                point.S = n3[7]
                point.H = n3[6]
                point.V = n3[8]
                point.x = n3[0]
                point.y = n3[1]
                point.z = n3[2]
                point.width = n3[4]
                point.target_id = n2[6]
                targets [n2[4]].addPoint(point)
        for t in targets.values():
            result.append(t)
        return result






















