def pointinpolygon(pol, x, y, n):
    Xdata = []
    Ydata = []
    corn = pol.getCorners(n)
    l = corn - 1
    temp = pol.polys[n]
    for t in range(0, corn):
        Xdata.append(pol.Xdata[temp[t]])
    for t in range(0, corn):
        Ydata.append(pol.Ydata[temp[t]])
    Odd = -1
    for k in range(0, corn):
        if ((Ydata[k] < y and Ydata[l] >= y) or (Ydata[l] < y and Ydata[k] >= y)):
            det = (Ydata[l] - Ydata[k])
            if det == 0:
                det = 0.0000001 #0 division protection
            if Xdata[k] + (y - Ydata[k])/det * (Xdata[l] - Xdata[k]) < x:
                Odd = -Odd
        l = k
    return Odd