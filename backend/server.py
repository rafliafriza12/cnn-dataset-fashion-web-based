from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
from flask_cors import CORS
from PIL import Image

app = Flask(__name__)
CORS(app)
model = load_model('AdvancedCNN_best.h5')

IMG_SIZE = (28, 28)

# Label Fashion MNIST
fashion_labels = [
    "T-shirt/top", "Trouser", "Dress"
]

@app.route('/', methods=['GET'])
def testing():
    return jsonify({
        'status': 200,
        'message': "Testing Flask OK",
    }), 200


@app.route('/predict', methods=['POST'])
def predict():
    # print(request.files)
    if 'image' not in request.files:
        return jsonify({'message': 'No image uploaded', 'status': 400}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'message': 'No selected file', 'status': 400}), 400

    try:
        # Ubah gambar ke grayscale dan resize ke 28x28
        image = Image.open(file).convert('L')
        image = image.resize(IMG_SIZE)
        image_array = img_to_array(image)
        image_array = image_array / 255.0
        image_array = np.expand_dims(image_array, axis=0)  # (1, 28, 28, 1)

        prediction = model.predict(image_array)[0]  # Ambil array hasil prediksi
        predicted_index = int(np.argmax(prediction))
        predicted_label = fashion_labels[predicted_index]
        confidence = float(prediction[predicted_index])  # Confidence level

        return jsonify({
            'status': 200,
            'data': {
                'class_index': predicted_index,
                'class_label': predicted_label,
                'confidence': round(confidence, 4),
                'full_prediction': prediction.tolist(),
            },
            'message': 'success',
        })
    except Exception as e:
        return jsonify({'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
