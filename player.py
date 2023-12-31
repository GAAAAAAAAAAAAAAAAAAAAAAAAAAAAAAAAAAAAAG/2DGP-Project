# 이것은 각 상태들을 객체로 구현한 것임.

#from pico2d import get_time, load_image, load_font, clamp, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE,draw_rectangle

from pico2d import *
from pico2d import load_font
import game_world
import game_framework
import play_mode
import server
import gameover_mode
import gameclear_mode
import random


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
#TIME_PER_ACTION = 0.5
TIME_PER_ACTION = 1.0
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
        if get_time() - player.wait_time >1.0 and get_time() - player.wait_time < 2.0:
            player.start = True
            events = get_events()
            if player.numkey == 1:
                for event in events:
                    if event.type == SDL_KEYDOWN and event.key == SDLK_1:
                        player.start = False
                        Player.boost_sound.play()
                        player.state_machine.cur_state.exit(player, None)
                        player.state_machine.cur_state = Boost_LeftSkiing
                        player.state_machine.cur_state.enter(player, None)
            if player.numkey == 2:
                for event in events:
                    if event.type == SDL_KEYDOWN and event.key == SDLK_2:
                        player.start = False
                        Player.boost_sound.play()
                        player.state_machine.cur_state.exit(player, None)
                        player.state_machine.cur_state = Boost_LeftSkiing
                        player.state_machine.cur_state.enter(player, None)
            if player.numkey == 3:
                for event in events:
                    if event.type == SDL_KEYDOWN and event.key == SDLK_3:
                        player.start = False
                        Player.boost_sound.play()
                        player.state_machine.cur_state.exit(player, None)
                        player.state_machine.cur_state = Boost_LeftSkiing
                        player.state_machine.cur_state.enter(player, None)
            if player.numkey == 4:
                for event in events:
                    if event.type == SDL_KEYDOWN and event.key == SDLK_4:
                        player.start = False
                        Player.boost_sound.play()
                        player.state_machine.cur_state.exit(player, None)
                        player.state_machine.cur_state = Boost_LeftSkiing
                        player.state_machine.cur_state.enter(player, None)
            if player.numkey == 5:
                for event in events:
                    if event.type == SDL_KEYDOWN and event.key == SDLK_5:
                        player.start = False
                        Player.boost_sound.play()
                        player.state_machine.cur_state.exit(player, None)
                        player.state_machine.cur_state = Boost_LeftSkiing
                        player.state_machine.cur_state.enter(player, None)
            if player.numkey == 6:
                for event in events:
                    if event.type == SDL_KEYDOWN and event.key == SDLK_6:
                        player.start = False
                        Player.boost_sound.play()
                        player.state_machine.cur_state.exit(player, None)
                        player.state_machine.cur_state = Boost_LeftSkiing
                        player.state_machine.cur_state.enter(player, None)
            if player.numkey == 7:
                for event in events:
                    if event.type == SDL_KEYDOWN and event.key == SDLK_7:
                        player.start = False
                        Player.boost_sound.play()
                        player.state_machine.cur_state.exit(player, None)
                        player.state_machine.cur_state = Boost_LeftSkiing
                        player.state_machine.cur_state.enter(player, None)
            if player.numkey == 8:
                for event in events:
                    if event.type == SDL_KEYDOWN and event.key == SDLK_8:
                        player.start = False
                        Player.boost_sound.play()
                        player.state_machine.cur_state.exit(player, None)
                        player.state_machine.cur_state = Boost_LeftSkiing
                        player.state_machine.cur_state.enter(player, None)
            if player.numkey == 9:
                for event in events:
                    if event.type == SDL_KEYDOWN and event.key == SDLK_9:
                        player.start = False
                        Player.boost_sound.play()
                        player.state_machine.cur_state.exit(player, None)
                        player.state_machine.cur_state = Boost_LeftSkiing
                        player.state_machine.cur_state.enter(player, None)
            if player.numkey == 0:
                for event in events:
                    if event.type == SDL_KEYDOWN and event.key == SDLK_0:
                        player.start = False
                        Player.boost_sound.play()
                        player.state_machine.cur_state.exit(player, None)
                        player.state_machine.cur_state = Boost_LeftSkiing
                        player.state_machine.cur_state.enter(player, None)

        if get_time() - player.wait_time > 2:
            player.start = False
            player.state_machine.handle_event(('TIME_OUT', 0))

    @staticmethod
    def draw(player):
        player.image.clip_composite_draw(int(player.frame)*100,0, 100, 103, 0,'h', player.x, player.y,75,75)

