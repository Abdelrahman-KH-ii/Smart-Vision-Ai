import os
from pymongo import MongoClient
from PIL import Image
import easyocr
import cv2
import numpy as np
import re
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client['ocr_results']
collection = db['images']

image_folder = r'C:\Users\bodaa\OneDrive\Desktop\data b\img'

reader = easyocr.Reader(['en'])

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    img_blurred = cv2.GaussianBlur(thresholded, (5, 5), 0)
    pil_img = Image.fromarray(img_blurred)
    return pil_img

def clean_text(text):
    cleaned_text = re.sub(r'\s+', ' ', text)
    cleaned_text = re.sub(r'[^\w\s]', '', cleaned_text)
    return cleaned_text

for image_name in os.listdir(image_folder):
    if image_name.endswith(".jpg") or image_name.endswith(".png"):
        image_path = os.path.join(image_folder, image_name)
        try:
            preprocessed_image = preprocess_image(image_path)
            result = reader.readtext(image_path)
            extracted_text = ' '.join([text[1] for text in result])
            extracted_text = clean_text(extracted_text)
            collection.insert_one({
                'image_name': image_name,
                'extracted_text': extracted_text,
                'processed_at': datetime.now()
            })
            print(f"Processed: {image_name}")
        except Exception as e:
            print(f"Error processing {image_name}: {str(e)}")

print("Data successfully added to MongoDB.")
