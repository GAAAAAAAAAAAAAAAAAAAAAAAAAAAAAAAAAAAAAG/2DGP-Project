from pico2d import *
import game_world
import game_framework
import random
import server

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
SKIING_SPEED_KMPH = 20.0 # Km / Hour
SKIING_SPEED_MPM = (SKIING_SPEED_KMPH * 1000.0 / 60.0)
SKIING_SPEED_MPS = (SKIING_SPEED_MPM / 60.0)
SKIING_SPEED_PPS = (SKIING_SPEED_MPS * PIXEL_PER_METER)

# Player Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 7

class Gate:
    image = None
    def __init__(self, x = None, y = None):
        if Gate.image == None:
            Gate.image = load_image('redGate135.png')

        self.x = x if x else random.randint(100, 500)
        self.y = y if y else random.randint(-10000, 100)

        #self.image = load_image('redGate135.png')

    def update(self):
        self.y += SKIING_SPEED_PPS * game_framework.frame_time * server.level
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        #self.image.clip_draw(0,0,135,45,200,370)
        draw_rectangle(*self.get_bb())  # 튜플을 풀어헤쳐서 인자로 전달.

    def get_bb(self):
        return self.x - 70, self.y - 25, self.x + 70, self.y + 25

    def handle_collision(self, group, other):
        match group:
            case 'player:gate':
                # fill here
                game_world.remove_object(self)