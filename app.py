from flask import Flask, render_template, request, redirect
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
model = load_model('model/model.h5')  # Load your trained model
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class_names = [
    "Safe Driving",         # c0
    "Texting - Right",      # c1
    "Talking on Phone - Right",  # c2
    "Texting - Left",       # c3
    "Talking on Phone - Left",   # c4
    "Operating the Radio",  # c5
    "Drinking",             # c6
    "Reaching Behind",      # c7
    "Hair and Makeup",      # c8
    "Talking to Passenger"  # c9
]
  # Update based on your model

@app.route('/')
def index():
    return render_template('index.html', prediction=None, uploaded_image=None)

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
        
    if file:
        filename = secure_filename(file.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(image_path)

        # Preprocess image
        img = image.load_img(image_path, target_size=(128, 128))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        prediction = model.predict(img_array)
        predicted_index = np.argmax(prediction)
        confidence = round(float(np.max(prediction)) * 100, 2)
        predicted_class = class_names[predicted_index]

        # Send the image path along with prediction data back to the template
        return render_template("index.html",
                               prediction=predicted_class,
                               confidence=confidence,
                               uploaded_image=image_path)

if __name__ == '__main__':
    app.run(debug=True)
