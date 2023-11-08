from pico2d import *

import game_world
from background import Background

from player import Player


# Game object class here


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            player.handle_event(event)


def reset_world():
    global running
    global background
    global team
    global player

    running = True

    background = Background()
    game_world.add_object(background, 0)


    player = Player()
    game_world.add_object(player, 1)




def update_world():
    game_world.update()


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


open_canvas(600,800)
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
