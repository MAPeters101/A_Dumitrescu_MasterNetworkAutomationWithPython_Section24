
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


