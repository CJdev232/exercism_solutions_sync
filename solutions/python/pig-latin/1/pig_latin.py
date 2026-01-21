def translate(text):
    piglatin = PigLatin(text)
    return piglatin.piglatinize()
class PigLatin:
    def __init__(self,text):
        self.text = text
        self.words = self.text.split()
    def _helper_vowel_start(self,word):
        new_word = word + 'ay'
        return new_word
    def _helper_consonant_start(self,word):
        vowels='aeiouAEIOU'
        first_vowel_index = -1
        for i,letter in enumerate(word):
            if letter in vowels:
                first_vowel_index = i
                break
        if first_vowel_index == -1:
            new_word = word + 'ay'
        else:
            new_word = word[first_vowel_index:] + word[:first_vowel_index] + 'ay'
        return new_word
        
    def _helper_consonant_and_qu_start(self,word):
        vowels='aeiouAEIOU'
        first_vowel_index = -1
        for i,letter in enumerate(word):
            if letter in vowels:
                first_vowel_index = i
                break
        first_qu_index = -1
        for i,letter in enumerate(word):
            if letter == 'q':
                if word[i+1] == 'u':
                    first_qu_index = i
                    break
        before_qu = word[:first_qu_index]
        from_qu = word[first_qu_index:first_qu_index+2]
        after_qu = word[first_qu_index+2:]
        return after_qu + before_qu + from_qu + 'ay'
        
    def _helper_consonant_and_y_start(self,word):
        vowels = 'aeiouAEIOU'
        y_index = -1
        for i,letter in enumerate(word):
            if letter == 'y':
                y_index = i
                break
        before_y = word[:y_index]
        after_y=word[y_index:]
        new_word = after_y + before_y + 'ay'
        return new_word
    def _helper_does_word_vowel_start(self,word):
        vowels='aeiouAEIOU'
        if word[0] in vowels:
            return True
        if word.lower().startswith('xr') or word.lower().startswith('yt'):
            return True
        if self._helper_does_word_consonant_and_y_start(word):
            return False
        return False
    def _helper_does_word_consonant_start(self,word):
        vowels = 'aeiouAEIOU'
        consonants_lower_list = [chr(ord('a') + n) for n in range(26) if chr(ord('a') + n) not in 'aeiou']
        consonants_upper_list = [chr(ord('A') + n) for n in range(26) if chr(ord('A') + n) not in 'AEIOU']
        consonants_list = consonants_lower_list + consonants_upper_list
        consonants = ''.join(consonants_list)
        if word[0] in vowels:
            return False
        if word.lower().startswith('xr') or word.lower().startswith('yt'):
            return False
        if word.lower().startswith('qu'):
            return False
        return True
        
    def _helper_does_word_consonant_and_qu_start(self,word):
        vowels = 'aeiouAEIOU'
        first_vowel_index = -1
        for i,letter in enumerate(word):
            if letter in vowels:
                first_vowel_index = i
                break
        first_qu_index = -1
        for i,letter in enumerate(word):
            if letter == 'q':
                if word[i+1] == 'u':
                    first_qu_index = i
                    break
        for n in range(first_qu_index):
            if word[n] in vowels:
                return False
        return 'qu' in word.lower()
    def _helper_does_word_consonant_and_y_start(self,word):
        vowels = 'aeiouAEIOU'
        y_index = -1
        for i,letter in enumerate(word):
            if letter == 'y':
                y_index = i
                break
        if y_index == -1:
            return False
        if y_index == 0:
            return False
        for i in range(y_index):
            if word[i] in vowels:
                return False
        return True
                
    def piglatinize(self):
        piglatin_list = []
        for word in self.words:
            if self._helper_does_word_consonant_and_qu_start(word):
                modified = self._helper_consonant_and_qu_start(word)
                piglatin_list.append(modified)
                
            elif self._helper_does_word_consonant_and_y_start(word):
                modified = self._helper_consonant_and_y_start(word)
                piglatin_list.append(modified)
                
            elif self._helper_does_word_consonant_start(word):
                modified = self._helper_consonant_start(word)
                piglatin_list.append(modified)
                 
            elif self._helper_does_word_vowel_start(word):
                modified = self._helper_vowel_start(word)
                piglatin_list.append(modified)
                
           
        return ' '.join(piglatin_list)
            
