
l1 = [3, 4]
print(hex(id(l1)), l1)
l1 = l1 + [5, 6]
print(hex(id(l1)), l1)
l1 += [7, 8]
print(hex(id(l1)), l1)
l1.extend([11, 12])
print(hex(id(l1)), l1)
l1.append(['a', 'b'])
print(hex(id(l1)), l1)
l1.extend(['x', 'y'])
print(hex(id(l1)), l1)
l1.append(20)
print(hex(id(l1)), l1)
l1.extend([30])
print(hex(id(l1)), l1)
# l1.extend(40)
# print(hex(id(l1)), l1)
print()
l2 = list('abc')
l3 = l2 * 3
print(l3)


