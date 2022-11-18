import unittest
from ..translator import english_to_french,french_to_english

class TestTranslationMethods(unittest.TestCase):
    def test1(self):
        
        self.assertEqual(english_to_french(''), '')        
        self.assertEqual(french_to_english(''), '')
        
        self.assertEqual(french_to_english('Bonjour'), 'Hello')        
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        
        self.assertEqual(french_to_english('Bonjour'), 'Hello')        
        self.assertEqual(english_to_french('Hello'), 'Bonjour')


#unittest.main()

