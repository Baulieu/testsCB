"""class for a point, containing regular informations for an object detected in a frame"""


class Point:

    def __init__(self,target, time, frame, x, y, z, h, w, H, S, V, surface):
        self.target = target
        self.time = time
        self.frame = frame
        self.x = x
        self.y = y
        self.z = z
        self.h = h
        self.w = w
        self.H = H
        self.S = S
        self.V = V
        self.surface = surface

    def __init__(self, target, string):
        self.target = target
        str = string.split("*")
        self.x = str[0]
        self.y = str[1]
        self.z = str[2]
        self.time = str[3]
        self.h = str[4]
        self.w = str[5]
        self.H = str[6]
        self.S = str[7]
        self.V = str[8]
        # TODO add frames and target surface

    def whichTarget(self):
        return self.target

    def printMe(self):
        print(self.x , self.y , self.z, self.time, self.h, self.h, self.w, self.H, self.S, self.V)

    def printMe(self, f):
        print(self.x , self.y , self.z, self.time, self.h, self.h, self.w, self.H, self.S, self.V, file=f)

    def getZ(self):
        return float(self.z)

    def getHeight(self):
        return float(self.h)

    def getTime(self):
        return float(self.time)

class Point2:

    def __init__(self):
        self.time = None
        self.x = None
        self.y = None
        self.z = None
        self.length = None
        self.width = None
        self.H = None
        self.S = None
        self.V = None
        self.area = None
        self.confiance = None
        self.affinite = None
        self.bruit = None
        self.target_id = None

    def whichTarget(self):
        return self.target_id

    def printMe(self, f):
        print(self.time, self.x, self.y, self.z, self.h, self.s, self.v, self.area, self.confiance, self.affinite, self.bruit)

    def getZ(self):
        return float(self.z)

    def getHeight(self):
        return float(self.length)

    def getTime(self):
        return self.time