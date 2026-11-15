
from OpenGL.GL import *

def draw_coral(x, y):

    glLineWidth(8)

    glColor3f(1.0, 0.35, 0.35)

    branches = [
        (x, y, x - 20, y + 40),
        (x, y, x + 5, y + 65),
        (x, y, x + 30, y + 35),
        (x + 5, y + 65, x - 10, y + 85),
        (x + 5, y + 65, x + 25, y + 90)
    ]

    glBegin(GL_LINES)

    for x1, y1, x2, y2 in branches:
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)

    glEnd()

    glLineWidth(1)
