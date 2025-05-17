import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input
import numpy as np

model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

def get_image_embedding(image_path):
    try:
        img = image.load_img(image_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)
        embedding = model.predict(img_array)
        return embedding
    except Exception as e:
        print(f"Error processing image {image_path}: {str(e)}")
        return None

def get_batch_embeddings(image_paths):
    embeddings = []
    for path in image_paths:
        embedding = get_image_embedding(path)
        if embedding is not None:
            embeddings.append(embedding)
    return np.array(embeddings)

if __name__ == "__main__":
    image_path = "path_to_your_image.jpg"
    embedding = get_image_embedding(image_path)
    if embedding is not None:
        print(f"Image Embedding shape: {embedding.shape}")
    
    image_paths = ["path1.jpg", "path2.jpg", "path3.jpg"]
    batch_embeddings = get_batch_embeddings(image_paths)
    print(f"Batch Embeddings shape: {batch_embeddings.shape}")