class End:
    @staticmethod
    def enter(player, e):
        player.image = load_image('finish_animation_sheet.png')
        player.wait_time = get_time()
        Player.applause_sound.play()
        pass

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        if(player.frame <16):
            player.frame +=  FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time
        if get_time() - player.wait_time > 4:
            player.state_machine.handle_event(('TIME_OUT', 0))
            server.stop = False
            game_framework.change_mode(gameclear_mode)
        pass

    @staticmethod
    def draw(player):
        player.image.clip_composite_draw(int(player.frame) * 57, 0, 57, 65, 0, 'h', player.x, player.y, 100, 100)
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
        if(server.boost_start):
            player.state_machine.cur_state.exit(player, None)
            player.state_machine.cur_state = Boost_LeftSkiing
            player.state_machine.cur_state.enter(player, None)
        if(server.stop):
            player.state_machine.cur_state.exit(player, None)
            player.state_machine.cur_state = End
            player.state_machine.cur_state.enter(player, None)
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time* server.level) % 7


    @staticmethod
    def draw(player):
        player.snowparticle.clip_composite_draw(int(player.frame) * 100, 0, 100, 103, 0, 'h', player.x, player.y, 75, 75)
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
        if (server.boost_start):
            player.state_machine.cur_state.exit(player, None)
            player.state_machine.cur_state = Boost_RightSkiing
            player.state_machine.cur_state.enter(player, None)
        if (server.stop):
            player.state_machine.cur_state.exit(player, None)
            player.state_machine.cur_state = End
            player.state_machine.cur_state.enter(player, None)

        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time * server.level) % 7
    @staticmethod
    def draw(player):
        player.snowparticle.clip_composite_draw(int(player.frame) * 100, 0, 100, 103, 0, 'h', player.x, player.y, 75, 75)
        player.image.clip_draw(int(player.frame)*100,0,100,103,player.x,player.y,75,75)


class Boost_LeftSkiing:
    @staticmethod
    def enter(player, e):
        player.dir = -1
        server.boost = 1.5
        if(server.boost_start):
            player.wait_time = get_time()
            server.boost_start = False
        pass

    @staticmethod
    def exit(player, e):
        #server.boost = 1
        #server.boost_start = False
        pass

    @staticmethod
    def do(player):
        player.x += player.dir * SKIING_SPEED_PPS * game_framework.frame_time* server.level
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time * server.level * server.boost) % 7
        if (player.x < 0):
            player.state_machine.cur_state.exit(player, None)
            player.state_machine.cur_state = Boost_RightSkiing
            player.state_machine.cur_state.enter(player, None)
        if (server.stop):
            player.state_machine.cur_state.exit(player, None)
            player.state_machine.cur_state = End
            player.state_machine.cur_state.enter(player, None)

        if get_time() - player.wait_time > 5:
            player.state_machine.handle_event(('TIME_OUT', 0))
            server.boost = 1
        pass

    @staticmethod
    def draw(player):
        player.fireparticle.clip_composite_draw(int(player.frame) * 100, 0, 100, 103, 0, 'h', player.x, player.y+15, 125, 125)
        player.image.clip_composite_draw(int(player.frame) * 100, 0, 100, 103, 0, 'h', player.x, player.y, 125, 125)
        pass

