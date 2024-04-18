def formingMagicSquare(s):
    result = 1e9
    magics = [[8, 3, 4, 1, 5, 9, 6, 7, 2],
    [6, 1, 8, 7, 5, 3, 2, 9, 4],
    [2, 7, 6, 9, 5, 1, 4, 3, 8],
    [2, 9, 4, 7, 5, 3, 6, 1, 8],
    [4, 3, 8, 9, 5, 1, 2, 7, 6],
    [8, 1, 6, 3, 5, 7, 4, 9, 2],
    [6, 7, 2, 1, 5, 9, 8, 3, 4],
    [4, 9, 2, 3, 5, 7, 8, 1, 6]]
    
    arr_s = [s[i][j] for i in range(3) for j in range(3)]
    
    for magic in magics :
        total = 0
        for a, b in zip(magic, arr_s) :
            total += abs(a - b)
        result = min(result, total)
            
    return result
    
s = [[5,3,4], [1,5,8], [6,4,2]]
formingMagicSquare(s)
