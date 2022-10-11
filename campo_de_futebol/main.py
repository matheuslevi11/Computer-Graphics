from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from constants import *
from drawing import *
from classes import *
import sys

vision = Vision(INITIAL_EYE, INITIAL_CENTER, INITIAL_UP)

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0) 
    update_camera()
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, WINDOW_WIDTH/WINDOW_HEIGHT, 0.1, 100.)
    glMatrixMode(GL_MODELVIEW)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_MODELVIEW)
    draw_field(width= 20, depth= 10, thickness=2)
    draw_goal()
    draw_lines()
    glutSwapBuffers()

def keyboard_handler(key, x, y):
    eye, center, up = vision.get()
    key = key.lower()

    if key == b'\x1b':
        sys.exit()

    if key == b"w":
        eye.z -= 1

    elif key == b"s":
        eye.z += 1

    elif key == b"d":
        eye.x += 1 

    elif key == b"a":
        eye.x -= 1

    elif key == b"q":
        eye.y += 1

    elif key == b"e":
        eye.y -= 1

    
    elif key == b"i": 
        center.z -= 1

    elif key == b"k": 
        center.z += 1

    elif key == b"l":
        center.x += 1

    elif key == b"j":
        center.x -= 1 

    elif key == b"u": 
        center.y += 1

    elif key == b"o":
        center.y -= 1

    elif key == b"f":
        if up.x != 0:
            up.x *= -1 
        else: 
            up.x = 1
        
        up.y = 0
        up.z = 0

    elif key == b"g":
        if up.y != 0: 
            up.y *= -1
        else: 
            up.y = 1
        
        up.x = 0
        up.z = 0

    elif key == b"h":
        if up.z != 0: # Se já estiver orientado no eixo z
            up.z *= -1   # Inverte a câmera
        else: 
            up.z = 1
        
        up.x = 0
        up.y = 0

    update_camera()

    glutPostRedisplay()

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
    #glutTimerFunc(DELAY, timer, 0)
    #glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard_handler)
    glutMainLoop()

def update_camera():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(*vision.get_all())

if __name__ == "__main__":
    main()