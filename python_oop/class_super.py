class Base(object):
    def __init__(self):
        print 'base init'

class Base1(object):
    def __init__(self):
        print 'base1 init'

class ChildA(Base):
    def __init__(self):
        print 'childA init'
        super(ChildA, self).__init__()

class ChildB(Base):
    def __init__(self):
        print 'childB init'
        super(ChildB, self).__init__()

class ChildC(ChildA, ChildB):
    pass

childC = ChildC()
print childC.__class__.__mro__


class Person(object):
    def __new__(cls, name, age):
        print '__new___ called'
        return super(Person, cls).__new__(cls, name, age)

    def __init__(self, name, age):
        print '__init__ called'
        self.name = name
        self.age = age

zliu = Person("zliu", 10)


class PositiveInteger(int):

    def __new__(cls, value):
        return super(PositiveInteger, cls).__new__(cls, abs(value))


i = PositiveInteger(-3)
print i
