largest = None
smallest = None

list = [2,5,1,0,100,'done']

for number in list:
    if number == 'done':
        print("Maximum is", largest)
        print("Minimum is", smallest)
        exit()

    # set the initial first value for the loops below
    if largest is None:
        largest = number
    if smallest is None:
        smallest = number

    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

