import pygame
from kuai import Kuai

white = (255, 255, 255)
red = (255, 0, 0)


class View:
    def __init__(self, screen_res):
        pygame.init()
        self.screen = pygame.display.set_mode(screen_res)
        self.background = pygame.Surface(self.screen.get_size())
        Kuai.on('square', self.draw_square)
        Kuai.on('line', self.draw_line)
        Kuai.on('circle', self.draw_circle)
        Kuai.on('point', self.draw_point)
        Kuai.on('update-view', self.update)
        Kuai.emit('view-loaded')

    def update(self):
        pygame.display.update()

    def draw_circle(self, color, x, y, radius, width=0):
        pygame.draw.circle(self.screen, color, (x, y), radius, width)
        Kuai.emit('update-view')

    def draw_line(self, color, start_pos, end_pos, width=1):
        pygame.draw.line(self.screen, color, start_pos, end_pos, width)
        Kuai.emit('update-view')

    def draw_square(self, color, x, y, height, border=0):
        height = 20
        pygame.draw.rect(self.screen, color, (x, y, height, height), border)
        Kuai.emit('update-view')

    def draw_point(self, color, x, y):
        pygame.draw.rect(self.screen, color, (x, y, 1, 1))
        Kuai.emit('update-view')
