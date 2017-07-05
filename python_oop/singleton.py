class Singleton(object):
    '''singleton class limits instance is only one'''
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

obj1 = Singleton()
print Singleton.instance
obj2 = Singleton()
obj1.value = "test"
print obj2.value
print obj1 is obj2

#using decorator
def singleton(cls):
    _instances = {}
    def wrapper(args, **kwargs)
