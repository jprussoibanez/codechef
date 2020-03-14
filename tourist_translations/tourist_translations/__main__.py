from tourist_translations.translator import Translator

def main(args = None):
    try:
        number_of_translations, alphabet = input().split()
        translator = Translator(alphabet)
        for _ in range(int(number_of_translations)):
            phrase = input()
            translated_phrase = translator.translate(phrase)    
            print(translated_phrase)
    except EOFError:
        pass

if __name__ == "__main__":
    main()