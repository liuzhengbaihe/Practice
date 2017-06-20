def quick_sort(seq):
    if seq == []:
        return []
    else:
        front_part = quick_sort([x for x in seq[1:] if x < seq[0]])
        end_part = quick_sort([x for x in seq[1:] if x > seq[0]])
    return front_part + [seq[0]] + end_part

if __name__ == '__main__':
    seq=[5,6,78,9,0,-1,2,3,-65,12]
    print quick_sort(seq)
