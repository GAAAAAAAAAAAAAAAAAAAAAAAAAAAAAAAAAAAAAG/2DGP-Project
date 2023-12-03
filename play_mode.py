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
from finishline import Finishline
from point import Point


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
    hide_cursor()

    server.background = Background()
    game_world.add_object(server.background, 0)

    server.stop = False

    server.player = Player()
    game_world.add_object(server.player, 2)
    game_world.add_collision_pair('player:gate', server.player, None)
    game_world.add_collision_pair('player:star', server.player, None)
    game_world.add_collision_pair('player:finishline', server.player, None)
    game_world.add_collision_pair('player:point', server.player, None)

    server.hearts = [Heart(450+x*55) for x in range(3)]
    for heart in server.hearts:
        game_world.add_object(heart, 2)

    server.gates = [Gate(None, y*(-500)+(-1000)) for y in range(20)]
    for gate in server.gates:
        game_world.add_object(gate, 2)
        game_world.add_collision_pair('player:gate', None, gate)

    server.stars = [Star(None, y * (-3800) + (-600)) for y in range(10)]
    for star in server.stars:
        game_world.add_object(star, 2)
        game_world.add_collision_pair('player:star', None, star)

    server.finishline = Finishline()
    game_world.add_object(server.finishline, 1)
    game_world.add_collision_pair('player:finishline', None, server.finishline)

    server.points = [Point(None, y * (-80) + (-600)) for y in range(1000)]
    for point in server.points:
        game_world.add_object(point, 2)
        game_world.add_collision_pair('player:point', None, point)

    server.boost = 1



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

