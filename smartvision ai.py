from app.ml_models.classifier import train_classifier
from app.ocr import extract_text_from_image
from app.translate import translate_text
import os
from PIL import Image
from pymongo import MongoClient

# دالة resize_image معدلة تدعم نسخ PIL القديمة والجديدة
def resize_image(image_path, target_size=(224, 224)):
    image = Image.open(image_path)
    try:
        resample_method = Image.Resampling.LANCZOS
    except AttributeError:
        resample_method = Image.ANTIALIAS  # للنسخ القديمة
    resized_image = image.resize(target_size, resample=resample_method)
    return resized_image

# اتصال MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["smartvision_db"]
collection = db["ocr_results"]

img_dir = r"C:\Users\bodaa\OneDrive\Desktop\data b\img"
output_dir = "samples"

# إنشاء مجلد الحفظ لو مش موجود
os.makedirs(output_dir, exist_ok=True)

# لو عايز تلغي تدريب الموديل علشان مفيش تصنيفات
# علقه أو شيله
# if os.path.exists(img_dir):
#     train_classifier(img_dir)

# معالجة الصور وحفظ النتائج
for filename in os.listdir(img_dir):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        image_path = os.path.join(img_dir, filename)
        print(f"\n🔍 Processing {filename}...")

        # OCR
        try:
            text = extract_text_from_image(image_path)
            print("📝 Text:", text)
        except Exception as e:
            text = f"[OCR Error: {str(e)}]"
            print("❌ OCR Error:", e)

        # ترجمة النص (بدون target_lang)
        try:
            translated = translate_text(text)
            print("🌐 Translated:", translated)
        except Exception as e:
            translated = f"[Translation Error: {str(e)}]"
            print("❌ Translation Error:", e)

        # Resize الصورة
        try:
            resized = resize_image(image_path, target_size=(224, 224))
            resized_filename = f"resized_{filename}"
            resized_path = os.path.join(output_dir, resized_filename)
            if resized:
                resized.save(resized_path)
                print(f"✅ Saved resized image: {resized_path}")
            else:
                print(f"❌ Failed to resize image: {filename}")
        except Exception as e:
            resized_filename = None
            print("❌ Resize Error:", e)

        # إدخال البيانات في MongoDB
        doc = {
            "filename": filename,
            "text": text,
            "translated": translated,
            "image_path": resized_filename
        }
        collection.insert_one(doc)
        print("📦 Result saved to MongoDB")

print("\n✅ All results stored in MongoDB successfully.")
