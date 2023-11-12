from pico2d import *

class Gate:
    def __init__(self):
        self.image = load_image('redGate135.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0,0,135,45,200,370)

