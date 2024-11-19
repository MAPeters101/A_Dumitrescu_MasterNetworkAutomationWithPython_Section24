
l1 = [1, 2, 3]
l2 = l1
l2[0] = 'XX'
l2.append(10)
print(f'{hex(id(l1))=} {l1=}')
print(f'{hex(id(l2))=} {l2=}')
print()

l2.remove(2)
print(f'{hex(id(l1))=} {l1=}')
print(f'{hex(id(l2))=} {l2=}')
print()


l3 = l1.copy()
print(f'{hex(id(l1))=} {l1=}')
print(f'{hex(id(l3))=} {l3=}')
print()

l3.append('abc')
print(f'{hex(id(l1))=} {l1=}')
print(f'{hex(id(l3))=} {l3=}')
print()






