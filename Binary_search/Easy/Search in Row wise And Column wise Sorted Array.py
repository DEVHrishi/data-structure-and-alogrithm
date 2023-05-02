def search_matrix(matrix, target):
    """
    Searches for an element in a row-wise and column-wise sorted matrix.
    Returns the position of the element if found, otherwise returns None.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    row = 0
    col = cols - 1
    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return (row, col)
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    return None
