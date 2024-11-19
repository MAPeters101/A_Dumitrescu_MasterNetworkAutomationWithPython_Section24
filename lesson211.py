
l1 = [1, 2,5, 'Python', True, ['abc', 'xyz'], (10, 20, 30)]
print(len(l1))
l2 = []
l3 = list()

print(l1[0])
x = l1[-1]
print(x)
#print(l1[10])
print()

s1 = 'abc'
#s1[0] = 'X'

l4 = list('abcd')
print(l4)
print(hex(id(l4)))
l4[0] = 'X'
print(l4)
print(hex(id(l4)))
l4.append(100)
print(l4)
print(hex(id(l4)))

