"""contains the initial parameters, from """


class Parameters:

    def __init__(self, dic):
        self.settings = {}
        i = 0
        for data in dic:
            if i == 1:
                for e in data.values():
                    for index, d in e.items():
                        self.settings[index] = d
            i += 1
        if self.settings.__len__() > 6:
            raise ValueError('trop de parametres dans le fichier caracteristiques_video.yml.\nIl doit y'
                             ' avoir:\n  -> nom\n  -> nonCam3\n  -> fps\n  -> serial\n  -> convergence\n  -> targets')

    def fill(self, dic):
        self.settings = dic

    def printMe(self):
        for i, d in self.settings.items():
            print(i, ": ", d)

    def addOut(self, outside):
        self.outside = outside

    def addDrone(self, drone):
        self.drone = drone

    def change(self, changed, value):
        # str = "changing", changed, "to", value
        print("changing", changed, "to", value, "...")
        if changed == "history":
            # i = 0
            #  for data in self.outside:
                # if i == 1:
                    # data["MOG2"]["history"] = value
                # i += 1
            self.write(open("outside.yml", encoding="cp1252", mode="r+"), "history", value)
        else:
            # i = 0
            # for data in self.drone:
                # if i == 1:
                #     data["MOG2"][changed] = value
                # i += 1
            self.write(open("drones.yml", "r+"), changed, value)
        print("done")

    def write(self, file, item, value):
        i = 0
        while file.read(1) != "":
            if file.read(item.__len__()) == item:
                i += item.__len__() + 3
                file.seek(i)
                file.write(str(value))
                file.write("    ")
                break
            i += 1
            file.seek(i)
