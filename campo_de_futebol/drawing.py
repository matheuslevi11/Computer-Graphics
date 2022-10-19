from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from constants import *
from math import sin, cos, tan, pi

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
    glutSolidCylinder(radius, height, SLICES, STACKS)
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
    glPointSize(5)
    glBegin(GL_LINE_LOOP)
    glVertex3f(-8.5, h, -4.5)
    glVertex3f(8.5, h, -4.5)
    glVertex3f(8.5, h, 4.5)
    glVertex3f(-8.5, h, 4.5)
    glEnd()
    glPointSize(10)
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
    glPointSize(10)
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
    """
    h = -3
    p = 10000 # Precisão ( quantidade de vértices )
	
    glBegin(GL_LINE_LOOP);
    for i in range(p+1):
        a = x + (radius * cos(i *  2*pi / p))
        b = y + (radius* sin(i * 2*pi / p))
        glVertex3f(a, h, b)
    glEnd()
    """

def draw_semicircle(x, y, radius, side):
    h = -3
    iterator = []
    n = 0
    while n <= pi:
        iterator.append(n)
        n += 0.001
    glBegin(GL_LINE_LOOP)
    for i in iterator:
        a = x + (radius * sin(i))
        b = y + (radius* cos(i))
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

def draw_scoreboard(p1, p2):
    width = 4
    depth = 2
    thickness = 1
    offset = 2 * thickness 

    glColor4f(0.35, 0.71, 0.94, 0)
    glPushMatrix()
    glTranslatef(0, +offset, 0)
    glRotatef(90, 1, 0, 0)
    glScalef(width, thickness , depth)
    glutWireCube(1)
    glPopMatrix()

    draw_bar(offset, 0)
    glPointSize(13)
    
    glColor4f(0.12, 0.9, 0.3, 0) # Cor do time esquerdo
    x = -1.8; y = 2.5
    for i in range(p1):
        glBegin(GL_POINTS)
        glVertex3f(x, y, 0)
        x += 0.3
        if x > 0:
            x = -1.8
            y -= 0.3
        glEnd()

    glColor4f(0.8, 0.2, 0.6, 0) # Cor do time direito
    x = 0.5; y = 2.5
    for i in range(p2):
        glBegin(GL_POINTS)
        glVertex3f(x, y, 0)
        x += 0.3
        if x > 1.8:
            x = 0.5
            y -= 0.3
        glEnd()
    
    glPointSize(10)

def draw_bar(offset, dx):
    glPushMatrix()
    glTranslatef(dx, +offset, 0)
    glRotatef(90, 1, 0, 0)
    glScalef(0.3, 1.3, 1.9)
    glutSolidCube(1)
    glPopMatrix()

def bresenham(p, q):
    x1, y1 = p
    x2, y2 = q
    dx = x2 - x1
    dy = y2 - y1
    delta_E = 2*dy
    delta_NE = 2 * (dy-dx)
    d = 2 * dy - dx
    glPointSize(5)
    glBegin(GL_POINTS)
    x, y = x1, y1
    if x == x2:
        simple_line_draw(x, y, y2)
    else:
        while x <= x2 or y <= y2:
            glVertex3f(x, -3, y)
            if d <= 0:
                d += delta_E
                x += 0.01
            else:
                d += delta_NE
                x += 0.01
                y += 0.01
            if x > x2 or y > y2:
                break
        glVertex3f(x, -3, y)
    glEnd()

def simple_line_draw(x, y, y2):
    while y < y2:
        glVertex3f(x, -3, y)
        y += 0.01

def bresenham_circle(r):
    x = 0
    y = r
    d = 3 - 2 * r
    circle_points(x, y)
    while (y >= x):
        if d <= 0:
            d = d + CIRCLE_D * x + CIRCLE_X
            x += 0.01
        else:
            d = d + CIRCLE_D * (x - y) + CIRCLE_X
            x += 0.01
            y -= 0.01
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