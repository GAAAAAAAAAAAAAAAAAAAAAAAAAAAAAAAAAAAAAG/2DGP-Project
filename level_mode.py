import game_framework
from pico2d import *
import play_mode
import server


def init():
    global image
    #global titleclicksound
    image = load_image('LevelOfDifficulty.png')
    #titleclicksound = load_music('titleclicksound.wav')
    #titleclicksound.set_volume(25)

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
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_e):
            #titleclicksound.play()
            server.level = 1.0
            game_framework.change_mode(play_mode)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_n):
            #titleclicksound.play()
            server.level = 2.0
            game_framework.change_mode(play_mode)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_h):
            #titleclicksound.play()
            server.level = 3.0
            game_framework.change_mode(play_mode)


def draw():
    clear_canvas()
    image.draw(300, 400)
    update_canvas()


def update():
    pass