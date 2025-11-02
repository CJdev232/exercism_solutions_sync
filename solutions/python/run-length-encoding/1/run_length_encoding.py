def decode(string):
    decoded = ''
    i = 0
    while i < len(string):
        cur_digits = ''
        while i <len(string) and string[i].isdigit():
            cur_digits += string[i]
            i += 1
        count = int(cur_digits) if cur_digits else 1
        if i < len(string):
            decoded += count*string[i]
            i +=1
    return decoded
                
            
            


def encode(string):
    if not string:
        return  ''
    encoded = ''
    count = 1
    for i in range(1,len(string)):
        if string[i] == string[i-1]:
            count += 1
        else:
            if count > 1:
                encoded += str(count) +string[i-1]
            else:
                encoded += string[i-1]
            count = 1
    if count > 1:
        encoded += str(count) +string[-1]
    else:
        encoded += string[-1]
    return encoded
        
