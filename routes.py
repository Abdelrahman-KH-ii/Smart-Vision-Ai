from flask import Flask, request, jsonify
from ocr import ocr_extract
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/ocr', methods=['POST'])
def ocr_route():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        extracted_text = ocr_extract(filepath)
        return jsonify({'extracted_text': extracted_text}), 200
    else:
        return jsonify({'error': 'Invalid file format'}), 400

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

if __name__ == "__main__":
    app.run(debug=True)
