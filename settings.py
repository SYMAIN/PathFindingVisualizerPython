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
    "TRANS": (1, 1, 1),
    "DARKGREEN": (0, 153, 51)
}
pygame.init()

# screen size
WIDTH, HEIGHT = (800, 800)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

algs = ["BFS", "ASTAR"]

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
    "speed": {
        "val": SliderValue,
        "maxi": SliderMax,
        "mini": SliderMin,
        "xpos": 650,
        "ypos": 175
    }
}

# default button
buttons = {}
buttonsInfo = {
    "BFS": {
        "color": COLOR["WHITE"],
        "highLight": COLOR["TURQUOISE"],
        "msg": "BFS",
        "id": "BFS",
        "dimension": (50, 100),
        "position": (654, 21),
        "screen" : "main"
    },
    "ASTAR": {
        "color": COLOR["WHITE"],
        "highLight": COLOR["TURQUOISE"],
        "msg": "ASTAR",
        "id": "ASTAR",
        "dimension": (50, 100),
        "position": (654, 104),
        "screen" : "main"
    },
    "INSTRUCTION": {
        "color": COLOR["GREEN"],
        "highLight": COLOR["DARKGREEN"],
        "msg": "INSTRUCTION",
        "id": "INSTRUCTION",
        "dimension": (50, 100),
        "position": (654, 704),
        "font": 15,
        "screen" : "main"
    },
    "INSTRU_BACK": {
        "color": COLOR["TURQUOISE"],
        "highLight": COLOR["BLUE"],
        "msg": "BACK",
        "id": "INSTRU_BACK",
        "dimension": (50, 100),
        "position": (50, 700),
        "screen": "instruction"
    }
}

# instructions
instructionText = {
    "title": "Instructions\n\n",
    "text": "Cell:Square in the grid\nRed Cell:End Point\nGreen Cell:Starting Point\nBlack Cell:Border\nDark Grey Cell:Walls\nLight Grey Cell:Empty Cell\n\nOrange Cell:Next to Visit\nYellow Cell:Visited Cell\nBlue Cell:Current Cell\nPurple Cell:Path\n\nTo get started, left click or drag start/end point to desire location on the grid. \nLeft click or drag along empty cells to create walls/obstacles. \nRight drag along walls to delete the walls. \nLeft click on buttons on the right to select different pathfinding algorithms. \nPress ‘space’ to start.\n\nTo erase everything including walls, and reset the grid, press ‘z’. \nTo erase the colors/pathfinding indicators, press ‘x’.\n"
}
