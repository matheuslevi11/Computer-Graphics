from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from constants import *
from drawing import *
from classes import *
from lightning import *
import sys
import pygame as pg

vision = Vision(INITIAL_EYE, INITIAL_CENTER, INITIAL_UP)

def init():
    global GRASS, BLUE_GRANDSTAND, YELLOW_GRANDSTAND, BALL

    update_camera()
    setup_lights()
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, WINDOW_WIDTH/WINDOW_HEIGHT, 0.1, 100.)
    glMatrixMode(GL_MODELVIEW)
    glDepthMask(GL_TRUE)
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    GRASS = Material('images/grass.png')
    BLUE_GRANDSTAND = Material('images/arquibancada_azul.jpeg')
    YELLOW_GRANDSTAND = Material('images/arquibancada_amarela.jpeg')
    BALL = Material('images/ball.png')

def keyboard_handler(key):
    global BALL_DX, BALL_DY, BALL_EX, BALL_EZ, SCORE_LEFT, SCORE_RIGHT, NIGHT
    eye, center, up = vision.get()
    #key = key.lower()

    if key[pg.K_n]:
        NIGHT = not NIGHT

    if key[pg.K_w]:
        eye.z -= 1

    elif key[pg.K_a]:
        eye.x -= 1

    elif key[pg.K_s]:
        eye.z += 1

    elif key[pg.K_d]:
        eye.x += 1 

    elif key[pg.K_q]:
        eye.y += 1

    elif key[pg.K_e]:
        eye.y -= 1
    
    elif key[pg.K_i]: 
        center.z -= 1

    elif key[pg.K_k]: 
        center.z += 1

    elif key[pg.K_l]:
        center.x += 1

    elif key[pg.K_j]:
        center.x -= 1 

    elif key[pg.K_u]:
        center.y += 1

    elif key[pg.K_o]:
        center.y -= 1 

    elif key[pg.K_KP3]:
        BALL_DX += 0.2
        BALL_EX = 0; BALL_EZ = 1

        if BALL_DX >= 19.5 and (-2 <= BALL_DY <= 2):
            SCORE_RIGHT += 1
            BALL_DX = 0; BALL_DY = 0

    elif key[pg.K_KP1]:
        BALL_DX -= 0.2
        BALL_EX = 0; BALL_EZ = 1

        if BALL_DX <= -19.5 and (-2 <= BALL_DY <= 2):
            SCORE_LEFT += 1
            BALL_DX = 0; BALL_DY = 0

    elif key[pg.K_KP2]:
        BALL_DY += 0.2
        BALL_EX = 1; BALL_EZ = 0
    elif key[pg.K_KP5]:
        BALL_DY -= 0.2
        BALL_EX = 1; BALL_EZ = 0

    update_camera()

    pg.display.flip()

def main_loop():
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                
        keys = pg.key.get_pressed()
        keyboard_handler(keys)

        global BALL_DX, BALL_DY, BALL_EX, BALL_EZ, NIGHT
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        if NIGHT:
            glClearColor(0.0, 0.0, 0.0, 1.0)
        else:
            glClearColor(0.53, 0.81, 0.92, 1.0) 
    
        glMatrixMode(GL_MODELVIEW)
        display()
        pg.display.flip()

    pg.quit()

def display():
    global NIGHT, BLUE_GRANDSTAND, YELLOW_GRANDSTAND
    draw_field(width=40, depth=20, thickness=2, texture=GRASS)
    draw_benches(textures=[BLUE_GRANDSTAND, YELLOW_GRANDSTAND])
    draw_goals()
    draw_lines()
    draw_ball(0.5, BALL_DX, BALL_DY, BALL_EX, BALL_EZ, texture=BALL)
    draw_scoreboard(SCORE_LEFT, SCORE_RIGHT)
    if not NIGHT:
        draw_sun()
    draw_spotlights()

def main():
    pg.init()
    glutInit(sys.argv)
    pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pg.OPENGL|pg.DOUBLEBUF)
    pg.display.set_caption('Campo de Futebol OpenGL')
    icon = pg.image.load('images/icon.png')
    pg.display.set_icon(icon)
    init()
    main_loop()


def update_camera():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(*vision.get_all())

if __name__ == "__main__":
    main()