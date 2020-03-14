import unittest

from tourist_translations.translator import Translator

class TestNode(unittest.TestCase):
    def test_english_alphabet_lowercase(self):
        #Arrange
        translator = Translator("abcdefghijklmnopqrstuvwxyz")
        
        #Act
        translation = translator.translate("word")
        
        #Assert
        self.assertEqual(translation, "word")
    
    def test_english_alphabet_uppercase(self):
        #Arrange
        translator = Translator("abcdefghijklmnopqrstuvwxyz")
        
        #Act
        translation = translator.translate("Word")
        
        #Assert
        self.assertEqual(translation, "Word")
    
    def test_english_alphabet_with_punctuation(self):
        #Arrange
        translator = Translator("abcdefghijklmnopqrstuvwxyz")
        
        #Act
        translation = translator.translate("Word!")
        
        #Assert
        self.assertEqual(translation, "Word!")

    def test_multiple_words_lowercase(self):
        #Arrange
        translator = Translator("abcdefghijklmnopqrstuvwxyz")
        
        #Act
        translation = translator.translate("multiple_words")
        
        #Assert
        self.assertEqual(translation, "multiple words")
    
    def test_multiple_words_uppercase(self):
        #Arrange
        translator = Translator("abcdefghijklmnopqrstuvwxyz")
        
        #Act
        translation = translator.translate("Multiple_Words")
        
        #Assert
        self.assertEqual(translation, "Multiple Words")
    
    def test_other_alphabet_with_punctuation(self):
        #Arrange
        translator = Translator("qwertyuiopasdfghjklzxcvbnm")
        
        #Act
        translation = translator.translate("Bpke_kdc_epclc_jcijsc_mihyo?")
        
        #Assert
        self.assertEqual(translation, "What are these people doing?")
    
    def test_other_uppercase_alphabet_with_punctuation(self):
        #Arrange
        translator = Translator("qwertyuioPasdfghjklzxcvbnm")
        
        #Act
        translation = translator.translate("Bpke_kdc_epclc_jcijsc_mihyo?")
        
        #Assert
        self.assertEqual(translation, "What are these people doing?")