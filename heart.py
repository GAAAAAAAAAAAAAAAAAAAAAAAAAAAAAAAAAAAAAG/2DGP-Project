from pico2d import *

class Heart:
    def __init__(self):
        self.image = load_image('heart.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 750)

