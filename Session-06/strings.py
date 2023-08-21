fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(f"Index: {index}, Letter: {letter}")

    index = index + 1 

for letter in fruit:
    print(f"Letter: {letter}")


# Create a string and assign it to sentence variable
sentence = "You have a choice of: kiwi, apple, orange, banana, pear or strawberry"
# sentence_slice = sentence[0:10]
# sentence_slice = sentence[11:17]
# sentence_slice = sentence[20:]

find_character = sentence.find(":")
sentence_slice = sentence[find_character + 1:]


print(sentence_slice)