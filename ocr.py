import os
import easyocr
from app.config import Config

class OCR:
    def __init__(self, language=Config.OCR_LANG):
        self.reader = easyocr.Reader([language])

    def extract_text(self, image_path):
        try:
            if not os.path.exists(image_path):
                return f" File not found: {image_path}"

            result = self.reader.readtext(image_path)
            extracted_text = " ".join([text[1] for text in result])
            return extracted_text if extracted_text else "⚠️ No text found."
        except Exception as e:
            return f" OCR Error: {str(e)}"

# ✅ Exported function used in run.py
def extract_text_from_image(image_path):
    ocr = OCR()
    return ocr.extract_text(image_path)
