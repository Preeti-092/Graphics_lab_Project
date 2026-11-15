
import sys
from math import sin

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import background
import fish
import shark
import sea_turtle
import jellyfish
import bubbles
import seaweed
import coral
import random


WIDTH = 1000
HEIGHT = 700

t = 0.0
paused = False

# Small fish school settings
school1 = [
    (random.randint(0, 1000), random.randint(220, 320))
    for _ in range(8)
]

school2 = [
    (random.randint(0, 1000), random.randint(380, 460))
    for _ in range(8)
]


def draw_fish_school(school, t, color, speed, direction):
    for i, (start_x, start_y) in enumerate(school):

        # Group movement
        x = (start_x + direction * speed * t) % 1150

        # Natural swimming movement
        y = start_y + 12 * sin(t * 2.5 + i * 0.5)

        # Small individual movement
        x += 8 * sin(t * 2 + i)

        fish.draw_fish(
            x, y, 0.30, direction, t, color
        )


def init():
    glClearColor(0.01, 0.08, 0.20, 1.0)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glShadeModel(GL_SMOOTH)
    glDisable(GL_DEPTH_TEST)

    glEnable(GL_LINE_SMOOTH)
    glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)

    # 2D Projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WIDTH, 0, HEIGHT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def draw_underwater_haze():
    # Blue underwater fog overlay
    glDisable(GL_FOG)

    glColor4f(0.02, 0.16, 0.28, 0.10)

    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(WIDTH, 0)
    glVertex2f(WIDTH, HEIGHT)
    glVertex2f(0, HEIGHT)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # Background
    background.draw_background(t)

    # Seaweed
    seaweed.draw_seaweed(t)

    # Coral
    coral.draw_coral(150, 100)
    coral.draw_coral(450, 100)
    coral.draw_coral(800, 100)

    # Fish 1 - moving right
    x1 = (180 + 45 * t) % 1200 - 100
    y1 = 350 + 25 * sin(t * 2)

    fish.draw_fish(
        x1, y1, 1.0, 1, t,
        (1.0, 0.45, 0.15)
    )

    # Fish 2 - moving left
    x2 = 1100 - ((35 * t) % 1200)
    y2 = 470 + 20 * sin(t * 1.8)

    fish.draw_fish(
        x2, y2, 0.7, -1, t,
        (1.0, 0.85, 0.15)
    )

    # Fish 3 - moving right
    x3 = (760 + 30 * t) % 1200 - 100
    y3 = 300 + 30 * sin(t * 1.5)

    fish.draw_fish(
        x3, y3, 0.8, 1, t,
        (0.15, 0.85, 0.95)
    )

    # Shark - moving right
    shark_x = (650 + 25 * t) % 1200 - 100
    shark_y = 530 + 20 * sin(t * 1.2)

    shark.draw_shark(shark_x, shark_y, t)

    # Turtle
    turtle_y = 180 + 12 * sin(t * 1.5)
    sea_turtle.draw_turtle(300, turtle_y, t)

    # Jellyfish
    jellyfish.draw_jellyfish(850, 430, t)

    # Bubbles
    bubbles.draw_bubbles(t)

    # Underwater haze
    draw_underwater_haze()

    # Yellow fish school
    draw_fish_school(
        school1, t,
        (1.0, 0.8, 0.15),
        45, 1
    )

    # Cyan fish school
    draw_fish_school(
        school2, t,
        (0.15, 0.85, 1.0),
        55, -1
    )

    glutSwapBuffers()


def update(value):
    global t

    if not paused:
        t += 0.016
        bubbles.update_bubbles()

    glutPostRedisplay()
    glutTimerFunc(16, update, 0)


def keyboard(key, x, y):
    global paused, t

    if key == b'\x1b':
        sys.exit(0)

    elif key == b' ':
        paused = not paused

    elif key == b'r' or key == b'R':
        t = 0.0


def main():
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(100, 50)

    glutCreateWindow(b"Advanced Underwater World")

    init()

    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)

    glutTimerFunc(16, update, 0)

    glutMainLoop()


if __name__ == "__main__":
    main()
