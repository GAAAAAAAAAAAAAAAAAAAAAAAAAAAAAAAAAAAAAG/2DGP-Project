import game_framework
from pico2d import *
import title_mode
import server

def init():
    global image
    global pointprint
    image = load_image('gameclear.png')
    pointprint = load_font('ENCR10B.TTF', 30)

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
    pointprint.draw(150, 580, f'your point : {server.player.point_count}', (0, 0, 0))
    update_canvas()


def update():
    pass