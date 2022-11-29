from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from constants import NIGHT

def setup_lights():
    ambient = [1.0, 1.0, 0.5]
    light_pos = [0.0, 20.0, 0.0]
    specular = [1.0, 1.0, 1.0]
    diffuse = [0.8, 0.8, 0.8]
    shininess = [70.0]
	
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, specular)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, shininess)

    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient)
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse)
    

    glLightfv(GL_LIGHT1, GL_DIFFUSE, ambient)
    glLightfv(GL_LIGHT1, GL_SPECULAR, ambient)
    glLightf(GL_LIGHT1, GL_SPOT_CUTOFF, 90)
    glLightfv(GL_LIGHT1, GL_POSITION, [21, 8, 10])
    glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION, [0.0, -1.0, 0.0])
    glLightf(GL_LIGHT1, GL_SPOT_EXPONENT, 2.0)
    
    if NIGHT:
        glEnable(GL_LIGHT1)
        glDisable(GL_LIGHT0)
    else:
        glEnable(GL_LIGHT0)
        glDisable(GL_LIGHT1)

    glEnable(GL_LIGHTING)