from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from constants import *

def draw_field():
    glColor4f(0, 0.3, 0.0, 1.0)
    glPushMatrix()
    glScalef(0.4, 0.2, 1)
    glutSolidCube(0.4)
    glPopMatrix()