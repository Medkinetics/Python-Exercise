from random import sample

def tic_tac_toe():
    matrix = []
    s = 3
    win = False  

    for x in range(s):
        y = sample(range(s), s) 
        matrix.append(y)
        print(y)

    #horizontal check:
    for x in range(s):
        if (matrix[x][0] == matrix[x][1] == matrix[x][2]) and matrix[x][0] != 0:
            print("Player {} wins!".format(matrix[x][0]))
            win = True

    #vertical check:
    for x in range(s):
        if (matrix[0][x] == matrix[1][x] == matrix[2][x]) and matrix[0][x] != 0:
            print("Player {} wins!".format(matrix[0][x]))
            win = True

    #diagonal_check:
    if (matrix[0][0] == matrix[1][1] == matrix[2][2]) and matrix[1][1] != 0:
        print("Player {} wins!".format(matrix[1][1]))
        win = True
    elif (matrix[0][2] == matrix[1][1] == matrix[2][0]) and matrix[1][1] != 0:
        print("Player {} wins!".format(matrix[1][1]))
        win = True

    if not win:
        print("Draw..")

tic_tac_toe()