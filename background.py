from pico2d import *
import server
import random
import game_framework


# class Background:
#     def __init__(self):
#         self.image = load_image('Scrallbackground.png')
#         self.cw = get_canvas_width()
#         self.ch = get_canvas_height()
#         self.w = self.image.w
#         self.h = self.image.h
#
#     def draw(self):
#         #self.image.draw(300, 400)
#         # 시도
#         self.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.cw, self.ch, 0, 0)
#         #player.image.clip_draw(int(player.frame) * 100, 0, 100, 103, player.x, player.y, 75, 75)
#
#     def update(self):
#         #시도
#         # self.window_left = clamp(0, int(server.player.x) - self.cw // 2, self.w - self.cw - 1)
#         # self.window_bottom = clamp(0, int(server.player.y) - self.ch // 2, self.h - self.ch - 1)
#         self.window_left = clamp(0, int(server.player.x) - self.cw // 2, self.w - self.cw - 1)
#         self.window_bottom = clamp(0, int(server.player.y) - self.ch // 2, self.h - self.ch - 1)
#         pass

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
SKIING_SPEED_KMPH = 20.0 # Km / Hour
SKIING_SPEED_MPM = (SKIING_SPEED_KMPH * 1000.0 / 60.0)
SKIING_SPEED_MPS = (SKIING_SPEED_MPM / 60.0)
SKIING_SPEED_PPS = (SKIING_SPEED_MPS * PIXEL_PER_METER)

# Player Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 7

class Background:
    def __init__(self):
        self.image = load_image('ScrallbackgroundLong.png')
        self.y = -800
        self.bgm = load_music('bgm.mp3')
        self.bgm.set_volume(27)
        self.bgm.repeat_play()

    def draw(self):
        self.image.clip_draw(0, 10000 + int(self.y), 600, 800, 300, 400)
        #self.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.cw, self.ch, 0, 0)
        #player.image.clip_draw(int(player.frame) * 100, 0, 100, 103, player.x, player.y, 75, 75)

    def update(self):
        if server.stop == False:
            self.y -= SKIING_SPEED_PPS * game_framework.frame_time * server.level * server.boost
        if(self.y<-9200):
            self.y = -800
        pass



cx = 900 % 800
cy = 700 // 600


class InfiniteBackground:

    def __init__(self):
        self.image = load_image('Scrallbackground.png')
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h



    def draw(self):
        self.image.clip_draw_to_origin(self.q3l, self.q3b, self.q3w, self.q3h, 0, 0)                        # quadrant 3
        self.image.clip_draw_to_origin(self.q2l, self.q2b, self.q2w, self.q2h, 0, self.q3h)                 # quadrant 2
        self.image.clip_draw_to_origin(self.q4l, self.q4b, self.q4w, self.q4h, self.q3w, 0)                 # quadrant 4
        self.image.clip_draw_to_origin(self.q1l, self.q1b, self.q1w, self.q1h, self.q3w, self.q3h)          # quadrant 1

    def update(self):

        # quadrant 3
        self.q3l = (int(server.player.x) - self.cw // 2) % self.w
        self.q3b = (int(server.player.y) - self.ch // 2) % self.h
        self.q3w = clamp(0, self.w - self.q3l, self.w)
        self.q3h = clamp(0, self.h - self.q3b, self.h)

        # quadrant 2
        self.q2l = self.q3l
        self.q2b = 0
        self.q2w = self.q3w
        self.q2h = self.ch - self.q3h

        # quadrand 4
        self.q4l = 0
        self.q4b = self.q3b
        self.q4w = self.cw - self.q3w
        self.q4h = self.q3h

        # quadrand 1
        self.q1l = 0
        self.q1b = 0
        self.q1w = self.q4w
        self.q1h = self.q2h


    def handle_event(self, event):
        pass