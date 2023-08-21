while True:
    line= input("Enter a phrase: ")
    # identify if starts with...
    if line.startswith('#'):
        continue
    if line=="done":
        break
    print(line)
    
print("!Done!")
