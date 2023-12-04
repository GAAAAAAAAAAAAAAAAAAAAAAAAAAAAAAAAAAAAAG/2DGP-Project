from pico2d import *
import game_world
import game_framework
import random
import server
import player
import play_mode
import gameover_mode

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
SKIING_SPEED_KMPH = 20.0 # Km / Hour
SKIING_SPEED_MPM = (SKIING_SPEED_KMPH * 1000.0 / 60.0)
SKIING_SPEED_MPS = (SKIING_SPEED_MPM / 60.0)
SKIING_SPEED_PPS = (SKIING_SPEED_MPS * PIXEL_PER_METER)

# Player Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 7

class Point:
    image = None
    def __init__(self, x = None, y = None):
        if Point.image == None:
            Point.image = load_image('point.png')

        self.x = x if x else random.randint(50, 550)
        self.y = y


    def update(self):
        if server.stop == False:
            self.y += SKIING_SPEED_PPS * game_framework.frame_time * server.level * server.boost
        if self.y > 800:
            game_world.remove_object(self)
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 100, 100, self.x, self.y, 30, 30)
        #draw_rectangle(*self.get_bb())  # 튜플을 풀어헤쳐서 인자로 전달.

    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15

    def handle_collision(self, group, other):
        match group:
            case 'player:point':
                # fill here
                game_world.remove_object(self)
                pass