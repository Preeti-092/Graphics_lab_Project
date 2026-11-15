
from OpenGL.GL import *
from math import sin, cos, pi


WIDTH = 1000
HEIGHT = 700

# 1. Draw Rectangle

def draw_quad(x1, y1, x2, y2, color):

    glColor4f(*color)

    glBegin(GL_QUADS)

    glVertex2f(x1, y1)
    glVertex2f(x2, y1)
    glVertex2f(x2, y2)
    glVertex2f(x1, y2)

    glEnd()



# 2. Draw Triangle

def draw_triangle(points, color):

    glColor4f(*color)

    glBegin(GL_TRIANGLES)

    for x, y in points:
        glVertex2f(x, y)

    glEnd()



# 3. Draw Ellipse

def draw_ellipse(x, y, rx, ry, color):

    glColor4f(*color)

    glBegin(GL_TRIANGLE_FAN)

    glVertex2f(x, y)

    for i in range(61):

        angle = 2 * pi * i / 60

        glVertex2f(
            x + rx * cos(angle),
            y + ry * sin(angle)
        )

    glEnd()



# 4. Ocean Gradient

def draw_ocean():

    glBegin(GL_QUADS)

    # Deep blue top
    glColor3f(0.01, 0.08, 0.25)
    glVertex2f(0, HEIGHT)
    glVertex2f(WIDTH, HEIGHT)

    # Turquoise bottom
    glColor3f(0.02, 0.42, 0.58)
    glVertex2f(WIDTH, 0)
    glVertex2f(0, 0)

    glEnd()



# 5. Sunlight Glow

def draw_sunlight(t):

    draw_ellipse(
        500, 695,
        330, 100,
        (0.40, 0.85, 1.0, 0.12)
    )

    # Animated sunlight rays
    for i in range(8):

        x = 100 + i * 115

        movement = sin(t * 0.7 + i) * 35

        draw_triangle(
            [
                (x, 700),
                (x + 28, 700),
                (x + 130 + movement, 170)
            ],
            (0.55, 0.90, 1.0, 0.045)
        )



# 6. Underwater Caustics

def draw_caustics(t):

    glLineWidth(2)

    for row in range(7):

        y = 145 + row * 65

        glColor4f(0.65, 0.95, 1.0, 0.17)

        glBegin(GL_LINE_STRIP)

        for i in range(51):

            x = i * 20

            wave = (
                sin(x * 0.018 + t * 1.4 + row)
                * 9
                +
                cos(x * 0.012 - t + row)
                * 5
            )

            glVertex2f(x, y + wave)

        glEnd()



# 7. Sandy Ocean Floor

def draw_seabed(t):

    # Main sand
    draw_quad(
        0, 0, WIDTH, 105,
        (0.72, 0.53, 0.32, 1.0)
    )

    # Wavy sand surface
    glBegin(GL_QUAD_STRIP)

    for x in range(0, WIDTH + 25, 25):

        wave = sin(x * 0.012 + t * 0.15) * 7

        glColor3f(0.91, 0.76, 0.51)
        glVertex2f(x, 88 + wave)

        glColor3f(0.68, 0.48, 0.29)
        glVertex2f(x, 0)

    glEnd()

    # Small sand details
    for i in range(40):

        x = (i * 83) % WIDTH
        y = 12 + (i * 17) % 65

        draw_ellipse(
            x, y,
            3, 1.5,
            (0.98, 0.84, 0.60, 0.8)
        )



# 8. Underwater Rocks

def draw_rocks():

    rocks = [
        (80, 75, 65, 30),
        (230, 65, 80, 27),
        (720, 70, 90, 35),
        (920, 75, 75, 32)
    ]

    for x, y, rx, ry in rocks:

        # Main rock
        draw_ellipse(
            x, y,
            rx, ry,
            (0.12, 0.23, 0.29, 1.0)
        )

        # Highlight
        draw_ellipse(
            x - 12, y + 8,
            rx * 0.50, ry * 0.40,
            (0.22, 0.36, 0.39, 1.0)
        )



# 9. Floating Particles

def draw_particles(t):

    glPointSize(3)

    glColor4f(0.80, 0.96, 1.0, 0.65)

    glBegin(GL_POINTS)

    for i in range(65):

        x = (
            i * 157 + sin(t + i) * 25
        ) % WIDTH

        y = (
            120 + (i * 73 + t * (8 + i % 5)) % 550
        )

        glVertex2f(x, y)

    glEnd()



# 10. Main Background Function

def draw_background(t):

    draw_ocean()

    draw_sunlight(t)

    draw_caustics(t)

    draw_seabed(t)

    draw_rocks()

    draw_particles(t)
