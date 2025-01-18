# translation.py
from googletrans import Translator

# The translate_text function is sync, but we can make the bot async around it
def translate_text(text, src='en', dest='hi'):
    # Create a Translator object
    translator = Translator()

    # Translate the text
    translated = translator.translate(text, src=src, dest=dest)

    # Return translated text
    return translated.text
