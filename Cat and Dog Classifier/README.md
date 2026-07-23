<div align="center">

# Cat vs Dog Image Classifier
### A Deep Learning Image Classification App powered by TensorFlow & Streamlit

<p>
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/TensorFlow-Keras-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" alt="TensorFlow"/>
  <img src="https://img.shields.io/badge/NumPy-Data-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"/>
  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/>
</p>

</div>

---

## 🧠 Project Overview

The **Cat vs Dog Image Classifier** is a deep learning computer vision project that classifies an uploaded image as either a **Cat** or a **Dog**, using a trained Convolutional Neural Network (CNN) served through an interactive Streamlit web app.

> 💡 **Why it matters:** Image classification is one of the most foundational tasks in computer vision, and this project demonstrates the full journey from a trained Keras model to a deployed, user-facing prediction app — a pattern that generalizes to countless real-world visual recognition tasks.

**Real-world applications:**
- 🐾 Pet identification & shelter management systems
- 📱 Photo-organizing apps with automatic tagging
- 🎓 Educational tool for teaching CNN-based image classification
- 🧪 Baseline template for other binary image classification problems

**Expected users:** ML learners, recruiters evaluating computer vision skills, and developers looking for a lightweight CNN deployment reference.

---

---

## ✨ Features

- ✅ Upload any `.jpg`, `.jpeg`, or `.png` image
- ✅ Real-time inference using a trained CNN
- ✅ Confidence score displayed alongside prediction
- ✅ Automatic image preprocessing (resize, normalize, RGBA→RGB handling)
- ✅ Clean, single-page Streamlit interface

---

## 🛠 Tech Stack

| Category | Tools |
|---|---|
| **Language** | Python |
| **Deep Learning Framework** | TensorFlow / Keras |
| **Data Handling** | NumPy, Pandas |
| **Image Processing** | Pillow (PIL) |
| **Web App / Deployment** | Streamlit |
| **Model Format** | Keras (`.keras`) |
| **Version Control** | Git & GitHub |

---

## 📁 Project Structure

```
cat-dog-classifier/
│
├── notebooks/
│   └── (training notebook)     # Model training & experimentation
│
├── app.py                      # Streamlit application entry point
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

---

## 🔄 Workflow

```
Image Dataset Collection
         ↓
Data Preprocessing (Resize, Normalize)
         ↓
CNN Model Architecture Design
         ↓
Model Training
         ↓
Model Evaluation
         ↓
Model Export (.keras)
         ↓
Streamlit Deployment
         ↓
Real-time Image Prediction
```

---

## 📊 Dataset

> ⚠️ Dataset details were not available during README generation.

| Detail | Value |
|---|---|
| **Source** | [Cat and Dog Dataset](https://www.kaggle.com/datasets/tongpython/cat-and-dog) |
| **Target Classes** | Cat, Dog |
| **Input** | RGB images, resized to `128 × 128` |
| **Number of Samples** | *Not specified* |
| **Missing Values** | Not applicable (image data) |

---

## 🧹 Data Preprocessing

Confirmed from `app.py`'s inference pipeline:

- Images resized to **128 × 128** pixels
- RGBA images converted to RGB (alpha channel dropped)
- Pixel values normalized to the **[0, 1]** range (`/ 255.0`)
- Batch dimension added via `np.expand_dims` before inference

---

## 🧠 Model Used

| Model | Purpose |
|---|---|
| Convolutional Neural Network (Keras) | Binary image classification — Cat vs Dog |

> 📌 Exact architecture (number of layers, filters, activation functions) is **not confirmed** — add a model summary from the training notebook for full transparency.

---

## ▶️ Usage

Run the Streamlit app locally:

```bash
streamlit run app.py
```

Then open your browser at:

```
http://localhost:8501
```

---

## 🚀 Future Improvements

- [ ] Add training notebook with full EDA and model architecture
- [ ] Add data augmentation for better generalization
- [ ] Deploy on Streamlit Community Cloud / Render / Hugging Face Spaces
- [ ] Containerize with Docker
- [ ] Add CI/CD pipeline (GitHub Actions)
- [ ] Extend to multi-class animal classification
- [ ] Add automated testing for the preprocessing/prediction pipeline

---

## 👤 Author

### Rohit Rane

Aspiring Machine Learning Engineer | MLOps Enthusiast

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star!

</div>
