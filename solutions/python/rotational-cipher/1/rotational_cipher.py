def rotate(text, key):
    result = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                cipher = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            else:
                cipher = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            result += cipher
        else:
            result += char
    return result
                
        
