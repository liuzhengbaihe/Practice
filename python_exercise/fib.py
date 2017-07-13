import time

N = 40

# time complexity is o(n**2)
def fib1(n):
    if n < 2:
        return n
    else:
        return fib1(n-1) + fib1(n-2)

start = time.time()
print "fibnacci:", fib1(N)
print "time spent:", time.time() - start

# time complexity is o(n)
def fib(n, cache={}):
    if n < 2:
        return n
    elif cache.get(n):
        return cache[n]
    else:
        result = fib(n-1, cache) + fib(n-2, cache)
        cache[n] = result
        return result

start = time.time()
print fib(N)
print "time spent:", time.time() - start

# space complexity is o(1), time complexity is o(n)
def fib3(n):
    if n < 2:
        return n
    a, b = 1, 1
    result = 0
    for num in range(3, n+1):
        result = a + b
        a, b = b, result
    return result

start = time.time()
print fib3(N)
print "time spent:", time.time() - start
