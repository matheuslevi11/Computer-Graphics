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