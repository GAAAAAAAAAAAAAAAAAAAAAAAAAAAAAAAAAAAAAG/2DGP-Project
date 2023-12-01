from pico2d import *
import game_world
import random
import server

class Gate:
    image = None
    def __init__(self, x = None, y = None):
        if Gate.image == None:
            Gate.image = load_image('redGate135.png')

        self.x = x if x else random.randint(100, server.background.w - 100)
        self.y = y if y else random.randint(100, server.background.h - 100)

        #self.image = load_image('redGate135.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x - server.background.window_left, self.y - server.background.window_bottom)
        #self.image.clip_draw(0,0,135,45,200,370)
        draw_rectangle(*self.get_bb())  # 튜플을 풀어헤쳐서 인자로 전달.

    def get_bb(self):
        return self.x - 70, self.y - 25, self.x + 70, self.y + 25

    def handle_collision(self, group, other):
        match group:
            case 'player:gate':
                # fill here
                game_world.remove_object(self)