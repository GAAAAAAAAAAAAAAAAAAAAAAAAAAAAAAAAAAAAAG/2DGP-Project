import random
import json
import tomllib
import os

from pico2d import *
import game_framework
import server
import game_world

#from background import InfiniteBackground as Background

from background import Background
from player import Player
from heart import Heart
from gate import Gate
from star import Star

# player = None
hearts = None
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            server.player.handle_event(event)


def init():
    # global background
    # global player
    # global hearts
    # global gate
    # global star
    #
    # running = True

    hide_cursor()

    server.background = Background()
    game_world.add_object(server.background, 0)

    server.player = Player()
    game_world.add_object(server.player, 1)
    game_world.add_collision_pair('player:gate', server.player, None)

    server.hearts = [Heart(450+x*55) for x in range(3)]
    for heart in server.hearts:
        game_world.add_object(heart, 1)

    # gate = Gate()
    # game_world.add_object(gate, 1)

    server.gates = [Gate(None, y*(-500)+(-1000)) for y in range(100)]
    for gate in server.gates:
        game_world.add_object(gate, 1)
        game_world.add_collision_pair('player:gate', None, gate)


    # for _ in range(100):
    #     gate = Gate()
    #     game_world.add_object(gate, 1)
    #     game_world.add_collision_pair('player:gate', None, gate)

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

