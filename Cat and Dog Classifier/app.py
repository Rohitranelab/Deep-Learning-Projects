import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# Load model
model = load_model("cat_and_dog.keras")

# Image Size (same as training)
IMAGE_SIZE = (128, 128)

# Class Names
classes = ["Cat", "Dog"]

st.set_page_config(
    page_title="Cat vs Dog Classifier"
)

st.title("Cat vs Dog Image Classifier")

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    img = Image.open(uploaded_file)

    st.image(img, caption="Uploaded Image", use_container_width=True)

    # Preprocess
    img = img.resize(IMAGE_SIZE)
    img = np.array(img)

    if img.shape[-1] == 4:
        img = img[:, :, :3]

    img = img.astype("float32") / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)

    predicted_class = classes[np.argmax(prediction)]
    confidence = np.max(prediction)

    st.success(f"Prediction : {predicted_class}")
    st.write(f"Confidence : {confidence:.2%}")