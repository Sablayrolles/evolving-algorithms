import pyglet
import config
from system.component import Component
from entities.ball import Ball
from random import randint

window = pyglet.window.Window(height=config.window_height,
                              width=config.window_width)

ball_objects = []


def draw():
    """
    Clears screen and then renders our list of ball objects
    :return:
    """
    window.clear()
    for ball in ball_objects:
        ball.draw_self()


def update(time):
    """
    Updates our list of ball objects
    :param time:
    :return:
    """
    for ball in ball_objects:
        if isinstance(ball, Component):
            ball.update_self()


@window.event
def on_mouse_press(x, y, button, modifiers):
    """
    On each mouse click, we create a new ball object
    """
    print('x: {}, y: {}'.format(x, y))
    ball_objects.append(Ball(x=x, y=y, speed=randint(3, 12)))


def main():
    """
    This is the main method. This contains an embedded method
    :return:
    """
    @window.event
    def on_draw():
        draw()
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()

main()
