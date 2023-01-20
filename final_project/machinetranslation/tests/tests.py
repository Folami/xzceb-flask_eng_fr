import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(None), None) # test when null is given as input the output is null.
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  # test when ‘Hello’ is given as input the output is ‘Bonjour’.
        self.assertNotEqual(english_to_french('Miss'), 'Monsieur')  # test when ‘Mr’ is given as input the output is ‘Monsieur’.
        

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(None), None) # test when null is given as input the output is null.
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when ‘Bonjour’ is given as input the output is ‘Hello’.
        self.assertNotEqual(french_to_english('Mademoiselle'), 'Mr') # test when ‘Mademoiselle’ is given as input the output is ‘Miss’.
        
unittest.main()
