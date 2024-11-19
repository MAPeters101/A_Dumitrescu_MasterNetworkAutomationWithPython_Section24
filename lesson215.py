
# l1 = list()
# print(dir(l1))
# help(l1.append)

l1 = [1, 2.2, 'abc']
l1.append(5)
#l1.append(6, 7)
l1.append([6, 7])
print(l1)
print()

l1.extend(['x', 'y'])
print(l1)
print()

l1.extend('xyz')
print(l1)
print()

years = ['2020', '2022', '2023']
years.insert(1, '2021')
years.insert(len(years), '2024')
print(years)
years.insert(-1, '2025')
print(years)

print('='*80)

years.clear()
print(years)
print()
l2 = [10, 20, 30, 40]
print(l2)
x = l2.pop()
print(x)
print(l2)
print()

y = l2.pop(1)
#l2.pop(100)
print(y)
print(l2)
print()

l3 = [10, 20, 10, 40, 20]
l3.remove(10)
print(l3)
print()


l3 = [10, 20, 10, 40, 20, 10, 20, 20, 'z']
l3.remove(10)
print(l3)
while 20 in l3:
    l3.remove(20)
print(l3)
print()





