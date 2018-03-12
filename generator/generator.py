class Bank():
    crisis = False
    def create_atm(self):
        while not self.crisis:
            yield "$100"

b = Bank()
atm = b.create_atm()
print(next(atm))

try:
    print('set crisis = True.')
    b.crisis = True
    print(next(atm))

    print(next(b.create_atm()))
except Exception as e:
    print(e)

try:
    print('set crisis = False.')
    b.crisis = False
    print(next(b.create_atm()))
except Exception as e:
    print(e)

print('new Bank .')
b = Bank()
print(next(b.create_atm()))


print('-----------------lambda----------------')
a=[1,2,3]
print(a)
print('map')
for i in map(lambda x: x+1, a):
    print(i)
print('filter')
for i in filter(lambda x: x%2, a):
    print(i)