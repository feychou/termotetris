from helpers.termcolor import colored

class Board:

    def __init__(self, height, width, offsety, offsetx):
        self.h = height
        self.w = width
        self.oy = offsety
        self.ox = offsetx
        self.matrix = self.generate()
        
    def generate(self):
        matrix = []
        for y in range(0, self.h):
            matrix.append([])
            for x in range(0, self.w):
                if x == 0 or y == (self.h - 1) or x == (self.w - 1):
                    matrix[y].append(1)
                else:
                    matrix[y].append(0)
        return matrix
        
    def draw(self):
        colors = [None, 'white', 'red', 'blue', 'yellow', 'green', 'magenta']
        for row in self.matrix:
            for tile in row:
                color = colors[tile]
                print(colored(("█"," ")[tile==0], color), end="")
            print('\n', end="")
        print('\n')
        
    def destroy_full_rows(self):
        for n in range(0, self.h - 1):
            tot_tiles = 0
            for tile in self.matrix[n]:
                if tile: tot_tiles += 1
            if tot_tiles == self.h:
                del self.matrix[n]
                new_row = []
                for x in range(0, self.w):
                    if x == 0 or x == (self.w - 1):
                        new_row.append(1)
                    else:
                        new_row.append(0)
                self.matrix.insert(0,new_row)
                self.destroy_full_rows()
                
    def set(self, y, x, value):
        self.matrix[y][x] = value
        
    def unset(self, y, x):
        self.matrix[y][x] = 0
        
    def get(self, y, x):
        return self.matrix[y][x]

board = Board(21, 21, 0, 10)
