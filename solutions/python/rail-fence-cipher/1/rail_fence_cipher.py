def encode(message, rails):
    if rails == 1 or rails >= len(message):
        return message  # Edge cases
    
    # Create a list for each rail
    fence = [[] for _ in range(rails)]
    rail = 0 
    direction = 1
    for char in message:
        fence[rail].append(char)
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1
    return ''.join([''.join(rail) for rail in fence])
    
        

def decode(encoded_message, rails):
    fence = [[None for _ in range(len(encoded_message))] for _ in range(rails)]
    rail = 0
    direction = 1
    for col in range(len(encoded_message)):
        fence[rail][col] = '*'
        rail += direction
        if rail == 0 or rail == rails-1:
            direction *= -1
    index = 0
    for row in range(rails):
        for col in range(len(encoded_message)):
            if fence[row][col] == '*':
                fence[row][col] =encoded_message[index]
                index += 1
    result = []
    rail = 0
    direction = 1
    for col in range(len(encoded_message)):
        result.append(fence[rail][col])
        rail += direction
        if rail == 0 or rail == rails-1:
            direction *= -1
    return ''.join(result)
