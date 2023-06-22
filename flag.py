import matplotlib.pyplot as plotter
import matplotlib.patches as shapes

def draw_flag():
   
    fig, bg = plotter.subplots(figsize=(10, 6))

    bg_rect = shapes.Rectangle((3, 10), 10, 6, facecolor='#006a4e')
    bg.add_patch(bg_rect)

    red_circle = shapes.Circle((4.5+3, 13), radius=2, facecolor='#f42a41')
    bg.add_patch(red_circle)

    hnd_rect = shapes.Rectangle((2.75, 0), 0.25, 16.25, facecolor='#000000')
    bg.add_patch(hnd_rect)
    hnd_crcle = shapes.Circle((2.85, 16.25), radius=.25, facecolor='#000000')
    bg.add_patch(hnd_crcle)


    bg.set_xlim(0, 18)
    bg.set_ylim(0, 19)
    bg.set_aspect('equal')
    
    plotter.show()


draw_flag()