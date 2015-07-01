""" KPIs calculation -- convention : every KPI should be around 10"""
from parameters import Parameters


class Analysis:

    def __init__(self):
        self.good = none
        self.imgs = None
        self.tauxProfondeur = None
        self.fiabiliteTaille = None
        self.nbTargets = None
        self.nbPoints = None
        self.nbPertes = None
        self.perf = None

    def addResult(self, result):
        self.result = result

    def add_frames(self, frames):
        self.frames = frames

    def calcImgs(self):
        return float(self.frames.__len__()) / (float(self.frames[self.frames.__len__() - 1][2]) - float(self.frames[0][2]))

    def falseP(self):
        temp = self.result.liste.values()
        return temp.__len__() - self.good.__len__()

    def calcFiabTaille(self, alpha):
        j = 0
        n = 0
        for t in self.result.liste.values():
            moy = 0
            i = 0
            for p in t:
                moy += p.getHeight()
                i += 1
                j += 1
            if i != 0:
                moy = moy / i
            for p in t:
                if p.getHeight() < moy - alpha or p.getHeight() > moy + alpha:
                    n += 1
        # if j == 0:
        #     return n
        else:
            return n / j * 10  # proportion of bad results

    def calcNbTargets(self):
        return self.good.__len__()

    def calcNbPoints(self):
        i = 0
        j = True
        for t in self.result.liste.values():
            if id(t) in self.good:
                for p in t:
                    i += 1
        if j:
            raise NameError("problème de reconnaissance des targets! (dans analyse, fonction calculNbPoints")
        return i

    def calcNbPertes(self):
        classeur = []
        i = 0
        while i < self.calcNbPoints():
            classeur.append(False)
            i += 1
        i = 1
        count = 0
        previous = False
        for t in self.result.liste.values():
            if id(t in self.good):
                for c in classeur:
                    c = false
                i = 0
                for p in t:
                    while self.frames[i-1][2] >= p.getTime():
                        i += 1
                    classeur[i] = True
                for c in classeur:
                    if previous:
                        if c == False:
                            count += 1
                    previous = c
        return count

    def perfIndice(self):
        result = self.imgs / 60
        result += self.tauxProfondeur / 100
        result += self.fiabiliteTaille / 50
        result += self.nbPoints / 25
        result += self.nbTargets / 25
        result -= self.nbPertes
        result -= self.falseP()
        return result

    def recalc(self):
        self.imgs = self.calcImgs()
        self.tauxProfondeur = 1
        self.fiabiliteTaille = self.calcFiabTaille()
        self.nbTargets = self.calcNbTargets()
        self.nbPoints = self.calcNbPoints()
        self.nbPertes = self.calcNbPertes()
        self.perf = self.perfIndice()

    def addGoodTarget(self, line):
        self.good = line.split(" ")
        for t in self.good:
            t = float(t)

    def id(self, target):
        return target.getId()%10000


