from OpenGL.GL import *
import pygame as pg

class Vector():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def get(self):
        return [self.x, self.y, self.z]

class Vision():
    def __init__(self, eye, center, up):
        self.eye = eye
        self.center = center
        self.up = up

    def get(self):
        return self.eye, self.center, self.up

    def get_all(self):
        return [*self.eye.get(), *self.center.get(), *self.up.get()]

class Number():
    def __init__(self, array, side):
        self.array = array
        self.index = 0
        self.side = side
        self.color = int(self.array[self.index])
    
    def next(self):
        self.index += 1
        if self.index > 6:
            return
        self.color = int(self.array[self.index])

    def get_color(self):
        if self.side == 'left':
            return [0.12, 0.9, 0.3]
        else:
            return [0.8, 0.2, 0.6]

class Material:
    def __init__(self, filepath):
        self.texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        image = pg.image.load(filepath).convert_alpha()
        image_width,image_height = image.get_rect().size
        img_data = pg.image.tostring(image,'RGBA')
        glTexImage2D(GL_TEXTURE_2D,0,GL_RGBA,image_width,image_height,0,GL_RGBA,GL_UNSIGNED_BYTE,img_data)
        glGenerateMipmap(GL_TEXTURE_2D)

    def activate(self):
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.texture)
    
    def deactivate(self):
        glBindTexture(GL_TEXTURE_2D, 0)

    def destroy(self):
        glDeleteTextures(1, (self.texture,))