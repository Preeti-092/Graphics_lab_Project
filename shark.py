
from OpenGL.GL import *
from fish import circle
import math

def draw_shark(x, y, t):

    glPushMatrix()
    glTranslatef(x, y, 0)

    tail = math.sin(t * 5) * 12

    # Tail
    glColor3f(0.35, 0.40, 0.48)

    glBegin(GL_TRIANGLES)
    glVertex2f(-65, 0)
    glVertex2f(-100, 25 + tail)
    glVertex2f(-100, -25 + tail)
    glEnd()

    # Body
    glColor3f(0.48, 0.55, 0.62)

    glBegin(GL_POLYGON)

    for i in range(41):
        a = 2 * math.pi * i / 40

        glVertex2f(
            65 * math.cos(a),
            27 * math.sin(a)
        )

    glEnd()

    # Dorsal fin
    glColor3f(0.35, 0.40, 0.48)

    glBegin(GL_TRIANGLES)
    glVertex2f(-10, 20)
    glVertex2f(12, 52)
    glVertex2f(30, 20)
    glEnd()

    # Eye
    circle(43, 8, 4, (0, 0, 0))

    glPopMatrix()
