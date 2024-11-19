print('#' * 10 + ' LIST SLICING ' + '10' * 10)
numbers = [1, 2, 3, 4, 5]
nums = numbers[1:4]
print(f'nums: {nums}')
print(f'numbers: {numbers}')
print()
print(numbers[:3])
print(numbers[2:])
print(numbers[1:5:3])
print(numbers[4:1:-2])
print(numbers[::])
print(numbers[::-1])
print(numbers[1:100])
print()
numbers[0:2] = ['a', 'b']
print(numbers)
numbers[0:2] = ['x', 'y', 'z']
print(numbers)
print('#' * 10 + ' LIST ITERATION ' + '10' * 10)
ip_list = ['192.168.0.1', '192.168.0.2', '10.0.0.1']
for ip in ip_list:
    print(f'Connecting to {ip} ...')

print('10.0.0.1' in ip_list)
print('192.100' in ip_list)
print('192' not in ip_list)


