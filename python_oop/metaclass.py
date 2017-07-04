#def upper_attr(cls_name, parent_clses, cls_attrs):
#    attrs = ((k,v) for k, v in cls_attrs.items() if not k.startswith('__'))
#    print attrs
#    uppercase_attr =  dict((k.upper(), v) for k, v in attrs)
#    print uppercase_attr
#    return type(cls_name, parent_clses, uppercase_attr)
#
#
#__metaclass__ = upper_attr

class UpperAttr(type):
    def __new__(cls, name, bases, cls_attrs):
        print name
        print bases
        print cls_attrs
        attrs = ((k, v) for k, v in cls_attrs.items() if not k.startswith('__'))
        uppercase_attr = dict((k.upper(), v) for k,v in attrs)
        return super(UpperAttr, cls).__new__(cls, name, bases, uppercase_attr)

class Foo():

    __metaclass__ = UpperAttr

    def __init__(self, name, age):
        self.name = name
        self.age = age

#foo = Foo('zliu', 27)
#print foo.__dict__

# metaclass using __call__
class MyType(type):

    def __new__(cls, *args, **kwargs):
        print '__new__ run in MyType'
        return super(MyType, cls).__new__(cls, *args, **kwargs)

    def __init__(self, what, bases=None, dict=None):
        print '__init__ run in MyType'
        super(MyType, self).__init__(what, bases, dict)

    def __call__(self, *args, **kwargs):
        print '__call__ run in MyType'
        obj = self.__new__(self, *args, **kwargs)

        obj.__init__()

class Foo(object):

    __metaclass__ = MyType

    def __new__(cls, *args, **kwargs):
        print '__new__ run in Foo'
        return super(Foo, cls).__new__(cls, *args, **kwargs)

    def __init__(self, name):
        print '__init__ run in Foo'
        self.name = name


###phase 1: create Foo 
###phase 2: create obj
obj = Foo('zliu')
