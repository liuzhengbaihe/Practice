import inspect

def simple_coroutine():
    print('coroutine started')
    x = yield
    print('coroutine received:', x)

my_coro = simple_coroutine()
print(inspect.getgeneratorstate(my_coro))
