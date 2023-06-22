import math
import matplotlib.pyplot as plt

point = 0
x = []
y = []
angle = 0.0
xPivot = 0.0
yPivot = 0.0

def draw():
    for i in range(point):
        plt.plot([x[i], x[(i + 1) % point]], [y[i], y[(i + 1) % point]], 'r-')
        print(x[i], y[i])

def rotation():
    for i in range(point):
        xShift = x[i] - xPivot
        yShift = y[i] - yPivot
        x[i] = xPivot + (xShift * math.cos(angle)) - (yShift * math.sin(angle))
        y[i] = yPivot + (xShift * math.sin(angle)) + (yShift * math.cos(angle))

def run_program():
    global point, x, y, angle, xPivot, yPivot

    point = int(input("Enter no. of sides in polygon: "))
    print("Enter each vertex coordinates:")

    for i in range(point):
        vertex = input().split()
        x.append(float(vertex[0]))
        y.append(float(vertex[1]))

    angle = float(input("Enter rotation angle: "))
    xPivot, yPivot = map(float, input("Enter pivot points: ").split())
    plt.figure()
    draw()
    rotation()
    draw()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

run_program()
'''
Input Format:
Enter no. of sides in polygon: 4
Enter each vertex coordinates:
100 100
100 200
200 200
200 100
Enter rotation angle: 45
Enter pivot points: 200 200

'''