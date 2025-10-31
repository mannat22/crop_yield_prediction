import streamlit as st
import numpy as np
import pickle
import gdown

st.title("🌾 Crop Yield Prediction App")

# ---- Download the model from Google Drive ----
model_path = "crop_yield_model.pkl"
file_id = "10_I6-gmrgMcELV9hem7SzBt61llgNur9"  # Replace this with your Google Drive file ID
gdown.download(f"https://drive.google.com/uc?export=download&id={file_id}", model_path, quiet=False)

# Load the trained model
with open(model_path, "rb") as f:
    model = pickle.load(f)

st.subheader("Enter details to predict crop yield:")

# ---- Define categorical options (adjust according to your dataset encodings) ----
crop_options = {
    "Rice": 0,
    "Wheat": 1,
    "Maize": 2,
    "Cotton": 3,
    "Sugarcane": 4
}

season_options = {
    "Summer": 0,
    "Winter": 1,
    "Kharif": 2,
    "Rabi": 3,
    "Zaid": 4
}

state_options = {
    "Punjab": 0,
    "Haryana": 1,
    "Maharashtra": 2,
    "Karnataka": 3,
    "Tamil Nadu": 4
}

# ---- User inputs ----
crop = st.selectbox("Crop Type", list(crop_options.keys()))
season = st.selectbox("Season", list(season_options.keys()))
state = st.selectbox("State", list(state_options.keys()))
area_options = {
    "Very Small (≤ 1 hectare)": 0.1,
    "Small (1–2 hectares)": 0.3,
    "Medium (2–5 hectares)": 0.5,
    "Large (5–10 hectares)": 0.7,
    "Very Large (≥ 10 hectares)": 0.9
}

area_label = st.selectbox("Area Size", list(area_options.keys()))
area = area_options[area_label]

production = st.slider("Production ", 0.0, 1.0, 0.5)
rainfall = st.slider("Annual Rainfall ", 0.0, 1.0, 0.5)
fertilizer = st.slider("Fertilizer ", 0.0, 1.0, 0.5)
pesticide = st.slider("Pesticide ", 0.0, 1.0, 0.5)

# ---- Convert text input to encoded values for model ----
input_data = np.array([[
    crop_options[crop],
    season_options[season],
    state_options[state],
    area,
    production,
    rainfall,
    fertilizer,
    pesticide
]])

# ---- Predict ----
if st.button("Predict Yield"):
    prediction = model.predict(input_data)[0]

    # --- Convert and format output meaningfully ---
    yield_value = round(prediction, 2)  # rounded number
    yield_ton = yield_value / 1000      # convert kg→tons if applicable

    st.success(
        f"🌾 Based on {season} season conditions in {state} for {crop}, "
        f"the predicted crop yield is **{yield_ton:.2f} tons per hectare.**"
    )

    st.caption(
        "💡 Note: 1 ton = 1000 kg. Actual yield values may vary depending on rainfall, soil, and local conditions."
    )

