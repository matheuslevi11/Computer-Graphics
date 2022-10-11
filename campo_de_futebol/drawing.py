from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from constants import *
from math import sin, cos, pi

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
    glBegin(GL_LINES)
    glVertex3f(0, h, 4.5)
    glVertex3f(0, h, -4.5)
    glEnd()
    draw_circle(0, 0, 1.8)
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
    glBegin(GL_LINES)
    glVertex3f(-height, h, width)
    glVertex3f(-height, h, -width)
    glVertex3f(-height, h, width)
    glVertex3f(-8.5, h, width)
    glVertex3f(-height, h, -width)
    glVertex3f(-8.5, h, -width)
    glEnd()
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
	
    glBegin(GL_LINE_LOOP);
    for i in range(p+1):
        a = x + (radius * cos(i *  2*pi / p))
        b = y + (radius* sin(i * 2*pi / p))
        if a > x:
            glVertex3f(a*side, h, b*side)
    glEnd()