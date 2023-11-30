import game_framework
from pico2d import *
import title_mode

def init():
    global image
    image = load_image('gameover.png')

def finish():
    global image
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_r):
            game_framework.change_mode(title_mode)


def draw():
    clear_canvas()
    image.draw(300,400)
    update_canvas()


def update():
    pass