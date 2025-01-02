import difflib
from googletrans import Translator

# Mapping of language names to their respective language codes
LANGUAGE_CODES = {
    "hindi": "hi",
    "french": "fr",
    "russian": "ru",
    "spanish": "es",
    "german": "de",
    "chinese": "zh-cn",
    "japanese": "ja",
    "italian": "it",
    "korean": "ko",
    "arabic": "ar",
    "portuguese": "pt",
    "english": "en"
}

def get_closest_language(input_language):
    """
    Find the closest match to the input language name using difflib.
    :param input_language: The language name provided by the user.
    :return: The closest language name.
    """
    closest_match = difflib.get_close_matches(input_language.lower(), LANGUAGE_CODES.keys(), n=1, cutoff=0.8)
    return closest_match[0] if closest_match else None

def translate_text(text, target_language="english"):
    """
    Translates the given text into the target language.
    :param text: The text to be translated.
    :param target_language: The name or code of the target language (default is English).
    :return: Translated text.
    """
    translator = Translator()
    try:
        closest_language = get_closest_language(target_language)
        if not closest_language:
            return "Sorry, I couldn't recognize the target language."
        
        target_language_code = LANGUAGE_CODES[closest_language]
        translation = translator.translate(text, dest=target_language_code)
        return translation.text
    except Exception as e:
        return f"Translation error: {e}"
