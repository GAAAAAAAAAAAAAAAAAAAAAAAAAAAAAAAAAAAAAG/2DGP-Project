# 이것은 각 상태들을 객체로 구현한 것임.

#from pico2d import get_time, load_image, load_font, clamp, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE,draw_rectangle

from pico2d import *

import game_world
import game_framework
import play_mode
import server
from heart import Heart
from gate import Gate
from star import Star
import gameover_mode


# state event check
# ( state event type, event value )


def space_down(e):
    if e == None:
        return None
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


def time_out(e):
    if e == None:
        return None
    return e[0] == 'TIME_OUT'

# time_out = lambda e : e[0] == 'TIME_OUT'




# Player Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
SKIING_SPEED_KMPH = 20.0  # Km / Hour
SKIING_SPEED_MPM = (SKIING_SPEED_KMPH * 1000.0 / 60.0)
SKIING_SPEED_MPS = (SKIING_SPEED_MPM / 60.0)
SKIING_SPEED_PPS = (SKIING_SPEED_MPS * PIXEL_PER_METER)

# Player Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 7


class Start:
    @staticmethod
    def enter(player, e):
        player.action = 0
        player.dir = -1
        player.frame = 0
        player.wait_time = get_time() # pico2d import 필요
        pass

    @staticmethod
    def exit(player, e):
        player.dir = -1
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time * server.level) % 7
        if get_time() - player.wait_time > 2:
            player.state_machine.handle_event(('TIME_OUT', 0))

    @staticmethod
    def draw(player):
        player.image.clip_composite_draw(int(player.frame)*100,0, 100, 103, 0,'h', player.x, player.y,75,75)

class End:

    @staticmethod
    def enter(player, e):
        pass

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
       pass
    @staticmethod
    def draw(player):
        pass


class LeftSkiing:
    @staticmethod
    def enter(player, e):
        # if space_down(e):
        #     player.dir = -1
        player.dir = -1

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        global hearts

        player.x += player.dir * SKIING_SPEED_PPS * game_framework.frame_time* server.level
        #player.y -= SKIING_SPEED_PPS * game_framework.frame_time
        if(player.x < 0) :
            player.hp -= 1
            for heart in play_mode.server.hearts:
                game_world.remove_object(heart)
                play_mode.server.hearts.remove(heart)
                break
            if(player.hp == 0):
                game_framework.change_mode(gameover_mode)
            player.state_machine.cur_state.exit(player, None)
            player.state_machine.cur_state = RightSkiing
            player.state_machine.cur_state.enter(player, None)
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time* server.level) % 7


    @staticmethod
    def draw(player):
        player.image.clip_composite_draw(int(player.frame)*100,0, 100, 103, 0,'h', player.x, player.y,75,75)

class RightSkiing:
    @staticmethod
    def enter(player, e):
        # if space_down(e):
        #     player.dir = 1
        player.dir = 1

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        #player.frame = (player.frame + 1) % 7
        player.x += player.dir * SKIING_SPEED_PPS * game_framework.frame_time* server.level
        #player.y -= SKIING_SPEED_PPS * game_framework.frame_time

        if (player.x > 600):
            player.hp -= 1
            for heart in play_mode.server.hearts:
                game_world.remove_object(heart)
                play_mode.server.hearts.remove(heart)
                break
            if (player.hp == 0):
                game_framework.change_mode(gameover_mode)
            player.state_machine.cur_state.exit(player, None)
            player.state_machine.cur_state = LeftSkiing
            player.state_machine.cur_state.enter(player, None)

        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time* server.level) % 7
    @staticmethod
    def draw(player):
        player.image.clip_draw(int(player.frame)*100,0,100,103,player.x,player.y,75,75)


class Boost:
    @staticmethod
    def enter(boy, e):
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        pass

    @staticmethod
    def draw(boy):
        pass



class StateMachine:
    def __init__(self, player):
        self.player = player
        self.cur_state = Start
        self.transitions = {
            Start: {time_out:LeftSkiing},
            LeftSkiing: {space_down:RightSkiing},
            RightSkiing: {space_down:LeftSkiing},
            Boost: {},
            End:{}
        }

    def start(self):
        self.cur_state.enter(self.player, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.player)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.player, e)
                self.cur_state = next_state
                self.cur_state.enter(self.player, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.player)



class Player:
    def __init__(self):
        self.x, self.y = 300, 700
        self.frame = 0
        self.action = 3 #0은 처음 시작상태, 1은 왼쪽 이동, 2는 오른쪽 이동, 3은 부스터
        self.dir = -1    #-1 : 왼쪽, 1 : 오른쪽
        self.image = load_image('playersheet.png')
        self.hp = 3
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.start_count = 3

    def update(self):
        self.state_machine.update()
        #시도
        # self.x = clamp(50.0, self.x, server.background.w - 50.0)
        # self.y = clamp(50.0, self.y, server.background.h - 50.0)

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()

        draw_rectangle(*self.get_bb())  # 튜플을 풀어헤쳐서 인자로 전달.

        #시도
        #sx, sy = get_canvas_width() // 2, get_canvas_height() // 2 + 300

        # sx = self.x - server.background.window_left
        # sy = self.y - server.background.window_bottom
        #
        # if self.dir == 1:
        #     self.image.clip_draw(int(self.frame) * 100, 0, 100, 103, sx, sy, 75, 75)
        # elif self.dir == -1:
        #     self.image.clip_composite_draw(int(self.frame) * 100, 0, 100, 103, 0, 'h', sx, sy, 75, 75)

    def get_bb(self):
        return self.x - 35, self.y - 40, self.x + 35, self.y + 40  # 튜플

    def handle_collision(self, group, other):
        pass
        #if group == 'player:gate':     # 아... 볼과 충돌했구나...
