from functools import reduce


def multiply_arr(row):
    return reduce(lambda a, b: a*b, row)

def all_zeros(num):
    return reduce(lambda a,b: a+b , num)


def is_solved(board):
    counter = []
    col1 = []
    col2 = []
    col3 = []


    left_diag = [board[0][0], board[1][1], board[2][2]]
    right_diag =[board[0][2], board[1][1], board[2][0]]

    counter.append(multiply_arr(left_diag))
    counter.append(multiply_arr(right_diag))

    for row in board:
        creating_columns_from_rows(col1, col2, col3, row)
        counter.append(multiply_arr(row))

    add_col_to_counter(counter, col1, col2, col3)


    print (f'counter: {counter} ')

    for num in counter:
        if 1 in counter:
            final = 1
        elif 8 in counter :
            final= 2
        elif all_zeros(counter) ==0 or 0 in counter and not 1 in counter or 8 in counter:
            final = -1 
        else:
            final =0

    return final 


def creating_columns_from_rows(col1, col2, col3, row):
    col1.append(row[0])
    col2.append(row[1])
    col3.append(row[2])

def add_col_to_counter(counter, col1, col2, col3):
    counter.append(multiply_arr(col1))
    counter.append(multiply_arr(col2))
    counter.append(multiply_arr(col3))




# retrieving all the columns from the board

board = [[2, 2, 1],
         [2, 2, 1],
         [1, 1, 2]]

print(is_solved(board))
# test.assert_equals(is_solved(board), -1)

# # winning row
# board = [[1, 1, 1],
#          [0, 2, 2],
#          [0, 0, 0]]
# test.assert_equals(is_solved(board), 2)

# # winning column
# board = [[2, 1, 2],
#          [2, 1, 1],
#          [1, 1, 2]]
# test.assert_equals(is_solved(board), 1)

# # draw

# test.assert_equals(is_solved(board), 0)