import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
    UPLOAD_FOLDER = 'uploads/'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    OCR_LANG = 'en'
    OCR_TIMEOUT = 10
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/')
    API_KEY = os.environ.get('API_KEY', 'your_api_key')
