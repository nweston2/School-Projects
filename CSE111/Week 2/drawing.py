"""
Author: Noah Weston
Date: 7 Nov 2022
Assignment: 03 Prove Milestone: Writing Functions
Purpose: Draw a picture using functions
"""
# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 2*scene_height / 3, scene_width, scene_height, width=0, fill="sky blue")
    draw_oval(canvas, x0=-20, x1=50, y0=450, y1=520, outline="", fill="yellow")
    draw_cloud(canvas, scene_width, scene_height)
    draw_cloud(canvas, scene_width, scene_height)


def draw_ground(canvas, scene_width, scene_height):
        draw_rectangle(canvas, 0, 0, scene_width, 2*scene_height / 3, width=0, fill="blue")
        draw_sub(canvas)
        draw_fish(canvas, scene_width, scene_height)

def draw_cloud(canvas, scene_width, scene_height):
    for i in range(25):
        min_diam = 50
        max_diam = 100
        x = random.randint(0, scene_width)
        y = random.randint(0, scene_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + (diameter/2), outline="white", fill="aliceBlue")

def draw_sub(canvas):
    draw_oval(canvas, x0=200, x1=450, y0=200, y1=250, outline="", fill="seashell4")
    draw_rectangle(canvas, x0=312, x1=350, y0=222, y1=265, outline="", fill="seashell4")
    draw_rectangle(canvas, x0=190, x1=212, y0=200, y1=250, outline="", fill="seashell4")
    draw_oval(canvas, x0=395, x1=420, y0=225, y1=235, outline="", fill="turquoise4")

def draw_fish(canvas, scene_width, scene_height):
    for i in range(25):
        min_diam = 10
        max_diam = 20
        water = ((2*scene_height)//3)-50
        x = random.randint(0, scene_width)
        y = random.randint(0, water)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + (diameter/2), outline="", fill="chocolate")
        draw_polygon(canvas, x0=x-1, y0=y, x1=x+2, y1=y+5, x2=x-5, y2=y+10, outline="", fill="chocolate")


# Call the main function so that
# this program will start executing.
main()