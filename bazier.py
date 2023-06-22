import matplotlib.pyplot as plt

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

def ncr(n, r):
    return fact(n) // (fact(r) * fact(n - r))

def power(a, b):
    res = 1.0
    while b > 0:
        res *= a
        b -= 1
    return res

def BEZ(k, n, u):
    return ncr(n, k) * power(u, k) * power((1 - u), (n - k))

def drawBezierCurve(x, y, n):
    # Draw a straight line connecting the control points
    plt.plot(x, y, 'ro-', label='Control Points')
    
    # Draw the Bezier curve
    for u in range(0, 101):
        u /= 100.0
        xPixel, yPixel = 0.0, 0.0
        for k in range(n + 1):
            xPixel += x[k] * BEZ(k, n, u)
            yPixel += y[k] * BEZ(k, n, u)
        plt.scatter(xPixel, yPixel, color='black')
    
    for k in range(n + 1):
        xy = f"({x[k]},{y[k]})"
        plt.text(x[k] + 10, y[k] + 10, xy)
        plt.scatter(x[k], y[k], color='yellow')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Bezier Curve')
    plt.legend()
    plt.grid(True)
    plt.show()

# Main function
if __name__ == '__main__':
    n = int(input("Enter the number of Control Points: "))
    x, y = [], []
    for i in range(n):
        point = input(f"Enter the {i+1} point (x,y): ")
        x_val, y_val = map(int, point.split())
        x.append(x_val)
        y.append(y_val)

    drawBezierCurve(x, y, n - 1)
