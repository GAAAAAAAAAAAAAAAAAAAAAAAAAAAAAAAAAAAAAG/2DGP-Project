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
from heartitem import Heartitem
from gate import Gate
from star import Star
from finishline import Finishline
from point import Point
from minimap import Minimap


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
    game_world.collision_pairs = {}

    server.player = Player()
    game_world.add_object(server.player, 2)
    game_world.add_collision_pair('player:gate', server.player, None)
    game_world.add_collision_pair('player:star', server.player, None)
    game_world.add_collision_pair('player:finishline', server.player, None)
    game_world.add_collision_pair('player:point', server.player, None)
    game_world.add_collision_pair('player:heartitem', server.player, None)

    server.hearts = [Heart(450+x*55) for x in range(3)]
    for heart in server.hearts:
        game_world.add_object(heart, 2)

    #8000 16000 24000
    server.gates = [Gate(None, y*(-500)+(-1000)) for y in range(15*int(server.level))]
    for gate in server.gates:
        game_world.add_object(gate, 2)
        game_world.add_collision_pair('player:gate', None, gate)

    #7900 15800 23700
    server.stars = [Star(None, y * (-3800) + (-600)) for y in range(2*int(server.level))]
    for star in server.stars:
        game_world.add_object(star, 2)
        game_world.add_collision_pair('player:star', None, star)

    server.finishline = Finishline()
    game_world.add_object(server.finishline, 1)
    game_world.add_collision_pair('player:finishline', None, server.finishline)

    #7900 15800 23700
    server.points = [Point(None, y * (-80) + (-600)) for y in range(95*int(server.level))]
    for point in server.points:
        game_world.add_object(point, 2)
        game_world.add_collision_pair('player:point', None, point)

    #8400 14200 20000
    server.heartitems = [Heartitem(None, y * (-5800) + (-2600)) for y in range(1 * int(server.level))]
    for heartitem in server.heartitems:
        game_world.add_object(heartitem, 2)
        game_world.add_collision_pair('player:heartitem', None, heartitem)

    server.minimap = Minimap()
    game_world.add_object(server.minimap, 1)

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

