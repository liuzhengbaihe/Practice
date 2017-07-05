# classic class and new-style class, also inheritance 
# new-style class use C3 to brower parent classes
class A(object):
    def bar(self):
        print "A.bar"

class B(A):
    def bar(self):
        print "B.bar"

class C(B):
    def bar(self):
        print "C.bar"

class D(A):
    def bar(self):
        print "D.bar"

class E(D):
    def bar(self):
        print "E.bar"

class F(C,E):
    pass

f = F()
print F.__mro__
print f.__class__

class Foo(object):
    def m1(self):
        print "general method"

    @staticmethod
    def m2():
        print "static method"

    @classmethod
    def m3(cls):
        print "class method"


foo = Foo()
foo.m1()
foo.m2()
Foo.m2()
foo.m3()
Foo.m3()

# three properties used in new class
class Foo1(object):
 
    def get_bar(self):
        print 'wupeiqi'
 
    def set_bar(self, value): 
        print ('set value' + value)
 
    def del_bar(self):
        print 'delete wupeiqi'
 
    BAR = property(get_bar, set_bar, del_bar, 'description...')
    HAH = property(get_bar)
 
obj = Foo1()
print obj.BAR
print Foo1.__dict__
obj.BAR = "test"
del obj.BAR



#points between classic class and new style class
#new-style class supports more property, method.property_setter, method.property_getter
#new-style brower parent classes by breadth-first while classic class is by depth-first
#new-style supports super(class_name, self)
#declearation is different, new-style class inhert Object first, while classic class inhert type.

