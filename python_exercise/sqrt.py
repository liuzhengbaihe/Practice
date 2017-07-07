# caculate the square root value given a int number and double value precision limitation
def sqrt(n, rx=1, e=1e-10):
    n *= 1.0
    while True:
        if abs(n - rx*rx) < e:
            return rx
        else:
            return sqrt(n, (n/rx+rx)/2, e)
    
print sqrt(2)
