# 🩺 Handwritten Text Extraction and Medical Recommendation System

> 🧠 Extracts handwritten medical prescriptions and provides personalized medicine recommendations.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-red.svg)](https://opencv.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.1.4-orange.svg)](https://pandas.pydata.org/)
[![Tesseract](https://img.shields.io/badge/Tesseract-OCR-green.svg)](https://github.com/tesseract-ocr/tesseract)

## 🩻 Project Overview

This project extracts text from handwritten medical prescriptions using image processing and OCR techniques. After extracting the text, it analyzes symptoms or conditions and provides medicine recommendations and care suggestions.

## 🛠️ Environment Setup

### 🔧 Prerequisites
Make sure you have the following installed:

- Python (≥ 3.8)
- Pip (Python package manager)

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

Example requirements.txt:
```text
numpy
pandas
opencv-python
pytesseract
Pillow
matplotlib
torch
torchvision
```

### 👁️ OCR Setup (Tesseract)

- Ubuntu: `sudo apt install tesseract-ocr`
- Mac (Homebrew): `brew install tesseract`
- Windows: [Download Tesseract](https://github.com/tesseract-ocr/tesseract)

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

## 📚 Example Workflow

1. **Input:** An image of a doctor’s handwritten prescription.
2. **Process:** The image is processed, text is extracted, and analyzed.
3. **Output:** Medicines and care suggestions are printed.

## 🔧 Troubleshooting

- **Text not extracted:** Check the image quality and Tesseract installation.
- **Incorrect recommendations:** Expand the `MEDICINE_DB` in the recommendation engine.

## 🚀 Next Steps

- Enhance the NLP models for better text understanding.
- Integrate with real-time medicine databases via API.

---
