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
                        print("Key!")
                        Kuai.emit('key-up', x, y)
                    if event.key == pygame.K_DOWN:
                        print("Key!")
                        Kuai.emit('key-down', x, y)
                    if event.key == pygame.K_LEFT:
                        print("Key!")
                        Kuai.emit('key-left', x, y)
                    if event.key == pygame.K_RIGHT:
                        print("Key!")
                        Kuai.emit('key-right', x, y)
                    if event.key == pygame.K_ESCAPE:
                        print("Key!")
                        Kuai.emit('key-escape')
                    pass
