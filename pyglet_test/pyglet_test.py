import pyglet
import config

window = pyglet.window.Window(height=config.window_height,
                              width=config.window_width)


def init():
    """
    Sets up pyglet application 
    :return: 
    """
    pass


def keys(**kwargs):
    print(kwargs)


def main():
    """
    Main function 
    :return: nothing 
    """
    pyglet.app.run()


main()
keys(something='nig', hello='hehe')
