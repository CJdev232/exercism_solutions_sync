import re

def abbreviate(words):
    first_letter_upper = []
    for word in re.split(r'[ -]', words):
        for char in word:  # Iterate through characters until we find a letter
            if char.isalpha():
                first_letter_upper.append(char.upper())
                break  # Stop after finding the first letter
    return ''.join(first_letter_upper)