def done_or_not(board):
    row_list = board
    column_list = []
    squares = []
    correct = [1,2,3,4,5,6,7,8,9]

    col_number = 0 

    while col_number < 9: 
        col_list = []
        for i in range(9):
            col_list.append(board[i][col_number])

        column_list.append(col_list)
        col_number += 1


    for i in range(3):
        for j in range(3):
            squares.append(board[i][j])
        
        for j in range(3,6):
            squares.append(board[i][j])

        for j in range(6,9):
            squares.append(board[i][j])

    for i in range(6):
        for j in range(3):
            squares.append(board[i][j])
        
        for j in range(3,6):
            squares.append(board[i][j])

        for j in range(6,9):
            squares.append(board[i][j])

    for i in range(9):
        for j in range(3):
            squares.append(board[i][j])
        
        for j in range(3,6):
            squares.append(board[i][j])

        for j in range(6,9):
            squares.append(board[i][j])

    counter = 0
    for stuff in col_list,row_list,squares:
        if len(correct) == len(set(stuff)):
            counter+=1 

    print(counter)


        


print(done_or_not(
                [[1, 3, 2, 5, 7, 9, 4, 6, 8]
                ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]))