# 🩺 Handwritten Text Extraction and Medical Recommendation System

> 🧠 Extracts handwritten medical prescriptions and provides personalized medicine recommendations.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-red.svg)](https://opencv.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.1.4-orange.svg)](https://pandas.pydata.org/)
[![Tesseract](https://img.shields.io/badge/Tesseract-OCR-green.svg)](https://github.com/tesseract-ocr/tesseract)
[![Flask](https://img.shields.io/badge/Flask-2.0+-purple.svg)](https://flask.palletsprojects.com/)
[![NumPy](https://img.shields.io/badge/NumPy-1.24+-blue.svg)](https://numpy.org/)

## 🩻 Project Overview

This project extracts text from handwritten medical prescriptions using image processing and OCR techniques. After extracting the text, it analyzes symptoms or conditions and provides medicine recommendations and care suggestions through an interactive web interface.

## 🛠️ Environment Setup

### 🔧 Prerequisites
Make sure you have the following installed:

- Python (≥ 3.8)
- Pip (Python package manager)
- Tesseract OCR engine

### 📂 Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate    # On Windows
```

### 📦 Install Required Libraries

```bash
pip install -r requirements.txt
```

### 📚 Required Libraries
```text
numpy==1.24.3
pandas==2.1.4
opencv-python==4.8.0
pytesseract==0.3.10
Pillow==10.0.0
matplotlib==3.7.2
torch==2.0.1
torchvision==0.15.2
flask==2.0.1
scikit-learn==1.3.0
```

### 👁️ OCR Setup (Tesseract)

- Ubuntu: `sudo apt install tesseract-ocr`
- Mac (Homebrew): `brew install tesseract`
- Windows: [Download Tesseract](https://github.com/tesseract-ocr/tesseract)

## 📂 Project Structure
```
A-Pharmacist-s-assistant/
│
├── app.py                 # Flask application with chat endpoints
├── symptoms.json          # Medicine database with symptoms mapping
├── requirements.txt       # Project dependencies
├── image-to-text.ipynb   # Jupyter notebook for OCR development
│
├── templates/
│   └── index.html        # Chat interface with medicine suggestions
│
└── README.md             # Project documentation
```

## 🚀 Running the Code

### 📝 Extracting Text from Images

```bash
python extract_text.py --input path/to/image
```

### 💊 Running the Recommendation Engine

```python
from recommendation_engine import recommend_treatment

extracted_text = "Patient complains of fever and headache."
recommendations = recommend_treatment(extracted_text)

for rec in recommendations:
    print(f"Symptom: {rec['Symptom']}")
    print(f"Medicine: {rec['Medicine']}")
    print(f"Advice: {rec['Advice']}\n")
```

### 🌐 Starting the Web Interface
```bash
python app.py
# Open browser and navigate to http://localhost:5000
```

## 📚 Example Workflow

1. **Input:** An image of a doctor's handwritten prescription.
2. **Process:** The image is processed, text is extracted, and analyzed.
3. **Output:** Medicines and care suggestions are printed.

## 🔧 Troubleshooting

- **Text not extracted:** Check the image quality and Tesseract installation.
- **Incorrect recommendations:** Verify the `MEDICINE_DB` in the recommendation engine.
- **OCR errors:** Ensure proper image preprocessing and Tesseract version.
- **Server issues:** Check Flask installation and port availability.

---

📝 Note: Always consult healthcare professionals before following any medical recommendations.
