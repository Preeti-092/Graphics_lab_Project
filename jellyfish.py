
from OpenGL.GL import *
from fish import circle
import math

def draw_jellyfish(x, y, t):

    glPushMatrix()
    glTranslatef(x, y + math.sin(t * 2) * 12, 0)

    # Jellyfish head
    circle(0, 0, 24, (0.85, 0.35, 0.85))

    # Tentacles
    glColor3f(0.95, 0.65, 0.95)

    for i in range(4):
        px = -15 + i * 10
        wave = math.sin(t * 5 + i) * 7

        glBegin(GL_LINE_STRIP)
        glVertex2f(px, -12)
        glVertex2f(px + wave, -27)
        glVertex2f(px - wave, -42)
        glEnd()

    # Eyes
    circle(-8, 3, 3, (1, 1, 1))
    circle(8, 3, 3, (1, 1, 1))

    glPopMatrix()
