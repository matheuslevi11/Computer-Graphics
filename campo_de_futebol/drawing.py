from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from constants import *
from math import sin, cos, pi
from time import sleep
def draw_field(width, depth, thickness):
    offset = 2 * thickness 

    glColor4f(0, 0.3, 0.0, 1.0)
    glPushMatrix()
    glTranslatef(0, -offset, 0)
    glScalef(width, thickness , depth)
    glutSolidCube(1)
    glPopMatrix()

def draw_cilinder(radius, height, angle, z, x):
    glColor4f(0.9, 0.9, 0.9, 1.0)
    glPushMatrix()
    glTranslate(x, 0.8, z);
    glRotate(angle, 1.0, 0.0, 0.0);
    glutWireCylinder(radius, height, SLICES, STACKS)
    glPopMatrix()

def draw_goal():
    draw_cilinder(radius=0.1, height=3.75, angle=90,
    z=GOAL_SIZE, x=GOAL_DISTANCE)
    draw_cilinder(radius=0.1, height=3.75, angle=90,
    z=-GOAL_SIZE, x=GOAL_DISTANCE)
    draw_cilinder(radius=0.1, height=4, angle=0,
    z=-GOAL_SIZE, x=GOAL_DISTANCE)

    draw_cilinder(radius=0.1, height=3.75, angle=90,
    z=GOAL_SIZE, x=-GOAL_DISTANCE)
    draw_cilinder(radius=0.1, height=3.75, angle=90,
    z=-GOAL_SIZE, x=-GOAL_DISTANCE)
    draw_cilinder(radius=0.1, height=4, angle=0,
    z=-GOAL_SIZE, x=-GOAL_DISTANCE)

def draw_lines():
    h = -3
    glLineWidth(10)
    # Bordas
    glBegin(GL_LINE_LOOP)
    glVertex3f(-8.5, h, -4.5)
    glVertex3f(8.5, h, -4.5)
    glVertex3f(8.5, h, 4.5)
    glVertex3f(-8.5, h, 4.5)
    glEnd()
    # Centro
    """
    glBegin(GL_LINES)
    glVertex3f(0, h, 4.5)
    glVertex3f(0, h, -4.5)
    glEnd()
    """
    bresenham((0,-4.5), (0,4.5))
    bresenham_circle(1.8)
    #draw_circle(0, 0, 1.8)
    # Áreas
    draw_goal_areas(width=3, height=5)
    draw_goal_areas(width=1.5, height=7)
    draw_semicircle(-5, 0, 1, 1)
    draw_semicircle(-5, 0, 1, -1)
    # Pontos
    glPointSize(11)
    glBegin(GL_POINTS)
    glVertex3f(0, h, 0)
    glVertex3f(-6, h, 0)
    glVertex3f(6, h, 0)
    glEnd()

def draw_goal_areas(width, height):
    h = -3
    # Esquerda
    bresenham((-height, -width), (-height, width))
    bresenham((-8.5, width), (-height, width))
    bresenham((-8.5, -width), (-height, -width))
    """
    glBegin(GL_LINES)
    glVertex3f(-height, h, width)
    glVertex3f(-height, h, -width)
    glVertex3f(-height, h, width)
    glVertex3f(-8.5, h, width)
    glVertex3f(-height, h, -width)
    glVertex3f(-8.5, h, -width)
    glEnd()
    """
    # Direita
    glBegin(GL_LINES)
    glVertex3f(height, h, width)
    glVertex3f(height, h, -width)
    glVertex3f(height, h, width)
    glVertex3f(8.5, h, width)
    glVertex3f(height, h, -width)
    glVertex3f(8.5, h, -width)
    glEnd()

def draw_circle(x, y, radius):
    h = -3
    p = 10000 # Precisão ( quantidade de vértices )
	
    glBegin(GL_LINE_LOOP);
    for i in range(p+1):
        a = x + (radius * cos(i *  2*pi / p))
        b = y + (radius* sin(i * 2*pi / p))
        glVertex3f(a, h, b)
    glEnd()

def draw_semicircle(x, y, radius, side):
    h = -3
    p = 10000 # Precisão ( quantidade de vértices )
	
    glBegin(GL_LINE_LOOP)
    for i in range(p+1):
        a = x + (radius * cos(i *  2*pi / p))
        b = y + (radius* sin(i * 2*pi / p))
        if a > x:
            glVertex3f(a*side, h, b*side)
    glEnd()

def draw_ball(r, dx, dy, ex, ez):
    glLineWidth(1.2)
    glPushMatrix()    
    glTranslatef(dx, -3+r ,dy)
    glRotatef(dx*ez*1000 + dy*ex*1000, ex, 0, ez)
    # Criando a bola
    glColor4f(0.35, 0.71, 0.94, 0)
    glutSolidSphere(r, SLICES, STACKS)
    glColor4f(0, 0, 0, 0)
    glutWireSphere(r+0.001, 15, 15)

    
    glPopMatrix()

def bresenham(p, q):
    x1, y1 = p
    x2, y2 = q
    dx = x2 - x1
    dy = y2 - y1
    delta_E = 2*dy
    delta_NE = 2 * (dy-dx)
    d = 2 * dy - dx
    glPointSize(10)
    glBegin(GL_POINTS)
    x, y = x1, y1
    if x == x2:
        simple_line_draw(x, y, y2)
    else:
        while x <= x2 or y <= y2:
            glVertex3f(x, -3, y)
            if d <= 0:
                d += delta_E
                x += 0.1
            else:
                d += delta_NE
                x += 0.1
                y += 0.1
            if x > x2 or y > y2:
                break
        glVertex3f(x, -3, y)
    glEnd()

def simple_line_draw(x, y, y2):
    while y < y2:
        glVertex3f(x, -3, y)
        y += 0.1

def bresenham_circle(r):
    x = 0
    y = r
    d = 3 - 2 * r
    circle_points(x, y)
    while (y >= x):
        if d <= 0:
            d = d + 0.01 * x + 0.015
            x += 0.05
        else:
            d = d + 0.01 * (x - y) + 0.025
            x += 0.05
            y -= 0.05
        circle_points(x, y)


def circle_points(x, y):
    glBegin(GL_POINTS)
    glVertex3f(x,-3,y)
    glVertex3f(x, -3, -y)
    glVertex3f(-x, -3, y)
    glVertex3f(-x, -3, -y)
    glVertex3f(y, -3, x)
    glVertex3f(y, -3, -x)
    glVertex3f(-y, -3, x)
    glVertex3f(-y, -3, -x)
    glEnd()