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
        