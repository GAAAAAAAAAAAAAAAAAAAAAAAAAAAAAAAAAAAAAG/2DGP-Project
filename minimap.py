from pico2d import *
from pico2d import load_font
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

class Minimap:
    def __init__(self):
        self.image = load_image('minimap.png')
        self.arrow_image = load_image('minimap_arrow.png')
        self.x = 45
        self.y = 640
        self.arrow_y = 685 + 50*(server.level-1)
        self.font = load_font('ENCR10B.TTF', 20)
        self.distance_count = 0
        self.rounded_distance_count = 0

    def update(self):
        if server.stop == False:
            self.arrow_y -= SKIING_SPEED_PPS * game_framework.frame_time * server.level * server.boost  * (0.01 + 0.0007 * server.level)
            self.distance_count += SKIING_SPEED_PPS * game_framework.frame_time * server.level * server.boost * 0.01195
            self.rounded_distance_count = round(self.distance_count, 2)
        pass

    def draw(self):
        if server.level == 1.0:
            self.image.clip_draw(0, 0, 50, 100, self.x, self.y, 50, 100)
        if server.level == 2.0:
            self.image.clip_draw(0, 0, 50, 100, self.x, self.y, 50, 200)
        if server.level == 3.0:
            self.image.clip_draw(0, 0, 50, 100, self.x, self.y, 50, 315)
        self.arrow_image.clip_draw(0, 0, 100, 100, self.x, self.arrow_y, 10, 10)

        self.font.draw(75, 770, f'distance : {self.rounded_distance_count}', (0, 0, 0))
        #draw_rectangle(*self.get_bb())  # 튜플을 풀어헤쳐서 인자로 전달.

    def get_bb(self):
        return self.x - 300, self.y - 50, self.x + 300, self.y

    def handle_collision(self, group, other):
        pass