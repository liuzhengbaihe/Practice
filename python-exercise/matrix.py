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

def quick_sort(seq):
    if seq == []:
        return []
    else:
        front_part = quick_sort([x for x in seq[1:] if x < seq[0]])
        end_part = quick_sort([x for x in seq[1:] if x > seq[0]])
    return front_part + [seq[0]] + end_part

if __name__ == '__main__':
    #matrix = [[1,2,8,9], [2,6,9,12], [4,7,10,13], [6,8,11,15]]
    #target_loc = get_target_from_matrix(matrix, 6)
    #print set_zero_for_target(target_loc)
    seq=[5,6,78,9,0,-1,2,3,-65,12]
    print quick_sort(seq)
else:
    print "I am being imported as a module"
