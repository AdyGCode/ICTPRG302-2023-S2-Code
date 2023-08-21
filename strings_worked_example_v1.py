# Create a string and assign it to sentence variable
sentence = "You have a choice of kiwi ,apple ,pear ,orange, banana or strawberry"

# Choose a character to search for
letter_search = "a"

# Split the sentence into words
words = sentence.split()

# Iterate through each word
for word in words:
    # Take out the comma if it exists
    word = word.strip(',')

    # If the word is found
    if word == 'banana':
        # Find the start of the word within the sentence
        word_position = sentence.find(word)

        # Lets count the letters
        letter_count =  0

        # Loop through each character in the word and print all characters except the excluded one
        for letter in word:
            if letter == letter_search:
                letter_count += 1
        
        print(f"We found {letter_count} letters in your search word {word}")
        exit()
    # Lets remind ourselves we like oranges
    elif word.startswith("or"):
        print(f"Hang on, I realised I like {word}'s")
    # Remove the stuff we dont like
    elif word == "pear":
        position = sentence.find(word)
        print(sentence.replace(sentence[position-2:position+len(word)], ''))

# Challenge - 
# How would change this so the user can decide the letter to search for
# How would change this so the user can decide the fruit they dont like
# How would change this so the user can decide the fruit they do like
