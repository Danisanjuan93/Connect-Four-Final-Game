from games import *

def h1(state):
    bestO = 0
    bestX = 0
    totalO = 0
    totalX = 0
    if state.utility == 1:
        return infinity
    if state.utility == -1:
        return -infinity

    for x in legal_moves(state):
        totalX += k_in_row(state.board, x, 'X',(0,1))
        totalX += k_in_row(state.board, x, 'X',(1,0))
        totalX += k_in_row(state.board, x, 'X',(1,1))
        totalX += k_in_row(state.board, x, 'X',(1,-1))
        totalO += k_in_row(state.board, x, 'O',(0,1))
        totalO += k_in_row(state.board, x, 'O',(1,0))
        totalO += k_in_row(state.board, x, 'O',(1,1))
        totalO += k_in_row(state.board, x, 'O',(1,-1))

        if totalO > bestO:
            bestO = totalO
        if totalX > bestX:
            bestX = totalX
    return bestX - bestO


def legal_moves(state):

    return [(x, y) for (x, y) in state.moves
            if y == 1 or (x, y-1) in state.board]

def k_in_row (board, move, player,(delta_x,delta_y)):
    x, y = move
    n = 0
    p = 1
    z = 0
    while (board.get((x, y)) == None or board.get((x, y)) == player) and y < 7 and x < 8:
         if x == (x + delta_x):
             if board.get((x, y)) == None:
                 n += 50 * p
                 p -= 0.10
         elif y == (y + delta_y):
             if board.get((x, y)) == player:
                z += 1
                n += 100
             elif board.get((x, y)) == None:
                n += 50
         elif y != (y + delta_y) and x != (x + delta_x):
             if board.get((x, y)) == player:
                 z += 1
                 n += 100
             elif board.get((x, y)) == None:
                 n += 50 * p
                 p -= 0.10
         x, y = x + delta_x, y + delta_y

    x, y = move
    p = 1
    while (board.get((x, y)) == None or board.get((x, y)) == player) and y > 0 and x > 0:
        if x == (x - delta_x):
             if board.get((x, y)) == player:
                 z += 1
                 n += 100
        elif y == (y - delta_y):
             if board.get((x, y)) == player:
                 z += 1
                 n += 100
             elif board.get((x, y)) == None:
                 n += 50
        elif y != (y - delta_y) and x != (x - delta_x):
             if board.get((x, y)) == player:
                 z += 1
                 n += 100
             elif board.get((x, y)) == None:
                 n += 50 * p
                 p -= 0.10
        x, y = x - delta_x, y - delta_y

    if z == 3:
        if player == 'X':
            n *= 6
        else:
            n *= 12
    if z >= 4:
        if player == 'X':
            n *= 9
        else:
            n *= 18
    return n