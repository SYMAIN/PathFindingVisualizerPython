import pygame

COLOR = {
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "GREY": (150, 150, 150),
    "GREEN": (0, 255, 0),
    "RED": (255, 0, 0),
    "TURQUOISE": (0, 183, 255),
    "ORANGE": (255, 102, 0),
    "YELLOW": (255, 255, 0),
    "BLUE": (0, 0, 255),
    "PURPLE": (170, 0, 204),
    "DARKGREY": (50, 50, 50),
    "TRANS" : (1, 1, 1)
}
pygame.init()

# screen size
WIDTH, HEIGHT = (800, 800)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# grid size base on squares
# interface
panelSize = 10
height = 50
width = 50 - panelSize
# square sizes
CELLSIZE = WIDTH // height

# default slider
sliders = []
SliderValue = 1
SliderMin = 0
SliderMax = 1
sliderFontSize = 15

slidersInfo = {
    "speed":{
        "val":SliderValue,
        "maxi":SliderMax,
        "mini":SliderMin,
        "xpos":655,
        "ypos":275
    }
}

# default button
buttons = {}
