import matplotlib.pyplot as plt

numOfVertex = 0
x = []
y = []
xShift = 0
yShift = 0

def drawPolygon():
    for i in range(numOfVertex):
        plt.plot([x[i], x[(i+1) % numOfVertex]], [y[i], y[(i+1) % numOfVertex]], 'bo-')
        print(x[i],y[i])

def translation():
    for i in range(numOfVertex):
        x[i] += xShift
        y[i] += yShift

def run_program():
    global numOfVertex, x, y, xShift, yShift

    numOfVertex = int(input("Enter number of vertices of your polygon: "))

    print("Enter all vertices in anti-clockwise direction:")
    print("(x, y)")

    for i in range(numOfVertex):
        vertex = input().split()
        x.append(int(vertex[0]))
        y.append(int(vertex[1]))

    print("Enter translation factors:")
    print("XShift YShift")
    shift = input().split()
    xShift = int(shift[0])
    yShift = int(shift[1])

    plt.figure()
    drawPolygon()
    translation()
    drawPolygon()
    plt.xlim(min(x)-50, max(x)+10)
    plt.ylim(min(y)-50, max(y)+10)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

run_program()


"""
4
50 50
100 50
100 100
50 100

25 25
"""