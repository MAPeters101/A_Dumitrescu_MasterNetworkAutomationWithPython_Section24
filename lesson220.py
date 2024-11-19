
my_tuple = (1.4, 10, 'abc', True, (30, 40), 'x')
print(my_tuple)
t1 = my_tuple + tuple('yz')
print(t1)
print()

t2 = (1, 2, 'a') * 3
print(t2)
print(my_tuple[0:2])
print(my_tuple[0:3])
print(my_tuple[2:])
print()
print(my_tuple[::])
print(my_tuple[::2])
print(my_tuple[-1:0:-1])
print()

movies = ('The Wizard of Oz', 'The Legend', 'Casablanca')
for movie in movies:
    print(f'We are watching {movie}.')

print()
print('The Legend' in movies)
print('The Legend' not in movies)




