import random

from pico2d import *
import game_world

import server

class Heart:
    def __init__(self, x):
        self.image = load_image('heart.png')
        self.x = x

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0,0,100,100, self.x, 770,50,50)