
from OpenGL.GL import *
import math

def circle(x, y, r, color):
    glColor3f(*color)

    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)

    for i in range(41):
        angle = 2 * math.pi * i / 40
        glVertex2f(
            x + r * math.cos(angle),
            y + r * math.sin(angle)
        )
    glEnd()


def draw_fish(x, y, scale, direction, t, color):

    glPushMatrix()

    glTranslatef(x, y, 0)
    glScalef(scale * direction, scale, 1)

    # Moving tail
    tail = math.sin(t * 7) * 10

    glColor3f(*color)

    glBegin(GL_TRIANGLES)
    glVertex2f(-25, 0)
    glVertex2f(-48, 18 + tail)
    glVertex2f(-48, -18 + tail)
    glEnd()

    # Fish body
    glBegin(GL_POLYGON)

    for i in range(41):
        a = 2 * math.pi * i / 40

        glVertex2f(
            28 * math.cos(a),
            18 * math.sin(a)
        )

    glEnd()

    # Top fin
    glColor3f(1.0, 0.8, 0.2)

    glBegin(GL_TRIANGLES)
    glVertex2f(-5, 12)
    glVertex2f(8, 30)
    glVertex2f(18, 12)
    glEnd()

    # Eye
    circle(16, 6, 4, (1, 1, 1))
    circle(17, 6, 2, (0, 0, 0))

    glPopMatrix()
