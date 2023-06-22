import matplotlib.pyplot as plt

numOfVertex = 0
x = []
y = []
xScale = 0
yScale = 0
xFixed = 0
yFixed = 0

def drawPolygon():
    for i in range(numOfVertex):
        plt.plot([x[i], x[(i+1) % numOfVertex]], [y[i], y[(i+1) % numOfVertex]], color='b')
        print(x[i], y[i])

def calculateFixedPoint():
    global xFixed, yFixed
    for i in range(numOfVertex):
        xFixed += x[i]
        yFixed += y[i]
    xFixed //= numOfVertex # floor division operator
    yFixed //= numOfVertex

def scaling():
    global x, y
    for i in range(numOfVertex):
        x[i] = (x[i] * xScale) + xFixed * (1 - xScale)
        y[i] = (y[i] * yScale) + yFixed * (1 - yScale)

numOfVertex = int(input("Enter number of vertices of your polygon: "))

print("Enter all vertices in clockwise direction:")
print("(x, y)")

for i in range(numOfVertex):
    vertex = input().split()
    x.append(int(vertex[0]))
    y.append(int(vertex[1]))

print("Enter Scaling Factor:")
print("XScale YScale")
scale = input().split()
xScale = int(scale[0])
yScale = int(scale[1])

plt.figure()
drawPolygon()
calculateFixedPoint()
scaling()
drawPolygon()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
