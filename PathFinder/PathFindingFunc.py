import time
from PathFinder.ASTARClass import Astar
from PathFinder.BFSClass import BFS
import UIfunc as uf
from settings import *

def delayTimer(sec):
    max = sec
    start = time.time()
    while True:
        ### Do other stuff, it won't be blocked
        time.sleep(sec)

        ### This will be updated every loop
        remaining = max + start - time.time()

        ### Countdown finished, ending loop
        if remaining <= 0:
            break

def initStartEnd(start, end):
    start.setStart()
    end.setEnd()

def drawPath(alg, start, end, walls, grid, delay):
    path = []
    uf.clearPath(grid)
    if alg == "BFS":
        path = BFS(start, end, walls, grid, delay).main()
    elif alg == "ASTAR":
        path = Astar(start, end, walls, grid, delay).main()

    initStartEnd(start, end)
    if path == []:
        print("Path not Found")
        return True
    if path is None:
        return False
    for node in path:
        node.setCell(4, COLOR["PURPLE"], True)
    print("Path Found")
    print(alg, len(path))
    return True