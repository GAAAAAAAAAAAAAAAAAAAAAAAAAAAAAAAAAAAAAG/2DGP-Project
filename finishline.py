from pico2d import *
import game_world
import game_framework
import random
import server
import play_mode

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
SKIING_SPEED_KMPH = 20.0 # Km / Hour
SKIING_SPEED_MPM = (SKIING_SPEED_KMPH * 1000.0 / 60.0)
SKIING_SPEED_MPS = (SKIING_SPEED_MPM / 60.0)
SKIING_SPEED_PPS = (SKIING_SPEED_MPS * PIXEL_PER_METER)

# Player Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 7

class Finishline:
    image = None
    def __init__(self):
        if Finishline.image == None:
            Finishline.image = load_image('finishline.png')

        self.x = 300
        self.y = -5300
        self.c = False


    def update(self):
        if self.c == False:
            self.y += SKIING_SPEED_PPS * game_framework.frame_time * server.level * server.boost
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 600, 100, self.x, self.y)
        draw_rectangle(*self.get_bb())  # 튜플을 풀어헤쳐서 인자로 전달.

    def get_bb(self):
        return self.x - 300, self.y - 50, self.x + 300, self.y

    def handle_collision(self, group, other):
        match group:
            case 'player:finishline':
                self.c = True
                server.stop = True
                pass