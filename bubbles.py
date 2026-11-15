
from OpenGL.GL import *
import math

bubbles = [
    [100, 100, 5],
    [250, 200, 8],
    [400, 80, 4],
    [550, 150, 6],
    [700, 250, 7],
    [850, 100, 5],
    [930, 300, 9]
]

def update_bubbles():
    for b in bubbles:
        b[1] += 2

        if b[1] > 720:
            b[1] = 0

def draw_bubbles(t):

    glColor3f(0.75, 0.95, 1.0)

    for b in bubbles:

        x, y, r = b

        glBegin(GL_LINE_LOOP)

        for i in range(31):
            a = 2 * math.pi * i / 30

            glVertex2f(
                x + r * math.cos(a),
                y + r * math.sin(a)
            )

        glEnd()
