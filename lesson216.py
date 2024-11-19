
names = ['john', 'dan', 'tom', 'john', 'bill']
#i = names.index('dany')
i = names.index('dan')
print(f'dany is at index {i}.')
i = names.index('dan', 1, 3)
print(f'dany is at index {i}.')
print(names.index('john'))
print(names.index('john', 1))
print()

letters = list('dfsfadsgasgfdgasfgghjfhjggagfhfghj')
n = letters.count('a')
print(n)

n = letters.count('p')
print(n)
print('p' in letters)
print()

print('f' in letters)
print()

l1 = [1, 3, 'abc', 10, 'x']
print(f'{l1=}')
l1.reverse()
print(f'{l1=}')
print()

ages = [10, 8, 23, 40, 35]
print(f'{ages=}')
la = sorted(ages)
print(f'{la=}')
print(f'{ages=}')

ages = [10, 8, 23, 40, 35]
n = ages.sort()
print(f'{n=}')
print(f'{ages=}')
print()


ages = [10, 8, 23, 40, 35]
print(f'{ages=}')
la = sorted(ages, reverse=True)
print(f'{la=}')
print(f'{ages=}')

ages = [10, 8, 23, 40, 35]
n = ages.sort(reverse=True)
print(f'{n=}')
print(f'{ages=}')
print()

print('='*80)

l1 = [1, 3, '4']
#l1.sort()
print(l1)
print()

l2 = [9, 10, 5, 100, 46]
print(f'{max(l2)=}')
print(f'{min(l2)=}')
print(f'{sum(l2)=}')



