
class Points:
    def __init__(self):
        self.ID = []
        self.Xdata = []
        self.Ydata = []
    def getX(self, pos):
        return self.Xdata[pos]
    def getY(self, pos):
        return self.Ydata[pos]
    def getID(self,pos):
        return self.ID[pos]
    def addPoint(self,vector):
        self.ID.append(vector[2])
        self.Xdata.append(vector[0])
        self.Ydata.append(vector[1])
    def info(self):
        print("Znaleziono tyle Punktów:",len(self.ID))