from random import sample

a = int(input('Enter the number of times : '))

def horizontal():
    print(" --- " * (a))
    return  
    
def vertical():
    print("|    " * (a+1))
    return

for n1 in range(1, a+1):
    horizontal()
    vertical() 

#------------------------------------------------

matrix = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

def game(matrix):
    move = 9
    while True:
        while True:
            user1_turn = input("Player 1, please give the coordinates as (x,y): ") 
            user1_turn_list = user1_turn.split(",")
            if matrix [int(user1_turn_list[0])] [int(user1_turn_list[1])] != 0:
                print("The position is already occupied try again")
            else:
                matrix[int(user1_turn_list[0])][int(user1_turn_list[1])] = 'x'
                move = move - 1
                print(matrix)
                break

        if move == 0:
            break

        while True:
            user2_turn = input("Player 2, please give the coordinates of your turn (x,y): ")
            user2_turn_list = user2_turn.split(",")
            if matrix [int(user2_turn_list[0])] [int(user2_turn_list[1])] != 0:
                print("The position is already occupied try again")
            else:
                matrix[int(user2_turn_list[0])][int(user2_turn_list[1])] = 'O'
                move = move - 1
                print(matrix)
                break

        if move == 0:
            break

game(matrix)
#------------------------------------------------

def tic_tac_toe():
    
    s = 3
    win = False  
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

       
 
