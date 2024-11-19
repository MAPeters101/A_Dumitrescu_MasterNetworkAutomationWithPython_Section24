
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

print()








