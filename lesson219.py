
t1 = tuple()
t2 = ()
print(type(t1), t1)
print(type(t2), t2)

t3 = (1, 3.4, 'python', True)
print(type(t3), t3)

t4 = (10)
print(type(t4), t4)
print()

t4 = (10, )
print(type(t4), t4)
print()

t4 = 10,
print(type(t4), t4)
print()

t5 = 6.9, True, 10, 'abc'
print(type(t5), t5)
print()

t6 = tuple([1, 2, 3, 4])
print(type(t6), t6)
t7 = tuple('hello')
print(type(t7), t7)
print()

l1 = list(t5)
print(l1)
print()

print(t5[0])
print(t5[-1])
print()

#t5[0] = 'X'


