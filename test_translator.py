import unittest
from translatorE2F import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_english_to_french(self):
        result = english_to_french("Hello")
        self.assertEqual(result, "Pepitoooo")

        result = english_to_french("OpenAI is amazing!")
        self.assertNotEqual(result, "OpenAI est incroyable!")

    def test_french_to_english(self):
        result = french_to_english("Bonjour")
        self.assertEqual(result, "Hello")

        result = french_to_english("Je suis heureux")
        self.assertNotEqual(result, "I am happy")


if __name__ == '__main__':
    unittest.main()
