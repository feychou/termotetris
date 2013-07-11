from board import board

class Brick:

    def __init__(self, shape):
        self.original  = shape
        self.shape = shape
        
    def rotate(self, direction):
        if direction == 'w':
            next_brick = list(zip(*self.shape[::-1]))
        else:
            next_brick = list(zip(*self.shape))[::-1]
        return next_brick, board.ox, board.oy
        
    def move(self, direction):
        nextox = (board.ox + 1, board.ox - 1)[direction == 'a']
        return self.shape, nextox, board.oy
                
    def push_down(self):
        nextoy = board.oy + 1
        return self.shape, board.ox, nextoy
        
    def insert(self):
        for n, row in enumerate(self.shape):
            for c, stone in enumerate(row):
                if stone:
                    board.set(board.oy + n, board.ox + c, stone)
                    
    def remove(self):
        for n, row in enumerate(self.shape):
            for c, stone in enumerate(row):
                if stone:
                    board.unset(board.oy + n, board.ox + c)
                    
    def reset(self):
        self.shape = self.original
        
red       = Brick([(2, 0, 0), (2, 0, 0), (2, 2, 0)])
blue      = Brick([(0, 3, 0), (0, 3, 0), (3, 3, 0)])
yellow    = Brick([(4, 4),(4, 4)])
green     = Brick([(5, 5, 5, 5),(0, 0, 0, 0)])
purple    = Brick([(0, 6),(6, 6),(6, 0)])
bricks    = {'red' : red, 'blue' : blue, 'yellow' : yellow, 'green' : green, 'purple' : purple}
