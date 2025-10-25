def is_pangram(sentence):
    all_letters=set(chr(n) for n in range(ord('a'),ord('a')+26))
    sentence_refined=sentence.strip().lower()
    sentence_letters=set(letter for letter in sentence_refined if letter.isalpha())
    return sentence_letters==all_letters
