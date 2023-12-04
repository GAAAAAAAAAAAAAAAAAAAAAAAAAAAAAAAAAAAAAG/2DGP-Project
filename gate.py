from pico2d import *
import game_world
import game_framework
import random
import server
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

class Gate:
    image = None
    bumpimage1 = None
    bumpimage2 = None
    def __init__(self, x = None, y = None):
        if Gate.image == None:
            Gate.image = load_image('redGate135.png')
        if Gate.bumpimage1 == None:
            Gate.bumpimage1 = load_image('redGate1.png')
        if Gate.bumpimage2 == None:
            Gate.bumpimage2 = load_image('redGate1.png')

        self.x = x if x else random.randint(50, 550)
        self.y = y

        self.x1 = self.x - 54
        self.x2 = self.x + 54

        self.c = False
        self.bump = False
        self.r = 0


    def update(self):
        if server.stop == False:
            self.y += SKIING_SPEED_PPS * game_framework.frame_time * server.level * server.boost
        if(self.bump == True):
            self.r += SKIING_SPEED_PPS * game_framework.frame_time * server.level * server.boost

        if self.y > 800:
            if self.c == False and server.boost != 1.5:
                server.player.hp -= 1
                for heart in play_mode.server.hearts:
                    game_world.remove_object(heart)
                    play_mode.server.hearts.remove(heart)
                    break
            self.bump = False
            game_world.remove_object(self)
        if (server.player.hp == 0):
            game_framework.change_mode(gameover_mode)
        pass

    def draw(self):
        if(self.bump == False):
            self.image.draw(self.x, self.y)
        if(self.bump == True):
            self.bumpimage1.clip_composite_draw(0, 0, 27, 45, self.r*0.1, 'h', self.x1-self.r*0.2, self.y, 50+self.r*0.15, 50+self.r*0.15)
            self.bumpimage2.clip_composite_draw(0, 0, 27, 45, -self.r*0.1, 'h', self.x2+self.r*0.2, self.y, 50+self.r*0.15, 50+self.r*0.15)
        #draw_rectangle(*self.get_bb())  # 튜플을 풀어헤쳐서 인자로 전달.

    def get_bb(self):
        return self.x - 45, self.y - 25, self.x + 45, self.y + 25

    def handle_collision(self, group, other):
        match group:
            case 'player:gate':
                # fill here
                #game_world.remove_object(self)
                self.c = True
                if(server.boost == 1.5):
                    self.bump = True
                server.player.point_count += 10
                pass