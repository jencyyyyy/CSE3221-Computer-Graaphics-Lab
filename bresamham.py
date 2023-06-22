import matplotlib.pyplot as plt

def bresenham_line(xa, ya, xb, yb):
    dx = abs(xa - xb)
    dy = abs(ya - yb)
    p = 2 * dy - dx
    twoDy = 2 * dy
    twoDyDx = 2 * (dy - dx)

    x, y = xa, ya
    x_end = xb

    if xa > xb:
        x = xb
        y = yb
        x_end = xa

    plt.scatter(x, y, color='black')
    points = [[x, y]]  # Store the points for joining later
  
    while x < x_end:
        x += 1
        if p < 0:
            p += twoDy
        else:
            y += 1
            p += twoDyDx
        plt.scatter(x, y, color='black')
        points.append([x, y])

    # Join the points with a line
    x_coords, y_coords = zip(*points)
    plt.plot(x_coords, y_coords, color='blue')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title("Bresenham's Line")
    plt.grid(True)
    plt.show()
    print(points)

def main():
    xa, ya = map(int, input("Enter the starting point coordinates (x y): ").split())
    xb, yb = map(int, input("Enter the ending point coordinates (x y): ").split())

    bresenham_line(xa, ya, xb, yb)

main()
