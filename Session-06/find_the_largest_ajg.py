list = [2,5,1,0,100,'done']

    # set the initial first value for the loops below
if len(list) > 0:
    largest =list[0]
    smallest = list[0]
    
for number in list:
    if number == 'done':
        break
    
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

print("Maximum is", largest)
print("Minimum is", smallest)