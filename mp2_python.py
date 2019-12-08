from math import sqrt
def circle(x1, y1, x2, y2, x3, y3):
    A = (x1*(y2-y3))-(y1*(x2-x3))+((x2*y3-x3*y2))
    B = int((pow(x1,2)+pow(y1,2))*(y3-y2)+(pow(x2,2)+pow(y2,2))*(y1-y3)+(pow(x3,2)+pow(y3,2))*(y2-y1))
    C = int((pow(x1,2)+pow(y1,2))*(x2-x3)+(pow(x2,2)+pow(y2,2))*(x3-x1)+(pow(x3,2)+pow(y3,2))*(x1-x2))
    D = int((pow(x1,2)+pow(y1,2))*(x3*y2-x2*y3)+(pow(x2,2)+pow(y2,2))*(x1*y3-x3*y1)+(pow(x3,2)+pow(y3,2))*(x2*y1-x1*y2))
    x = int(-B/(2*A))
    y = int(-C/(2*A))
    r = int(sqrt(((x-x1)**2)+((y-y1)**2)))
    D_vec = int(B/A)
    E_vec = int(C/A)
    F_vec = int(D/A)
    vector = [D_vec,E_vec,F_vec]
    print("Points of the Center of the Circle:",(x,y))
    print("The Radius of the Circle:", r)
    print("Vector[D,E,F]:", vector)