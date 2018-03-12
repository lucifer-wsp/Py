import copy

a = [1, 2, 3, ['hello', 'world']]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
print(a)
print(b)
print(c)
print(d)

a[3].append('append')
b[2] = 'block'
c.append(4)
d.extend("Dp")
print(a)
print(b)
print(c)
print(d)
