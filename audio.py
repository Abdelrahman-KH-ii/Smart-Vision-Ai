from gtts import gTTS
import os

class AudioService:
    def __init__(self, language='en'):
        self.language = language

    def text_to_speech(self, text):
        try:
            tts = gTTS(text=text, lang=self.language, slow=False)
            tts.save("output.mp3")
            os.system("start output.mp3")  # لتشغيل الملف على Windows
        except Exception as e:
            return str(e)

def text_to_speech(text, language='en'):
    audio_service = AudioService(language)
    audio_service.text_to_speech(text)

# استخدام الكود
if __name__ == "__main__":
    text = "Hello, this is a test."
    text_to_speech(text, 'en')  # تحويل النص إلى كلام باللغة الإنجليزية
    print("Text-to-Speech is playing.")
