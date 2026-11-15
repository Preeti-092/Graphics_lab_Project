
from OpenGL.GL import *
from fish import circle
import math

def draw_turtle(x, y, t):

    glPushMatrix()
    glTranslatef(x, y, 0)

    # Shell
    circle(0, 0, 30, (0.25, 0.48, 0.20))

    # Shell pattern
    circle(0, 0, 23, (0.45, 0.60, 0.22))

    # Moving flippers
    movement = math.sin(t * 5) * 8

    glColor3f(0.35, 0.65, 0.32)

    for px, py in [(-23, 15), (23, 15),
                   (-23, -15), (23, -15)]:

        glBegin(GL_TRIANGLES)
        glVertex2f(px, py)
        glVertex2f(px + movement, py + 18)
        glVertex2f(px + 12, py - 8)
        glEnd()

    # Head
    circle(35, 5, 13, (0.35, 0.72, 0.35))

    # Eye
    circle(40, 9, 3, (0, 0, 0))

    glPopMatrix()
