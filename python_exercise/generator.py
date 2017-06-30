def myGenerator():
    list = range(3)
    for x in mylist:
        yield x*x

generator = myGenerator()

for i in myGenerator():
    print i
