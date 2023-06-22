import matplotlib.pyplot as plt

# Constants defining region codes
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

# Function to compute region code for a point (x, y)
def compute_region_code(x, y, xmin, ymin, xmax, ymax):
    code = INSIDE
    if x < xmin:
        code |= LEFT
    if x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    if y > ymax:
        code |= TOP
    return code

def cohenSutherland(winMin, winMax, point1, point2):
    code1 = compute_region_code(point1[0], point1[1], winMin[0], winMin[1], winMax[0], winMax[1])
    code2 = compute_region_code(point2[0], point2[1], winMin[0], winMin[1], winMax[0], winMax[1])

    done = False
    draw = False

    while not done:
        if code1 == 0 and code2 == 0:
            done = True
            draw = True
        elif code1 & code2 != 0:
            done = True
        else:
            if code1 != 0:
                m =  (point2[1] - point1[1]) / (point2[0] - point1[0])
                if code1 & LEFT:
                    point1[1] += (winMin[0] - point1[0]) *m
                    point1[0] = winMin[0]
                elif code1 & RIGHT:
                    point1[1] += (winMax[0] - point1[0]) * m
                    point1[0] = winMax[0]
                elif code1 & BOTTOM:
                    if point1[0] != point2[0]:
                        point1[0] += (winMin[1] - point1[1]) / m
                    point1[1] = winMin[1]
                elif code1 & TOP:
                    if point1[0] != point2[0]:
                        point1[0] += (winMax[1] - point1[1]) / m
                    point1[1] = winMax[1]

                code1 = compute_region_code(point1[0], point1[1], winMin[0], winMin[1], winMax[0], winMax[1])
            else:
                if code2 & LEFT:
                    point2[1] += (winMin[0] - point2[0]) * m
                    point2[0] = winMin[0]
                elif code2 & RIGHT:
                    point2[1] += (winMax[0] - point2[0]) *m
                    point2[0] = winMax[0]
                elif code2 & BOTTOM:
                    if point1[0] != point2[0]:
                        point2[0] += (winMin[1] - point2[1]) / m
                    point2[1] = winMin[1]
                elif code2 & TOP:
                    if point1[0] != point2[0]:
                        point2[0] += (winMax[1] - point2[1]) / m
                    point2[1] = winMax[1]

                code2 = compute_region_code(point2[0], point2[1], winMin[0], winMin[1], winMax[0], winMax[1])

    if draw:
        plt.plot([point1[0], point2[0]], [point1[1], point2[1]], color='blue')

def showWindow(xmin, ymin, xmax, ymax):
    plt.gca().set_xlim([xmin-50, xmax+50])
    plt.gca().set_ylim([ymin-50, ymax+50])
    plt.gca().add_patch(plt.Rectangle((xmin, ymin), xmax-xmin, ymax-ymin, fill=False))
    plt.text(xmin-20, ymin-20, f"({xmin},{ymin})")
    plt.text(xmax-20, ymin-20, f"({xmax},{ymin})")
    plt.text(xmin-20, ymax+20, f"({xmin},{ymax})")
    plt.text(xmax-20, ymax+20, f"({xmax},{ymax})")

def execute():
    xmin = 100
    ymin = 100
    xmax = 400
    ymax = 400

    showWindow(xmin, ymin, xmax, ymax)

    numOfLine = 1
    pointNumber = 1

    while numOfLine > 0:
        print(f"Enter point 1 for line {pointNumber}: ")
        x1 = int(input("x1: "))
        y1 = int(input("y1: "))
        print(f"Enter point 2 for line {pointNumber}: ")
        x2 = int(input("x2: "))
        y2 = int(input("y2: "))

        point1 = [x1, y1]
        point2 = [x2, y2]

        winMin = [xmin, ymin]
        winMax = [xmax, ymax]

        cohenSutherland(winMin, winMax, point1, point2)

        numOfLine -= 1
        pointNumber += 1

    plt.show()

execute()
