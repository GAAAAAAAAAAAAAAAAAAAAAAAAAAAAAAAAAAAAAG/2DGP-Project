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

class Star:
    image = None
    def __init__(self, x = None, y = None):
        if Star.image == None:
            Star.image = load_image('star.png')

        self.x = x if x else random.randint(50, 550)
        self.y = y


    def update(self):
        self.y += SKIING_SPEED_PPS * game_framework.frame_time * server.level
        if self.y > 800:
            game_world.remove_object(self)
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 100, 100, self.x, self.y, 20, 20)
        draw_rectangle(*self.get_bb())  # 튜플을 풀어헤쳐서 인자로 전달.

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        match group:
            case 'player:star':
                # fill here
                game_world.remove_object(self)
                server.boost_start = True
                pass