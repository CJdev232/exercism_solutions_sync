def transform(legacy_data):
    data = {}
    for point,letter_list in legacy_data.items():
        for letter in letter_list:
            data[letter.lower()] = point
    return data
            
