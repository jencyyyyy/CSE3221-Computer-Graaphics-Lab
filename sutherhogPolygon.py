import matplotlib.pyplot as plt

# Constants representing the region codes
INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8

def compute_outcode(x, y, xmin, xmax, ymin, ymax):
    code = INSIDE
    
    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP
    
    return code

def clip_polygon(polygon, xmin, xmax, ymin, ymax):
    clipped_polygon = []
    
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i+1) % len(polygon)]
        
        outcode1 = compute_outcode(x1, y1, xmin, xmax, ymin, ymax)
        outcode2 = compute_outcode(x2, y2, xmin, xmax, ymin, ymax)
        
        while True:
            if not (outcode1 | outcode2):  # Both points inside the window
                clipped_polygon.append((x1, y1))
                if outcode2 == INSIDE:
                    clipped_polygon.append((x2, y2))
                break
            
            if outcode1 & outcode2:  # Both points outside the same region
                break
            
            x, y = 0, 0
            outcode = outcode1 if outcode1 else outcode2
            
            if outcode & TOP:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif outcode & BOTTOM:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif outcode & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif outcode & LEFT:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin
            
            if outcode == outcode1:
                x1, y1 = x, y
                outcode1 = compute_outcode(x1, y1, xmin, xmax, ymin, ymax)
            else:
                x2, y2 = x, y
                outcode2 = compute_outcode(x2, y2, xmin, xmax, ymin, ymax)
    
    return clipped_polygon

def plot_polygon(polygon, clipped_polygon):
    # Extract x and y coordinates from the polygon vertices
    poly_x, poly_y = zip(*polygon)
    clipped_x, clipped_y = zip(*clipped_polygon)
    
    plt.figure()
    plt.plot(poly_x, poly_y, 'b-', label='Original Polygon')
    plt.plot(clipped_x, clipped_y, 'r-', label='Clipped Polygon')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Cohen-Sutherland Polygon Clipping')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # Example polygon vertices
    polygon = [(0, 0), (50, 100), (100, 50), (100, 0), (0, 50)]
    
    # Clipping window coordinates
    xmin, xmax, ymin, ymax = 25, 75, 25, 75
    
    # Perform polygon clipping
    clipped_polygon = clip_polygon(polygon, xmin, xmax, ymin, ymax)
    
    # Display the polygon
    plot_polygon(polygon, clipped_polygon)

# Run the main function
main()