class Boost_RightSkiing:
    @staticmethod
    def enter(player, e):
        player.dir = 1
        server.boost = 1.5
        if (server.boost_start):
            player.wait_time = get_time()
            server.boost_start = False
        pass

    @staticmethod
    def exit(player, e):
        #server.boost = 1
        #server.boost_start = False
        pass

    @staticmethod
    def do(player):
        player.x += player.dir * SKIING_SPEED_PPS * game_framework.frame_time* server.level
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time * server.level * server.boost) % 7
        if (player.x > 600):
            player.state_machine.cur_state.exit(player, None)
            player.state_machine.cur_state = Boost_LeftSkiing
            player.state_machine.cur_state.enter(player, None)
        if (server.stop):
            player.state_machine.cur_state.exit(player, None)
            player.state_machine.cur_state = End
            player.state_machine.cur_state.enter(player, None)

        if get_time() - player.wait_time > 5:
            player.state_machine.handle_event(('TIME_OUT', 0))
            server.boost = 1
        pass

    @staticmethod
    def draw(player):
        player.fireparticle.clip_composite_draw(int(player.frame) * 100, 0, 100, 103, 0, 'h', player.x, player.y+15, 125, 125)
        player.image.clip_draw(int(player.frame) * 100, 0, 100, 103, player.x, player.y, 125, 125)



class StateMachine:
    def __init__(self, player):
        self.player = player
        self.cur_state = Start
        self.transitions = {
            Start: {time_out:LeftSkiing},
            LeftSkiing: {space_down:RightSkiing},
            RightSkiing: {space_down:LeftSkiing},
            #Boost: {time_out:LeftSkiing},
            Boost_LeftSkiing: {time_out:LeftSkiing, space_down:Boost_RightSkiing},
            Boost_RightSkiing: {time_out:RightSkiing, space_down:Boost_LeftSkiing},
            End:{time_out:Start}
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
    point_eat_sound = None
    star_eat_sound = None
    applause_sound = None
    boost_sound = None
    def __init__(self):
        self.x, self.y = 300, 700
        self.frame = 0
        self.action = 3 #0은 처음 시작상태, 1은 왼쪽 이동, 2는 오른쪽 이동, 3은 부스터
        self.dir = -1    #-1 : 왼쪽, 1 : 오른쪽
        self.image = load_image('playersheet.png')
        self.snowparticle = load_image('snowparticle.png')
        self.fireparticle = load_image('fireparticle.png')
        self.hp = 3
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.start_count = 3
        self.font = load_font('ENCR10B.TTF', 20)
        self.startfont = load_font('ENCR10B.TTF', 30)
        self.point_count = 0
        self.start = False
        self.numkey = random.randint(0,9)

        if not Player.point_eat_sound:
            Player.point_eat_sound = load_wav('pointsound.wav')
            Player.star_eat_sound = load_wav('starsound.wav')
            Player.applause_sound = load_wav('applause.wav')
            Player.boost_sound = load_wav('boostsound.wav')
            Player.point_eat_sound.set_volume(50)
            Player.star_eat_sound.set_volume(55)
            Player.applause_sound.set_volume(25)
            Player.boost_sound.set_volume(50)

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
        self.font.draw(100, 740, f'point : {self.point_count}', (0, 0, 0))
        if self.start == True:
            self.startfont.draw(100, 540, f'Press {self.numkey} key!!!', (0, 0, 0))
        #draw_rectangle(*self.get_bb())  # 튜플을 풀어헤쳐서 인자로 전달.


    def get_bb(self):
        return self.x - 35, self.y - 40, self.x + 35, self.y + 40  # 튜플

    def handle_collision(self, group, other):
        if group == 'player:point':
            self.point_count += 10
            Player.point_eat_sound.play()
        if group == 'player:star':
            Player.star_eat_sound.play()
            Player.boost_sound.play()
        if group == 'player:heartitem':
            Player.star_eat_sound.play()
        pass

