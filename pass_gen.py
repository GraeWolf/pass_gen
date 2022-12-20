# An app to randomly generate a password.

from random import randrange

# Ask user for length of desired password.
# ASk user for inclusion of special characters or not.
# Use lists to store characters, numbers and special characters.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
special = ['!', '@', '#', '$', '%', '^', '&', '*']
new_pass = []

password_length = 14
for x in range(password_length):
    list_choice = randrange(0, 10)

    if list_choice < 6:
        char_choice = randrange(0, len(letters))
        new_pass.append(letters[char_choice])
    elif list_choice >= 6 and list_choice < 8:
        char_choice = randrange(0, len(numbers))
        new_pass.append(numbers[char_choice])
    else:
        char_choice = randrange(0, len(special))
        new_pass.append(special[char_choice])

for character in new_pass:
    print(character, end = " ")


#combined = [letters, numbers, special]

#password_length = 8
#for x in range(password_length):
#    print("it works")

#test = randrange(0,len(letters))
#print(len(letters))
#print(test)
