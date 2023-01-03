matrix = [
        [0, 675, 400, 166, 809, 720, 399, 233],
        [675, 0, 540, 687, 179, 348, 199, 401],
        [400, 540, 0, 107, 752, 521, 385, 280],
        [166, 687, 107, 0, 111, 540, 990, 361],
        [809, 179, 752, 111, 0, 206, 412, 576],
        [720, 348, 521, 540, 206, 0, 155, 621],
        [399, 199, 385, 990, 412, 155, 0, 100],
        [233, 401, 280, 361, 576, 621, 100, 0],
    ]



def minimum_cost_path(matrix: list[list[int]]) -> int:
    """
    Find the minimum cost traced by all possible paths from top left to bottom right in
    a given matrix

    >>> minimum_cost_path([[2, 1], [3, 1], [4, 2]])
    6

    >>> minimum_cost_path([[2, 1, 4], [2, 1, 3], [3, 2, 1]])
    7
    """

    # preprocessing the first row
    for i in range(1, len(matrix[0])):
        matrix[0][i] += matrix[0][i - 1]

    # preprocessing the first column
    for i in range(1, len(matrix)):
        matrix[i][0] += matrix[i - 1][0]

    # updating the path cost for current position
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1])

    return matrix[-1][-1]


print (minimum_cost_path(matrix))
if __name__ == "__main__":
    import doctest

    doctest.testmod()
