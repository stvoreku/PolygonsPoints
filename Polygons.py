
class Polygons:
    def __init__(self):
        self.pointID = []
        self.Xdata = []
        self.Ydata = []
        self.polys = {}
    def getX(self, pos):
        return self.Xdata[pos]
    def getY(self, pos):
        return self.Ydata[pos]
    def getID(self,pos):
        return self.ID[pos]
    def addPoint(self,vector):
        print(len(self.pointID))
        self.pointID.append(vector[0])
        self.Xdata.append(vector[1])
        self.Ydata.append(vector[2])
        print("dodano", vector)
    def addPolygon(self,id,points):
        id=int(id)
        for i in range(0,len(points)):
            points[i]=int(points[i])
        self.polys[id]=points
    def info(self):
        print("Znaleziono tyle wielokatow:", len(self.polys.keys()), "i tyle punktów", len(self.pointID))
        print(self.polys[1])
    def getAmmount(self):
        return len(self.polys.keys())
    def getCorners(self,n):
        return len(self.polys[n])

    def getXYs(self,polygon):
        p = self.polys[polygon]
        temp = []
        for i in range(0,len(p)):
            temp.append([self.Xdata[p[i]], self.Ydata[p[i]]])
        return(temp)


