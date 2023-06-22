import matplotlib.pyplot as plt

def pixelPlot(xc, yc, x, y):
    plt.scatter(xc + x, yc + y, color='black')
    plt.scatter(xc - x, yc + y, color='green')
    plt.scatter(xc + x, yc - y, color='blue')
    plt.scatter(xc - x, yc - y, color='red')
    plt.scatter(xc + y, yc + x, color='yellow')
    plt.scatter(xc - y, yc + x, color='cyan')
    plt.scatter(xc + y, yc - x, color='orange')
    plt.scatter(xc - y, yc - x, color='magenta')

def connectPoints(xc, yc, x, y):
    plt.plot([xc - x, xc + x], [yc + y, yc + y], color='black')
    plt.plot([xc - x, xc + x], [yc - y, yc - y], color='black')
    plt.plot([xc - y, xc + y], [yc + x, yc + x], color='black')
    plt.plot([xc - y, xc + y], [yc - x, yc - x], color='black')

def midPointCircleDraw(xc, yc, r):
    p = 1 - r
    x = 0
    y = r
    pixelPlot(xc, yc, x, y)
    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * x + 1 - 2 * y
        pixelPlot(xc, yc, x, y)
        connectPoints(xc, yc, x, y)
        plt.pause(0.001)

# Main function
if __name__ == '__main__':
    x, y, r = map(int, input("Enter the coordinates and radius of your circle (x y r): ").split())
    plt.figure()
    midPointCircleDraw(x, y, r)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Mid-Point Circle Drawing Algorithm')
    plt.grid(True)
    plt.show()
