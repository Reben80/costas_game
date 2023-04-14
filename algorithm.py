def calculate_slope(p1, p2):
    return (p2[1] - p1[1]) / (p2[0] - p1[0]) if p2[0] != p1[0] else None

def is_move_legal(distinct_points, distinct_slopes, point) -> bool:

    """
    DESCRIPTION: will take in a point and information about the current grid. Decides if moving to that point is legal.

    PARAM: the array of distinct points already in the grid
    PARAM: the array of distinct slopes already in the grid
    PARAM: the point the player is trying to add
    """

    is_legal_point = True
    distinct_x = []
    distinct_y = []

    for distinct_point in distinct_points:
        distinct_x.append(distinct_points[distinct_point][0])
        distinct_y.append(distinct_points[distinct_point][0])

    if point in distinct_points:
        is_legal_point = False


    if (point[0] in distinct_x) | (point[0] in distinct_y):
        is_legal_point = False

    for i in range(len(distinct_points) - 1):
        slope = calculate_slope(distinct_points[i], point)
        if slope in distinct_slopes:
            is_legal_point = False

    return is_legal_point




def get_next_possible_boards(distinct_points, distinct_slopes, player1: bool, n, m) -> list:

    """
    DESCRIPTION: takes in data about the current state of the game then outputs a list of all possible next boards.
    Where each entry corresponds to a list of the next board's information - the distinct points, distinct slopes, and if player1 made the last move

    PARAM: the list of distrinct points for the current board
    PARAM: the list of distrinct slopes for the current board
    PARAM: the boolean of if it is player1's turn
    PARAM: the n rows of the grid
    PARAM: the m columns of the grid

    RETURN: a list of each possible board's information for the next move
    """

    next_possible_boards = []

    distinct_x = []
    distinct_y = []

    for distinct_point in distinct_points:
        distinct_x.append(distinct_points[distinct_point][0])
        distinct_y.append(distinct_points[distinct_point][0])

    for x in range(0, m):
        if x not in distinct_x:

            for y in range (0, n):
                if y not in distinct_y:

                    point = (x, y)
                    if is_move_legal(distinct_points, distinct_slopes, point):

                        new_board = []
                        next_distinct_points = distinct_points
                        next_distinct_slopes = distinct_slopes

                        next_distinct_points.append(point)
                        next_distinct_slopes.append(calculate_slope(distinct_point))

                        new_board.append(next_distinct_points)
                        new_board.append(next_distinct_slopes)
                        new_board.append(player1)

                        next_possible_boards.append(new_board)

    return next_possible_boards


# this function will be run if the len of the output of get_next_possible_boards is 0
def who_wins(distinct_points, distinct_slopes, player1: bool) -> bool:

    """
    DESCRIPTION: takes in the data about the current board and outputs if player1 won

    PARAM: the list of distrinct points for the current board
    PARAM: the list of distrinct slopes for the current board
    PARAM: the boolean of if it is player1's turn

    RETURN: returns True, if player1 one won this configuration. Returns False if player2 won this configuration.
    """

    if player1:
        return False

    else:
        return True
    
def check_costas_array_is_costas_game(standard_notation_points: list) -> bool:

    is_valid_board = True
    distinct_points = []
    distinct_slopes = []

    for column in range(len(standard_notation_points)):
        point = (column + 1, standard_notation_points[column])
        distinct_points.append(point)

        for distinct_point in distinct_points:
                slope = calculate_slope(point, distinct_point)

                if (slope in distinct_slopes) & (slope != None):
                    is_valid_board = False

                distinct_slopes.append(slope)

    return is_valid_board

def filter_costas_arrays_for_games(costas_arrays: list) -> list:
    
    filtered_costas_arrays = []

    for array in costas_arrays:
        check = check_costas_array_is_costas_game(array)

        if check:
            filtered_costas_arrays.append(array)

    return filtered_costas_arrays

print(filter_costas_arrays_for_games([[1, 2, 6, 4, 7, 3, 5],  [1, 2, 7, 4, 6, 5, 3],  [1, 2, 7, 5, 4, 6, 3],  [1, 3, 6, 2, 7, 4, 5],  [1, 3, 6, 2, 7, 5, 4],  [1, 3, 7, 6, 4, 5, 2],  [1, 4, 5, 3, 7, 6, 2],  [1, 4, 5, 7, 2, 6, 3],  [1, 4, 6, 5, 3, 7, 2],  [1, 5, 3, 6, 7, 2, 4],  [1, 5, 7, 6, 3, 4, 2],  [1, 6, 5, 7, 3, 4, 2],  [1, 7, 3, 4, 6, 5, 2],  [2, 1, 5, 7, 3, 6, 4],  [2, 1, 6, 4, 7, 3, 5],  [2, 3, 5, 1, 7, 6, 4],  [2, 4, 3, 6, 7, 1, 5],  [2, 4, 5, 1, 7, 6, 3],  [2, 4, 7, 3, 1, 6, 5],  [2, 5, 1, 6, 7, 4, 3],  [2, 5, 1, 7, 6, 3, 4],  [2, 5, 6, 1, 3, 7, 4],  [2, 5, 6, 4, 1, 7, 3],  [2, 5, 7, 1, 6, 3, 4],  [2, 5, 7, 1, 6, 4, 3],  [2, 6, 1, 3, 4, 7, 5],  [2, 6, 7, 1, 4, 3, 5],  [3, 2, 5, 7, 1, 6, 4],  [3, 4, 1, 7, 6, 2, 5],  [3, 6, 1, 7, 5, 2, 4]
]))