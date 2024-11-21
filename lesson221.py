
t1 = (1, 2, 1, 3, 4)

i = t1.index(2)
print(f'2 is at position {i}')

#i = t1.index('x')
x = 10
if x in t1:
    i = t1.index(x)
    print(f'{x} is at index {i}')
else:
    print(f'{x} is not in tuple')

n = t1.count(1)
print(f'{n=}')
n = t1.count(100)
print(f'{n=}')
print(100 in t1)
print()

print(len(t1))
print(sum(t1))
print(max(t1))
print(min(t1))

t2 = sorted(t1)
print(t2)
print(t1)
print(sorted(t1))
print(sorted(t1, reverse=True))



