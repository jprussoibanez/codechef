class Translator:
    english_alphabet = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self, alphabet):
        self.mapping_alphabet = dict(zip(Translator.english_alphabet, alphabet.lower()))
        self.mapping_alphabet['_'] = " "

    def translate(self, phrase):
        translated_phrase = ''
        for letter in phrase:
            if letter.lower() in self.mapping_alphabet:
                translated_letter = self.mapping_alphabet[letter.lower()]
            else:
                translated_letter = letter
            
            if letter.isupper():
                translated_letter = translated_letter.upper()
            
            translated_phrase += translated_letter
        
        return translated_phrase