matrix = [[x, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

def game(matrix):
    move = 9
    while True:
        while True:
            user1_turn = input("Player 1, please give the coordinates of your turn (x,y): ") #
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