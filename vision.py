import os
from PIL import Image
import pytesseract
from .config import Config

# لو Tesseract مش متضاف للمسار تلقائيًا، فعل السطر ده:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def allowed_file(filename, allowed_extensions=Config.ALLOWED_EXTENSIONS):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def save_image(file, upload_folder=Config.UPLOAD_FOLDER):
    try:
        if file and allowed_file(file.filename):
            os.makedirs(upload_folder, exist_ok=True)
            filepath = os.path.join(upload_folder, file.filename)
            file.save(filepath)
            return filepath
        return None
    except Exception as e:
        print(f"❌ Error saving image: {str(e)}")
        return None

def resize_image(image_path, target_size=(224, 224)):
    try:
        if not os.path.exists(image_path):
            print(f"❌ Image path does not exist: {image_path}")
            return None
        image = Image.open(image_path)
        image = image.resize(target_size, Image.Resampling.LANCZOS)
        return image
    except Exception as e:
        print(f"❌ Error resizing image: {str(e)}")
        return None

def extract_text_from_image(image_path):
    try:
        if not os.path.exists(image_path):
            print(f"❌ Image not found: {image_path}")
            return "[OCR Error: File not found]"
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        print(f"❌ OCR error: {str(e)}")
        return "[OCR Error]"
