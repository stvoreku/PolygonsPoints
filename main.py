from handleInput import loadData
from matplotlib.patches import Polygon, Circle
import matplotlib.pyplot as plt
import numpy as np
from RayAlg import pointinpolygon




Points, Polygons=loadData("testData.txt")
colors = ['green', 'red', 'cyan', 'magenta', 'yellow', 'k', 'w']

punktyID=[]

#Prezentacja metody
fig, ax = plt.subplots()
plt.plot([1,1,-1,-1],[-1,1,-1,1], 'ro')
ax.set_title("Wyznaczanie punktu na podstawie równań okręgow, Punkt przecięcia = szukany punkt")
plt.axis([-2, 2, -2, 2])
for p in [
    Circle((-1, 1), 0.38234762301,fill=False),
    Circle((1, 1), 1.69833432368,fill=False),
    Circle((-1, -1), 2.65260245592, fill=False),
]:
    ax.add_patch(p)
    x = (0.3823 ** 2 - 1.6983 ** 2) / 4
    y = (2.6526 ** 2 - 1.6983 ** 2) / 4
plt.plot(x,y,'og')
for j in range(0,Polygons.getAmmount()):
    fig, ax = plt.subplots()
    q = np.array(Polygons.getXYs(1))
    dobreX = []
    dobreY = []
    ndobreX = []
    ndobreY = []
    dobreID = []
    for i in range(0,len(Points.ID)):
        x=Points.Xdata[i]
        y=Points.Ydata[i]
        tag=Points.ID[i]
        if pointinpolygon(Polygons,x,y,j) == 1:
            dobreX.append(x)
            dobreY.append(y)
            dobreID.append(tag)
        else:
            ndobreX.append(x)
            ndobreY.append(y)
    plt.plot(dobreX,dobreY, 'ro')
    plt.plot(ndobreX,ndobreY, 'bo')
    q = np.array(Polygons.getXYs(j))
    polygon = Polygon(q, edgecolor=colors[j], fill=False, facecolor='none')
    ax.set_title(j)
    ax.add_patch(polygon)
    plt.axis([-2, 2, -2, 2])
    dobreID = list(set(dobreID))
    punktyID.append(dobreID)
    print("W wielokącie", j, "znajdują się następujące tagi:", dobreID)

print("Punkty znajdujące się w każdym:", list(set(punktyID[0]) & set(punktyID[1]) & set(punktyID[2]) & set(punktyID[3]) & set(punktyID[4])))
print("Punkty znajdujące się w jakimś:", list(set(punktyID[0]) | set(punktyID[1]) | set(punktyID[2]) | set(punktyID[3]) | set(punktyID[4])))
print("Punkty znajdujące się w żadnym:", set(Points.ID)-((set(punktyID[0]) | set(punktyID[1]) | set(punktyID[2]) | set(punktyID[3]) | set(punktyID[4]))))
plt.show()

