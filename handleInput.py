from Polygons import Polygons
from Points import Points

def calculatePoints(d):
    x = (d[1] ** 2 - d[2] ** 2) / 4
    y = (d[3] ** 2 - d[2] ** 2) / 4
    id = d[0]
    return x,y,id

def loadData(filename):
    c=0
    Polygon1 = Polygons()
    Point1 = Points()
    f = open(filename, "r")
    linie = f.readlines()
    for i in range(0,len(linie)):
        a = linie[i].split()
        if linie[i].find("-")==0:
            c = c+1
            if c == 4:
                print("znaleziono wszystkie wartości, koniec importu")
                Point1.info()
                Polygon1.info()
        elif c == 1:
            if len(a)==3:
                for k in range(0,3):
                    a[k]=float(a[k])
                Polygon1.addPoint(a)
                #print(a,c)
        elif c == 2:
            if len(a)!=0:
                tab=[]
                for l in range(1,len(a)):
                    tab.append(a[l])
                Polygon1.addPolygon(a[0], tab)
        elif c==3:
            if len(a)==5:
                a[0]=int(a[0])
                for k in range(1,4):
                    a[k]=float(a[k])
                Point1.addPoint(calculatePoints(a))
    return Point1, Polygon1







