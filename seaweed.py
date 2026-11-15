
from OpenGL.GL import *
import math

def draw_seaweed(t):

    glLineWidth(5)
    glColor3f(0.10, 0.65, 0.25)

    for x in range(40, 1000, 100):

        glBegin(GL_LINE_STRIP)

        for j in range(11):

            y = j * 10
            wave = math.sin(t * 2 + j * 0.4 + x) * j * 1.5

            glVertex2f(x + wave, 60 + y)

        glEnd()

    glLineWidth(1)
