# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import *
import game_world
import game_framework

# state event check
# ( state event type, event value )


def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


def time_out(e):
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
FRAMES_PER_ACTION = 8




class Start:
    @staticmethod
    def enter(player, e):
        player.action = 0
        player.dir = 0
        player.frame = 0
        player.wait_time = get_time() # pico2d import 필요
        pass

    @staticmethod
    def exit(player, e):
        player.dir = -1
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        if get_time() - player.wait_time > 2:
            player.state_machine.handle_event(('TIME_OUT', 0))

    @staticmethod
    def draw(player):
        player.image.clip_draw(0,0, 100, 100, player.x, player.y)

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
        if space_down(e):
            player.dir = -1

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        # boy.frame = (boy.frame + 1) % 8
        player.x += player.dir * SKIING_SPEED_PPS * game_framework.frame_time
        if(player.x < 0) :
            player.dir = 1
        if(player.x > 600):
            player.dir = -1
        #player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8


    @staticmethod
    def draw(player):
        player.image.clip_draw(0,0, 100, 100, player.x, player.y)

class RightSkiing:
    @staticmethod
    def enter(player, e):
        if space_down(e):
            player.dir = 1

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        # boy.frame = (boy.frame + 1) % 8
        player.x += player.dir * SKIING_SPEED_PPS * game_framework.frame_time
        #player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        if (player.x < 0):
            player.dir = 1
        if (player.x > 600):
            player.dir = -1

    @staticmethod
    def draw(player):
        #player.image.clip_draw(player.frame * 100, player.action * 100, 100, 100, player.x, player.y)
        player.image.clip_draw(0,0,100,100,player.x,player.y)


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
        self.x, self.y = 300, 600
        self.frame = 0
        self.action = 3 #0은 처음 시작상태, 1은 왼쪽 이동, 2는 오른쪽 이동, 3은 부스터
        self.dir = 0    #-1 : 왼쪽, 1 : 오른쪽
        self.image = load_image('test.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
        draw_rectangle(*self.get_bb())  # 튜플을 풀어헤쳐서 인자로 전달.


    def get_bb(self):
        return self.x - 25, self.y - 50, self.x + 25, self.y + 40  # 튜플

    def handle_collision(self, group, other):
        pass
        #if group == 'player:gate':     # 아... 볼과 충돌했구나...
