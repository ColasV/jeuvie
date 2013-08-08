import argparse
import time
import random
 
class Grid(object):

    # init method
    # square grid
    def __init__(self, gridsize):
        self._xsize = gridsize
        self._ysize = gridsize
        self.initgrid()
 
    # initialize the grid
    def initgrid(self):
        self.grid = [[random.randint(0,1)  for y in range(self._ysize)] for x in range(self._xsize)]
 
 
    def _next(self):
        # initialize mtx temporary neighbourgs matrix
        mtx = [[0 for y in range(self._ysize)] for x in range(self._xsize)]
 
        # puts number of neighbours in each cell
        for j, y in enumerate(self.grid):
            for i, x in enumerate(y):
                if x == 1:
                    # adds 1 to adjacent cells
                    for n in range(-1, 2):
                        for m in range(-1, 2):
                            if not (n == 0 and m == 0) \
                              and 0 <= i + n < self._xsize \
                              and 0 <= j + m < self._ysize:
                                mtx[j+m][i+n] += 1
        
        # modifies current grid using mtx
        for j, y in enumerate(mtx):
            for i, x in enumerate(y):
                # cell dies
                if not 1 < x < 4:
                    self.grid[j][i] = '0'
                elif x == 3:
                    self.grid[j][i] = '1'
 
 
    def start(self):
        while True:
            print(self)
            self._next()
            time.sleep(1)
 
 
    def __str__(self):
        strg = ''
        for i in range(self._xsize):
            for j in range(self._ysize):
                strg += str(self.grid[i][j])

            strg += "\n"
        return strg
 
#############
# Main
#############

J = Grid(20)
J.start()