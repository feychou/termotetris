from random import choice
from helpers.getch import getch
from brick import board, bricks

valid_keys = ('a', 'w', 's', 'd', 'x', 'q')

def reset():
    global current_brick
    current_brick.reset()
    board.oy = 0
    board.ox = 10
    current_brick = draw_brick()

def draw_brick():
    global bricks
    return bricks[choice(list(bricks.keys()))]

def valid_move(next_brick, nextox, nextoy):
    for n, row in enumerate(next_brick):
        for c, stone in enumerate(row):
            if stone:
                if board.get(nextoy + n, nextox + c):                    
                    return False
    return True

def collision():
    for n, row in enumerate(current_brick.shape):
        for c, stone in enumerate(row):
            if stone:
                if board.get(board.oy + n + 1, board.ox + c):                        
                    return True
    return False
             
def game_loop():
    while True:
        current_brick.insert()
        board.draw()
        current_brick.remove()
        if collision():
            current_brick.insert()
            board.destroy_full_rows()            
            reset()
            if valid_move(current_brick.shape, board.ox, board.oy):
                current_brick.insert()
            else:
                print("GAME OVER")
                quit()
            board.draw()
            current_brick.remove()
        key = getch()
        if key in valid_keys:
            if key == 'a' or key == 'd':
                shape, ox, oy = current_brick.move(key)
            elif key == 'w' or key == 's':
                shape, ox, oy = current_brick.rotate(key)
            elif key == 'x':
                shape, ox, oy = current_brick.push_down()
            elif key == 'q':
                quit()
            if valid_move(shape, ox, oy):
                current_brick.shape, board.ox, board.oy = shape, ox, oy
                if not collision():
                    board.oy += 1 
        else:
            print("Please give a valid input: a, d, w, s, q")       

current_brick = draw_brick()        
        
if __name__ == '__main__':
    game_loop()
