string = input("Enter a string value: ")

# Prints the length of the string
print(len(string))

# Prints the first letter of the string
first_letter = string[0]
print(first_letter)

# Prints the last letter of the string
last_letter = string[-1]
print(last_letter)

# Deletes the third character in the string and then prints it.
delete_character_in_string = string
print(delete_character_in_string[:3] + delete_character_in_string[4:])

# Prints the string in all upper case
print(string.upper())

# Prints the string in Title case
print(string.title())

# Checks is a string has only alphabetic characters
print(string.isalpha())

# Replaces empty space in a string with a comma.
string_with_commas = string.replace(' ',',')
print(string_with_commas)

# Prints the string in all lower case
print(string.lower())
