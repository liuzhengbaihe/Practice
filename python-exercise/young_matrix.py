ROW = 4
COL = 4

def get_target_from_matrix(matrix, target):
    x = 0
    y = COL - 1
    result = []
    while(x < ROW and y >= 0):
        if matrix[x][y] > target:
            y = y - 1
        elif matrix[x][y] < target:
            x = x + 1
        else:
            result.append((x,y))
            y = y - 1
    return result

def set_zero_for_target(target_loc):
    for x, y in target_loc:
        matrix[x] = [0 for i in xrange(COL)]
        for i in xrange(ROW):
            matrix[i][y] = 0
    return matrix

if __name__ == '__main__':
    matrix = [[1,2,8,9], [2,6,9,12], [4,7,10,13], [6,8,11,15]]
    target_loc = get_target_from_matrix(matrix, 6)
    print set_zero_for_target(target_loc)
else:
    print "I am being imported as a module"