class Analysis2:

    def __init__(self, name, settings):
        self.name = name
        self.result = None
        self.falsep = 0
        self.imgs = None
        self.tauxProfondeur = None
        self.fiabiliteTaille = None
        self.nbTargets = None
        self.nbPoints = None
        self.nbPertes = None
        self.perf = 0
        self.settings = settings
        self.frames = []
        self.good = []

        """def __init__(self, name, result):
        self.name = name
        self.result = result
        self.falsep = 0
        self.imgs = self.calcImgs()
        self.tauxProfondeur = self.calcProfondeur()
        self.fiabiliteTaille = self.calcFiabTaille(0.5)
        self.nbTargets = self.calcNbTargets()
        self.nbPoints = self.calcNbPoints()
        self.nbPertes = self.calcNbPertes()
        self.perf = self.perfIndice()"""

    def addFalsep(self, falsep):
        self.falsep = falsep

    def addResult(self, result):  # filling the object data
        self.result = result
        self.imgs = self.calcImgs()
        self.tauxProfondeur = self.calcProfondeur()
        self.fiabiliteTaille = self.calcFiabTaille(0.5)
        self.nbTargets = self.calcNbTargets()
        self.nbPoints = self.calcNbPoints()
        self.nbPertes = self.calcNbPertes()

    def add_frames(self, frames):
        self.frames = frames

    def calcImgs(self):  # frames analyzed per second -> Ok
        return float(self.frames.__len__()) / (float(self.frames[self.frames.__len__() - 1][2]) - float(self.frames[0][2]))

    def calcProfondeur(self):  # success proportion for depth recuperation -> Ok
        i = 0
        j = 0
        for t in self.result.liste.values():
            if id(t) in self.good:
                for p in t:
                    if p.getZ() ==0:
                        i += 1
                    j += 1
        if j == 0:
            return i
        else:
            return ( j - i ) / j * 10

    def calcFiabTaille(self, alpha):
        # reliability of height -> Ok
        j = 0
        n = 0
        for t in self.result.liste.values():
            moy = 0
            i = 0
            for p in t:
                moy += p.getHeight()
                i += 1
                j += 1
            if i != 0:
                moy = moy / i
            for p in t:
                if p.getHeight() < moy - alpha or p.getHeight() > moy + alpha:
                    n += 1
        if j == 0:
            return n
        else:
            return n / j * 10

    def calcNbTargets(self):  # number of detected targets -> Ok
        # i = 0
        # for t in self.result.liste.values():
        #     i += 1
        # return i
        return self.good.__len__()

    def calcNbPoints(self):  # new definition -> number of points from good targets
      # number of detected pictures -> Ok
        i = 0
        for t in self.result.liste.values():
        	if id(t) in self.good:
        		for p in t:
        			i += 1
        if self.settings.getNbTargetsTheo() != 0:
            return i/self.settings.getNbTargetsTheo()  # bullshit
        else:
            return i

    def calcNbPertes(self):  # how many times a target has been lost during detection -> yep
        # mode opératoire: savoir quand sont les frames analysées, pour chaque target ranger ses points dans les intervalles .on part du premier, on va au dernier. à chaque fois qu'on passe de True à False, on incrémente, et on enlève une fois à la fin pour ne pas compter la disparition normal de la cible. Et paf, ça fait des chocapics.
        # temporary : detection of analyzed frames using timecodes -> stock them in a list and use it as a list of intervals /!\ stock timecodes // 10 to prevent slight differences!
        """inter = []
        for t in self.result.liste.values():
            for p in t:
                if float(p.getTime())//10 not in inter:
                    inter.append(float(p.getTime())//10)
        inter.sort()
        # end of temporary code -> we've got a list of all timecodes used by the program.
        pertes = 0
        temp = []
        for t in self.result.liste.values():
            i = 0
            for p in t:
                while float(p.getTime()) // 10 < inter[i]:
                    i += 1
                temp.append(i)
            temp.sort()
            i = 0
            while i < temp.__len__() - 1:
                pertes += temp[i + 1] - temp[i] - 1
                i += 1
        return pertes"""
        #return self.frames.__len__()
        classeur = []
        i = 0
        while i < self.calcNbPoints():
            classeur.append(False)
            i += 1
        i = 1  # parcours des intervalles
        count = 0  # nombre total de pertes enregistrées
        previous = False  # valeur precedente de classeur
        for t in self.result.liste.values():
            if id(t) in self.good:
                for c in classeur:
                    c = False
                i = 0
                for p in t:
                    while self.frames[i-1][2] >= p.getTime():
                        classeur[i] = True
                        i += 1
                for c in classeur:
                    if previous:
                        if c == False:
                            count += 1
                    previous = c
        return count

    def perfIndice(self):  # note sur 12 -> super sensible aux faux positifs!!
        result = self.imgs / 60
        result += self.tauxProfondeur / 100
        result += self.fiabiliteTaille / 50
        result += self.nbPoints / 25
        result += self.nbTargets / 25
        result -= self.nbPertes
        result -= self.falsep
        return result

    def recalc(self):
        self.imgs = self.calcImgs()
        self.tauxProfondeur = self.calcProfondeur()
        self.fiabiliteTaille = self.calcFiabTaille(0.5)
        self.nbTargets = self.calcNbTargets()
        self.nbPoints = self.calcNbPoints()
        self.nbPertes = self.calcNbPertes()
        self.perf = self.perfIndice()

    def printMe(self):
        print("*** analyse de", self.name, ":")
        print(" images par secondes :", self.imgs)
        print(" taux profondeur :", self.tauxProfondeur)
        print(" nombre de cibles :", self.nbTargets)
        print(" nombre de points :", self.nbPoints)
        print(" pertes de cible :", self.nbPertes)

    def addGoodTarget(self, line):
        self.good = line.split(" ")  # toutes les bonnes targets sont rangées dans ce tableau
        for t in self.good:
            t = float(t)

    def id(self, target):
        return target.getId()%10000

