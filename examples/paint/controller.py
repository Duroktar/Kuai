import time
import pygame
from kuai import Kuai


class Controller:
    def __init__(self):
        self.is_done = False

    def stop(self):
        self.is_done = True

    def run(self):
        while not self.is_done:
            time.sleep(0.01)
            x, y = pygame.mouse.get_pos()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        Kuai.emit('key-up', x, y)
                    if event.key == pygame.K_DOWN:
                        Kuai.emit('key-down', x, y)
                    if event.key == pygame.K_LEFT:
                        Kuai.emit('key-left', x, y)
                    if event.key == pygame.K_RIGHT:
                        Kuai.emit('key-right', x, y)
                    if event.key == pygame.K_ESCAPE:
                        Kuai.emit('key-escape')
                    pass
