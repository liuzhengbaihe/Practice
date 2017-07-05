#def myGenerator():
#    mylist = range(3)
#    for x in mylist:
#        yield x*x
#
#generator = myGenerator()
#
#for i in myGenerator():
#    print i


class Bank():
    crisis = False
    def create_atm(self):
        while not self.crisis:
            yield "$100"

hsbc = Bank()
corner_street_atm = hsbc.create_atm()
print (corner_street_atm.next())
hsbc.crisis = True
print(corner_street_atm.next())
wall_street_atm = hsbc.create_atm()
print(wall_street_atm.next())
hsbc.crisis = False
print(wall_street_atm.next())
