# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import *
import game_world
import game_framework

# state event check
# ( state event type, event value )


def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT



def time_out(e):
    return e[0] == 'TIME_OUT'

# time_out = lambda e : e[0] == 'TIME_OUT'




# Player Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Player Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8




class Idle:

    @staticmethod
    def enter(player, e):
        if player.face_dir == -1:
            player.action = 2
        elif player.face_dir == 1:
            player.action = 3
        player.dir = 0
        player.frame = 0
        player.wait_time = get_time() # pico2d import 필요
        pass

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1) % 8
        if get_time() - player.wait_time > 2:
            player.state_machine.handle_event(('TIME_OUT', 0))

    @staticmethod
    def draw(player):
        player.image.clip_draw(player.frame * 100, player.action * 100, 100, 100, player.x, player.y)



class Run:

    @staticmethod
    def enter(player, e):
        if right_down(e) or left_up(e): # 오른쪽으로 RUN
            player.dir, player.face_dir, player.action = 1, 1, 1
        elif left_down(e) or right_up(e): # 왼쪽으로 RUN
            player.dir, player.face_dir, player.action = -1, -1, 0

    @staticmethod
    def exit(player, e):
        if space_down(e):
            player.fire_ball()
        pass

    @staticmethod
    def do(player):
        # boy.frame = (boy.frame + 1) % 8
        player.x += player.dir * RUN_SPEED_PPS * game_framework.frame_time
        player.x = clamp(25, player.x, 1600 - 25)
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8


    @staticmethod
    def draw(player):
        player.image.clip_draw(player.frame * 100, player.action * 100, 100, 100, player.x, player.y)



class Sleep:

    @staticmethod
    def enter(player, e):
        player.frame = 0
        pass

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1) % 8

    @staticmethod
    def draw(player):
        if player.face_dir == -1:
            player.image.clip_composite_draw(player.frame * 100, 200, 100, 100,
                                          -3.141592 / 2, '', player.x + 25, player.y - 25, 100, 100)
        else:
            player.image.clip_composite_draw(player.frame * 100, 300, 100, 100,
                                          3.141592 / 2, '', player.x - 25, player.y - 25, 100, 100)


class StateMachine:
    def __init__(self, player):
        self.player = player
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, time_out: Sleep},
            Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle},
            Sleep: {right_down: Run, left_down: Run, right_up: Run, left_up: Run}
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
        self.action = 3
        self.dir = 0
        self.face_dir = 1
        self.image = load_image('animation_sheet.png')
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
        return self.x - 20, self.y - 50, self.x + 20, self.y + 50  # 튜플

    def handle_collision(self, group, other):
        if group == 'player:gate':     # 아... 볼과 충돌했구나...
            self.ball_count += 1