def decorator_passing_arbitary_args(func):
    def wrapper(*args, **kwargs):
        print "Start!"
        print args
        print kwargs
        func(*args, **kwargs)
        print "Done!"
    return wrapper

def func(a, b, c="test"):
    print a, b,c

func = decorator_passing_arbitary_args(func)
func(1,2,c="haha")
