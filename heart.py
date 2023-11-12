from pico2d import *

class Heart:
    def __init__(self):
        self.image = load_image('heart.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0,0,100,100,400,770,50,50)

