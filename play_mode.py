import random

from pico2d import *
import game_framework

import game_world
from background import Background
from player import Player

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

    running = True

    background = Background()
    game_world.add_object(background, 0)

    player = Player()
    game_world.add_object(player, 1)



    # 충돌 검사 필요 상황을 등록
    # game_world.add_collision_pair('player:ball', player, None)   # 소년을 등록
    # for ball in balls:
    #     game_world.add_collision_pair('player:ball', None, ball)



def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    # fill here
    # for ball in balls.copy():
    #     if game_world.collide(player, ball):
    #         print('COLLISION player:Ball')
    #         player.ball_count += 1     # 소년 관점의 충돌처리
    #         balls.remove(ball)
    #         game_world.remove_object(ball)  # 볼을 제거

    game_world.handle_collisions()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def pause():
    pass


def resume():
    pass

