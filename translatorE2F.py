from deep_translator import MyMemoryTranslator


def english_to_french(text):
    translator = MyMemoryTranslator(source='en', target='fr')
    translated_text = translator.translate(text)
    return translated_text


def french_to_english(text):
    translator = MyMemoryTranslator(source='fr', target='en')
    translated_text = translator.translate(text)
    return translated_text
