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


st.subheader("Enter details to predict crop yield:")

crop = st.number_input("Crop (encoded)", min_value=0)
season = st.number_input("Season (encoded)", min_value=0)
state = st.number_input("State (encoded)", min_value=0)
area = st.slider("Area (normalized)", 0.0, 1.0)
production = st.slider("Production (normalized)", 0.0, 1.0)
rainfall = st.slider("Annual Rainfall (normalized)", 0.0, 1.0)
fertilizer = st.slider("Fertilizer (normalized)", 0.0, 1.0)
pesticide = st.slider("Pesticide (normalized)", 0.0, 1.0)

if st.button("Predict Yield"):
    input_data = np.array([[crop, season, state, area, production, rainfall, fertilizer, pesticide]])
    prediction = model.predict(input_data)
    st.success(f"🌱 Predicted Crop Yield: {prediction[0]:.2f}")
