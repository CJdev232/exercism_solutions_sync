def extract_7bits(number):
    return number & 0x7F
def encode(numbers):
    bytes_for_numbers = []
    for number in numbers:
        bytes_for_this = []
        if number == 0:
            bytes_for_this = [0]
        else:
            while (number > 0):
                seven_bits=extract_7bits(number)
                bytes_for_this.append(seven_bits)
                number >>= 7
        reversed_bytes_for_this=bytes_for_this[::-1]
        for i in range(len(reversed_bytes_for_this) - 1):
            reversed_bytes_for_this[i] |= 0x80

        bytes_for_numbers+=reversed_bytes_for_this
    return bytes_for_numbers
    
            
        
        
    
    


def decode(bytes_):
    result = []
    current_number = 0
    for byte in bytes_:
        data_bits = byte & 0x7F
        current_number = (current_number <<7) | data_bits
        if byte & 0x80 ==0:
            result.append(current_number)
            current_number = 0
    if bytes_ and bytes_[-1] & 0x80 != 0:
        raise ValueError('incomplete sequence')
    return result
    
