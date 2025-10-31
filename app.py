import streamlit as st
import numpy as np
import pickle
import gdown

st.title("🌾 Crop Yield Prediction App")

# Google Drive model file
model_path = "crop_yield_model.pkl"
file_id = "10_I6-gmrgMcELV9hem7SzBt61llgNur9"

# Download from Drive if not already present
gdown.download(f"https://drive.google.com/uc?id={file_id}", model_path, quiet=False)

# Load normal pickle file (NOT gzip)
with open(model_path, "rb") as f:
    model = pickle.load(f)
