def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    m, n = len(matrix), len(matrix) and len(matrix[0])

# Start searching from top, right element: Min element of row with max value
    r, c = 0, n-1
    while r < m and c >= 0:
        if target > matrix[r][c]:
            r += 1
        elif target < matrix[r][c]:
            c -= 1
        else: return True
    return False  