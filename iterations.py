# 2 break & continue example
while True:
    line = input('Enter a phrase: ')
    if line.startswith('#'):
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

# # 3 definite loop using for
# fruits = ['apple', 'banana', 'cherry']

# for fruit in fruits:
#     print(fruit)

#     if fruit == 'banana':
#         break