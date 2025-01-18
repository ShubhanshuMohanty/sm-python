from googletrans import Translator

# Translator object banayein
translator = Translator()

# English text ko Hindi me translate karein
text = "Hello, how are you?"
translated_text = translator.translate(text, src='en', dest='hi')

# Translation print karein
print(f"Original text: {text}")
print(f"Translated text: {translated_text.text}")
