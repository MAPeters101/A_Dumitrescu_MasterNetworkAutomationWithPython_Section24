
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
print('='*80)

nums = [1, 2, 3, 4, 5, 6, 7, 0, 1, 2]

# for n in nums:
#     if n < 5:
#         nums.remove(n)
# print(nums)

new_list = list()
for n in nums:
    if n >= 5:
        new_list.append(n)
print(new_list)


my_list = [n for n in nums if n >= 5]
print(my_list)




