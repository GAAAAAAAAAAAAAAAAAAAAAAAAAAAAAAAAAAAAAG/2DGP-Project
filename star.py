from pico2d import *

class Star:
    def __init__(self):
        self.image = load_image('star.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0,0,100,100,500,170,50,50)

