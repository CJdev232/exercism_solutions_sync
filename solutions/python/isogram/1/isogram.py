def is_isogram(string):
    string_lower=string.lower()
    letters_only=''.join(char for char in string_lower if char.isalpha())
    return len(letters_only)==len(set(letters_only))