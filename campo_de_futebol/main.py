from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from constants import *
from drawing import *
import sys

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0) # set background color to black
    glEnable(GL_CULL_FACE)
    glViewport(0,0,WINDOW_WIDTH, WINDOW_HEIGHT)
    glLoadIdentity()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)

    draw_field()

    glutSwapBuffers()

def keyboard_handler(key, x, y):
    if key == b'\x1b':
        sys.exit()

def timer(v):
    #glPushMatrix()
    glRotatef(90, 1, 0, 0)
    #glPopMatrix()
    glutPostRedisplay()

    glutTimerFunc(DELAY, timer, v)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(300, 100)
    glutCreateWindow("Campo de Futebol")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(DELAY, timer, 0)
    #glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard_handler)
    glutMainLoop()

if __name__ == "__main__":
    main()