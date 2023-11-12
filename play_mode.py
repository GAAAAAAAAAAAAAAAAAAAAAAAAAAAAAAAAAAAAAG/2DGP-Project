import random

from pico2d import *
import game_framework

import game_world
from background import Background
from player import Player
from heart import Heart
from gate import Gate
from star import Star

# player = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            player.handle_event(event)


def init():
    global background
    global player
    global heart
    global gate
    global star

    running = True

    background = Background()
    game_world.add_object(background, 0)

    player = Player()
    game_world.add_object(player, 1)

    heart = Heart()
    game_world.add_object(heart, 1)

    gate = Gate()
    game_world.add_object(gate, 1)

    star = Star()
    game_world.add_object(star, 1)



    # 충돌 검사 필요 상황을 등록
    # game_world.add_collision_pair('player:ball', player, None)   # 소년을 등록
    # for ball in balls:
    #     game_world.add_collision_pair('player:ball', None, ball)



def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    game_world.handle_collisions()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def pause():
    pass


def resume():
    pass

