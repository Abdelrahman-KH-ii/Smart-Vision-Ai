from googletrans import Translator

class TranslatorService:
    def __init__(self, lang='en'):
        self.translator = Translator()
        self.lang = lang

    def translate_text(self, text):
        try:
            translated = self.translator.translate(text, dest=self.lang)
            return translated.text
        except Exception as e:
            return str(e)

def translate_text(text, dest_lang='en'):
    translator = TranslatorService(lang=dest_lang)
    return translator.translate_text(text)


if __name__ == "__main__":
    text = "Hello, how are you?"
    translated_text = translate_text(text, 'fr')  # ترجمة النص إلى الفرنسية
    print(f"Translated Text: {translated_text}")
