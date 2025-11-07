import re 
def count_words(sentence):
    sentence = sentence.lower()
    words = re.split(r'[,_\s]+', sentence)
    words_count = {}
    for word in words:
        cleaned = word.strip("'\".:;!?&@$%^*()-")
        if cleaned:
            words_count[cleaned] = words_count.get(cleaned, 0) + 1
    return words_count
    
        
