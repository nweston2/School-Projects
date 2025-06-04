#Alycia May Halliday Date:1/20/2023
import random
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

def main():
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call the draw_sky and draw_ground functions in this file.
    draw_sky(canvas, scene_width, scene_height)

    for i in range(0,30):
        x = random.randint(1, 800)
        y = random.randint(1, 500)
        draw_cloud(canvas, scene_height, scene_width, x, y)

    draw_ground(canvas, scene_width, scene_height)
    draw_bird(canvas, scene_height, scene_width, 230, 230)
    draw_bird(canvas, scene_height, scene_width, 250, 250)
    draw_bird(canvas, scene_height, scene_width, 270, 200)
    draw_bird(canvas, scene_height, scene_width, 200, 280)
    
    #draw_clouds(canvas, scene_width, scene_height)

    # Call the finish_drawing function
    # in the draw2d.py libra-ry.
    finish_drawing(canvas)

def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width = 0, fill="darkOrange")
    draw_sun(canvas, scene_width, scene_height / 2)

def draw_sun(canvas, scene_width, scene_height):
    """sun"""
    draw_oval(canvas, scene_width * 0.35, scene_height / 2, scene_width * 0.55, scene_height, outline = "gold1", width = 5, fill = "gold2")

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_mountain(canvas, scene_width, scene_height)
    draw_rectangle(canvas, 0, 0,
        #scene_width, scene_height / 3, width = 0, fill="tan4")
        scene_width, scene_height / 3, width = 0, fill="grey15")

def draw_mountain(canvas, scene_width, scene_height):
    draw_polygon(canvas, x0 = 0, y0 = 0, x1 = 0, y1 = scene_height * 0.65,
    x2 = scene_width * 0.35, y2 = scene_height * 0.15, outline = "grey14", width = 0, fill = "grey14")   
    
    draw_polygon(canvas, x0 = 0, y0 = scene_height * 0.15, x1 = scene_width * 0.15, y1 = scene_height * 0.55,
    x2 = scene_width * 0.5, y2 = scene_height * 0.15, outline = "grey14", width = 0, fill = "grey14")
    
    draw_polygon(canvas, x0 = scene_width * 0.22, y0 = scene_height * 0.2, x1 = scene_width * 0.32, y1 = scene_height * 0.45,
    x2 = scene_width * 0.5, y2 = scene_height * 0.22, outline = "grey14", width = 0, fill = "grey14")

    draw_polygon(canvas, x0 = scene_width * 0.4, y0 = scene_height * 0.2, x1 = scene_width * 0.65, y1 = scene_height * 0.7,
    x2 = scene_width * 0.85, y2 = scene_height * 0.2, outline = "grey14", width = 0, fill = "grey14")

    draw_polygon(canvas, x0 = scene_width * 0.65, y0 = scene_height * 0.2, x1 = scene_width * 0.8, y1 = scene_height * 0.5,
    x2 = scene_width, y2 = scene_height * 0.2, outline = "grey14", width = 0, fill = "grey14")

    draw_polygon(canvas, x0 = scene_width * 0.75, y0 = scene_height * 0.2, x1 = scene_width * 0.95, y1 = scene_height * 0.6,
    x2 = scene_width, y2 = scene_height * 0.4, outline = "grey14", width = 0, fill = "grey14")

    draw_rectangle(canvas, x0 = scene_width, y0 = scene_height * 0.4, 
    x1 = scene_width * 0.7, y1 = scene_height * 0.2, outline = "grey14", width = 0, fill = "grey14")

def draw_bird(canvas, scene_height, scene_width, x, y):
    draw_polygon(canvas, x0 = 0 + x, y0 = scene_height * 0.02 + y, x1 = scene_width * 0.05 + x, y1 = scene_height * 0.01 + y, 
    x2 = scene_width * 0.05 + x, y2 = 0 + y, width = 0, fill = "black")
    draw_polygon(canvas, x0 = scene_width * 0.1 + x, y0 = scene_height * 0.02 + y, x1 = scene_width * 0.05 + x, y1 = scene_height * 0.01 + y, 
    x2 = scene_width * 0.05 + x, y2 = 0 + y, width = 0, fill = "black")

def draw_cloud(canvas, scene_height, scene_width, x, y):
    draw_oval(canvas, x0 = 0 + x, y0 = scene_height * 0.015 + y, x1 = scene_width * 0.05 + x, y1 = scene_height * 0.045 + y,
    width = 0, outline = "lightPink1", fill = "lightPink1")
    draw_oval(canvas, x0 = scene_width * 0.02 + x, y0 = scene_height * 0 + y, x1 = scene_width * 0.06 + x, y1 = scene_height * 0.07 + y,
    width = 0, outline = "lightPink1", fill = "lightPink1")
    draw_oval(canvas, x0 = scene_width * 0.04 + x, y0 = scene_height * 0 + y, x1 = scene_width * 0.08 + x, y1 = scene_height * 0.08 + y,
    width = 0, outline = "lightPink1", fill = "lightPink1")
    draw_oval(canvas, x0 = scene_width * 0.07 + x, y0 = scene_height * 0.015  + y, x1 = scene_width * 0.09 + x, y1 = scene_height * 0.045 + y,
    width = 0, outline = "lightPink1", fill = "lightPink1")

#     Draw a pine tree.
#     tree_center_x = 170
#     tree_bottom = 100
#     tree_height = 200
#     draw_pine_tree(canvas, tree_center_x,
#             tree_bottom, tree_height)

#     # Draw another pine tree.
#     tree_center_x = 90
#     tree_bottom = 70
#     tree_height = 220
#     draw_pine_tree(canvas, tree_center_x,
#             tree_bottom, tree_height)


# def draw_pine_tree(canvas, center_x, bottom, height):
#     """Draw a single pine tree.
#     Parameters
#         canvas: The canvas where this function
#             will draw a pine tree.
#         center_x, bottom: The x and y location in pixels where
#             this function will draw the bottom of a pine tree.
#         height: The height in pixels of the pine tree that
#             this function will draw.
#     Return: nothing
#     """
#     trunk_width = height / 10
#     trunk_height = height / 8
#     trunk_left = center_x - trunk_width / 2
#     trunk_right = center_x + trunk_width / 2
#     trunk_top = bottom + trunk_height

#     # Draw the trunk of the pine tree.
#     draw_rectangle(canvas,
#             trunk_left, trunk_top, trunk_right, bottom,
#             outline="gray20", width=1, fill="tan3")

#     skirt_width = height / 2
#     skirt_height = height - trunk_height
#     skirt_left = center_x - skirt_width / 2
#     skirt_right = center_x + skirt_width / 2
#     skirt_top = bottom + height

#     # Draw the crown (also called skirt) of the pine tree.
#     draw_polygon(canvas, center_x, skirt_top,
#             skirt_right, trunk_top,
#             skirt_left, trunk_top,
#             outline="gray20", width=1, fill="dark green")


# Call the main function so that
# this program will start executing.
main()