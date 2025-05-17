import os
from PIL import Image

def allowed_file(filename, allowed_extensions={'png', 'jpg', 'jpeg'}):
    """

    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def save_image(file, upload_folder='uploads/'):
    """

    """
    if file and allowed_file(file.filename):
        filepath = os.path.join(upload_folder, file.filename)
        file.save(filepath)
        return filepath
    return None

def resize_image(image_path, target_size=(224, 224)):
    """.
    """
    image = Image.open(image_path)
    image = image.resize(target_size)
    return image
