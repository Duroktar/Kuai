from kuai import Kuai
from view import View, white, red
from controller import Controller
import random

resolution = (800, 600)
view = View(resolution)
controller = Controller()


def draw_squid(x, y):
    print("Draw squid!")
    Kuai.emit('circle', white, x, y, random.randrange(5, 15))


def draw_worm(x, y):
    print("Draw worm!")
    Kuai.emit('line', white, (x, y),
              (random.randrange(0, 799), random.randrange(0, 599)), 1)


def draw_turtle(x, y):
    print("Draw turtle!")
    Kuai.emit('square', red, x, y, random.randrange(5, 20))


def draw_speck(x, y):
    print("Draw speck!")
    Kuai.emit('point', red, x, y)


def confirm_exit(msg=None):
    if msg:
        print("Select y or n..")
    conf = input("Sure you want to exit?  n [y] $ ").lower() or 'y'
    if conf not in ['y', 'n']:
        confirm_exit()
    else:
        if conf == 'y':
            Kuai.emit('display-is-done')


def greeting():
    print(f"Welcome to the demo! Pygame is ready to go~")


if __name__ == '__main__':
    Kuai.on('key-up', draw_squid)
    Kuai.on('key-down', draw_worm)
    Kuai.on('key-left', draw_turtle)
    Kuai.on('key-right', draw_speck)
    Kuai.on('key-escape', confirm_exit)
    Kuai.on('display-is-done', controller.stop)
    Kuai.on('view-loaded', greeting)
    controller.run()
