from pico2d import load_image


class Background:
    def __init__(self):
        #self.image = load_image('background1.png')
        self.image = load_image('Scrallbackground.png')

    def draw(self):
        self.image.draw(300, 400)

    def update(self):
        pass
