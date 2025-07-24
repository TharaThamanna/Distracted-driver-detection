✅ README.md

# 🚗 Distracted Driver Detection

This project is a **Flask-based web application** that uses a deep learning model to detect **distracted driving behaviors** from images. It predicts whether a driver is **safe** or performing actions like texting, talking on the phone, drinking, etc.

---

## 🖼️ Features
- Upload an image of a driver and detect distraction.
- Displays **prediction** and **confidence score**.
- **Image Preview** before prediction.
- **Dark/Light Mode Toggle**.
- **Warning Alerts**:
  - Visual alert (Toast message).
  - Audio alert when distracted driving is detected.
- Responsive and modern UI.

---

## 🛠️ Tech Stack
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Deep Learning**: TensorFlow / Keras
- **Model**: Pre-trained CNN model (`model.h5`)

---

## 📂 Project Structure
distracted-driver-app/
│
├── app.py # Flask backend
├── templates/
│ └── index.html # Frontend HTML
├── static/
│ ├── static.css # Custom CSS
│ ├── warning.mp3 # Warning sound
│ └── uploads/ # Uploaded images
├── model/
│ └── model.h5 # Trained CNN model
└── README.md # Project documentation


## ⚡ Installation & Setup
### 1️⃣ Clone the repository
git clone https://github.com/TharaThamanna/Distracted-driver-detection.git
cd Distracted-driver-detection
2️⃣ Create Virtual Environment

python -m venv venv
Activate:

Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

If requirements.txt is missing, use:
pip install flask tensorflow numpy pillow werkzeug

4️⃣ Run the App
python app.py
Open in browser: http://127.0.0.1:5000

🔍 How It Works
Upload an image of a driver.

The image is preprocessed and passed to the trained CNN model.

The model predicts the driver's activity:

✅ Safe Driving

📱 Texting / Talking on phone

🍹 Drinking

💄 Hair & Makeup

🎵 Operating Radio

And more...

If distracted, a warning alert + sound will trigger.

✅ Future Enhancements
Real-time webcam detection.

Integration with vehicle systems.

Deploy on Render / Railway / Heroku for live demo.

👩‍💻 Author
Thara Thamanna
GitHub Profile

⚠️ Note
The model file (model/model.h5) is large (>50MB).
Use Git LFS for handling large files:

git lfs install
git lfs track "model/model.h5"
