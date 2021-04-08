puzzle = [
    [0, 7, 0, 0, 0, 0, 0, 0, 9],
    [5, 0, 9, 4, 2, 7, 6, 0, 3],
    [0, 8, 6, 3, 9, 0, 0, 1, 4],
    [0, 0, 8, 5, 4, 1, 3, 7, 2],
    [0, 0, 0, 7, 0, 6, 9, 4, 5],
    [4, 0, 7, 9, 3, 0, 1, 6, 8],
    [0, 0, 2, 0, 7, 0, 5, 0, 1],
    [0, 3, 5, 6, 0, 0, 4, 2, 7],
    [7, 4, 1, 2, 5, 3, 8, 9, 6]
]

ANSWER = [
    [3, 7, 4, 1, 6, 8, 2, 5, 9],
    [5, 1, 9, 4, 2, 7, 6, 8, 3],
    [2, 8, 6, 3, 9, 5, 7, 1, 4],
    [6, 9, 8, 5, 4, 1, 3, 7, 2],
    [1, 2, 3, 7, 8, 6, 9, 4, 5],
    [4, 5, 7, 9, 3, 2, 1, 6, 8],
    [9, 6, 2, 8, 7, 4, 5, 3, 1],
    [8, 3, 5, 6, 1, 9, 4, 2, 7],
    [7, 4, 1, 2, 5, 3, 8, 9, 6]
]

NUMS = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def possible_values(arr):
    return list(filter(lambda x: x not in arr, NUMS))


def possible_horizontal_values(puzzle, row_index):
    row = puzzle[row_index]
    return possible_values(row)


def possible_vertical_values(puzzle, column_index):
    column = list(map(lambda x: x[column_index], puzzle))
    return possible_values(column)


def possible_square_values(puzzle, row_index, column_index):
    square = []
    for i in range(row_index, row_index + 3):
        print(f'row: {i}')
        for j in range(column_index, column_index + 3):
            print(f'column: {j}')
            square.append(puzzle[i][j])
    return possible_values(square)


def is_completed(puzzle):
    for row in puzzle:
        for cell in row:
            if cell == 0:
                return False
    return True


def get_matches(row, column, square):
    matches = []
    for num in NUMS:
        if num in row and num in column and num in square:
            matches.append(num)
    return matches


STACK = []


def steps_taken(num, row, column, possible_moves):
    STACK.append({
        'num': num,
        'row': row,
        'column': column,
        'possible_moves': possible_moves
    })


def main():
    while not is_completed(puzzle):
        for row in range(9):
            for column in range(9):
                if puzzle[row][column] == 0:
                    print(f'Row: {row}, Column: {column} is empty')
                    horizontal_values = possible_horizontal_values(puzzle, row)
                    vertical_values = possible_vertical_values(puzzle, column)
                    square_values = possible_square_values(puzzle, row - (row % 3), column - (column % 3))
                    matches = get_matches(horizontal_values, vertical_values, square_values)
                    if not matches:
                        undo_moves(STACK)
                    else:
                        for match in matches:
                            fill_board(match, row, column, matches)
    if puzzle == ANSWER:
        print('correct')
    print(puzzle)


def undo_moves(stack):
    possible_moves = []
    while not possible_moves:
        move = stack.pop()
        puzzle[move.get('row')][move.get('column')] = 0  # undo the move
        possible_moves = move.get('possible_moves')
    if possible_moves:
        fill_board(possible_moves[0], move.get('row'), move.get('column'), possible_moves)


def fill_board(num, row, column, matches):
    remaining_matches = list(filter(lambda x: x is not num, matches))
    puzzle[row][column] = num
    steps_taken(num, row, column, remaining_matches)


main()