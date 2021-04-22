from UI.BUTTONClass import button
from UI.NODEClass import NODE
from UI.SLIDERClass import slider
from settings import *


def createGrid():
    grid = [[NODE(j, i, CELLSIZE) for i in range(width)] for j in range(height)]
    # border
    for i in range(width):
        grid[0][i].setCell(-1, COLOR["BLACK"], True)
        grid[height - 1][i].setCell(-1, COLOR["BLACK"], True)
    for j in range(height):
        grid[j][0].setCell(-1, COLOR["BLACK"], True)
        grid[j][width - 1].setCell(-1, COLOR["BLACK"], True)
    return grid


def getMousePos():
    mouseCol, mouseRow = pygame.mouse.get_pos()
    mouseX, mouseY = mouseCol // CELLSIZE, mouseRow // CELLSIZE
    return mouseY, mouseX


def valid(x, y):
    return 0 < x < width - 1 and 0 < y < height - 1


def createPath(start, end):
    path = []
    current = end
    while not current.posEqual(start):
        path.append(current)
        current = current.parent
    path.pop(0)
    return path


def reDrawScreen(grid):
    screen.fill(COLOR["GREY"])  # set background color
    # draw grid
    for i in grid:
        for cell in i:
            cell.draw(screen)
    for bnt in buttons.values():
        bnt.draw(screen)

    for s in sliders:
        s.draw()
    pygame.display.update()


def clearPath(grid):
    for i in grid:
        for j in i:
            if j.state == 4 or j.state == 5 or j.state == 6:
                j.resetCell()


def clearALL(grid, walls):
    for i in grid:
        for j in i:
            if j.state != 1 and j.state != 2 and j.state != -1:
                if j.state == 3:
                    walls.remove(j)
                j.resetCell()

def createSlider(name,info):
    return slider(name,info["val"],info["maxi"],info["mini"],info["xpos"],info["ypos"])

def loadSlider():
    for name,s in slidersInfo.items():
        newSlider = createSlider(name,s)
        sliders.append(newSlider)

def sliderClicked():
    pos = pygame.mouse.get_pos()
    for s in sliders:
        if s.button_rect.collidepoint(pos):
            s.hit = True

def createButton(col, row, l, w, color, hl, msg, id):
    return button(col, row, l, w, color, hl, msg, id)

def loadBUttons():
    for key,value in buttonsInfo.items():
        buttons[key] = createButton(value["position"][0], value["position"][1], value["dimension"][0],
                                    value["dimension"][1], value["color"], value["highLight"], value["msg"],
                                    value["id"])
        if key in algs:
            buttons[key].algSet = False

        if key == "BFS":
            # init the default alg
            buttons[key].highLighted = True
            buttons[key].algSet = True


def buttonHover():
    # highlight button when hovering over
    for bnt in buttons.values():
        if bnt.onButton(pygame.mouse.get_pos()):
            bnt.highlightButton()
        else:
            bnt.unhighlightButton()

def buttonClicked(alg):
    """
    function to change alg base on button clicked +
    activate functionality of buttons
    """
    # check if one of the button is clicked
    buttonChanged = [False]
    for bnt in buttons.values():
        if bnt.onButton(pygame.mouse.get_pos()):
            if bnt.algSet is None: # not a alg button
                if bnt.id == "INSTRUCTION":
                    instructions()
                return alg
            if not bnt.algSet:
                bnt.highlightButton()
                alg = bnt.id
                buttonChanged = [True,bnt]
                bnt.algSet = True
                break

    if buttonChanged[0]:
        for bnt in buttons.values():
            if bnt == buttonChanged[1]:
                continue
            else:
                if bnt.algSet is None:
                    continue
                bnt.unhighlightButton()
                bnt.algSet = False
    return alg

def instructions():
    run = True
    while run:
        screen.fill(COLOR["GREY"])  # set background color
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                exit()

            for key,bnt in buttons.items():
                if key == "BACK":
                    return

        titlefont = pygame.font.SysFont("comicsans", 40)
        titleRect = pygame.Rect((0, 20, screen.get_rect().width, 80))
        rendered_title = render_textrect(instructionText["title"],titlefont,titleRect,COLOR["BLACK"],COLOR["GREY"],1)

        textfont = pygame.font.SysFont("comicsans", 30)
        textRect = pygame.Rect((15, 100, screen.get_rect().width, 700))
        rendered_text = render_textrect(instructionText["text"],textfont,textRect,COLOR["DARKGREY"],COLOR["GREY"])

        if rendered_text:
            screen.blit(rendered_text, textRect.topleft)
        if rendered_title:
            screen.blit(rendered_title,titleRect.topleft)


        pygame.display.update()

class TextRectException:
    def __init__(self, message = None):
        self.message = message
    def __str__(self):
        return self.message

def render_textrect(string, font, rect, text_color, background_color, justification=0):
    # http://www.pygame.org/pcr/text_rect/index.php

    """Returns a surface containing the passed text string, reformatted
    to fit within the given rect, word-wrapping as necessary. The text
    will be anti-aliased.

    Takes the following arguments:

    string - the text you wish to render. \n begins a new line.
    font - a Font object
    rect - a rectstyle giving the size of the surface requested.
    text_color - a three-byte tuple of the rgb value of the
                 text color. ex (0, 0, 0) = BLACK
    background_color - a three-byte tuple of the rgb value of the surface.
    justification - 0 (default) left-justified
                    1 horizontally centered
                    2 right-justified

    Returns the following values:

    Success - a surface object with the text rendered onto it.
    Failure - raises a TextRectException if the text won't fit onto the surface.
    """
    final_lines = []

    requested_lines = string.splitlines()

    # Create a series of lines that will fit on the provided
    # rectangle.

    for requested_line in requested_lines:
        if font.size(requested_line)[0] > rect.width:
            words = requested_line.split(' ')
            # if any of our words are too long to fit, return.
            for word in words:
                if font.size(word)[0] >= rect.width:
                    raise Exception(TextRectException, "The word " + word + " is too long to fit in the rect passed.")
            # Start a new line
            accumulated_line = ""
            for word in words:
                test_line = accumulated_line + word + " "
                # Build the line while the words fit.
                if font.size(test_line)[0] < rect.width:
                    accumulated_line = test_line
                else:
                    final_lines.append(accumulated_line)
                    accumulated_line = word + " "
            final_lines.append(accumulated_line)
        else:
            final_lines.append(requested_line)

            # Let's try to write the text out on the surface.

    surface = pygame.Surface(rect.size)
    surface.fill(background_color)

    accumulated_height = 0
    for line in final_lines:
        if accumulated_height + font.size(line)[1] >= rect.height:
            raise Exception (TextRectException, "Once word-wrapped, the text string was too tall to fit in the rect.")
        if line != "":
            tempsurface = font.render(line, 1, text_color)
            if justification == 0:
                surface.blit(tempsurface, (0, accumulated_height))
            elif justification == 1:
                surface.blit(tempsurface, ((rect.width - tempsurface.get_width()) / 2, accumulated_height))
            elif justification == 2:
                surface.blit(tempsurface, (rect.width - tempsurface.get_width(), accumulated_height))
            else:
                raise Exception (TextRectException, "Invalid justification argument: " + str(justification))
        accumulated_height += font.size(line)[1]

    return surface