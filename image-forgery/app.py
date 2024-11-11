# app.py
import streamlit as st
from PIL import Image
from prediction import predict_result
from ela import convert_to_ela_image

# Page configuration
st.set_page_config(page_title="Signature Forgery Detection", layout="centered", initial_sidebar_state="collapsed")

# Custom CSS for styling
st.markdown("""
    <style>
    /* Background */
    .main {
        background: rgb(64,85,187);
        background: linear-gradient(18deg, rgba(64,85,187,1) 23%, rgba(141,135,206,1) 70%);
        font-family: 'Arial', sans-serif;
    }
    body {
        background-color: #f0f8ff; /* Light background */
        color: #333333;
    }
    </style>
""", unsafe_allow_html=True)

# Title and Description
st.title("🔍 Signature Forgery Detection")
st.markdown("""
This application uses **Error Level Analysis (ELA)** and a deep learning model to detect potential forgeries in digital signatures. 
Upload an image of a signature, and the app will analyze it for signs of manipulation. 

- **Original Image**: This is the image you provide.
- **ELA Image**: Shows differences between the original and a compressed version, highlighting areas of potential alteration.
- **Result**: The model's prediction and confidence level.

---
""")

# Styling the sidebar
st.sidebar.header("Instructions")
st.sidebar.write("""
1. Upload an image file of the signature (PNG or JPG format).
2. Click "Analyze" to run the forgery detection.
3. See the prediction and confidence score below the ELA image.
""")
st.sidebar.write("For best results, use clear and high-resolution images.")

# Image upload section
st.subheader("Upload Signature Image")
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

# Display uploaded image and results
if uploaded_file is not None:
    # Display the original image
    st.image(uploaded_file, caption="Original Image", use_column_width=True)

    # Convert to ELA image and display
    ela_image = convert_to_ela_image(uploaded_file, 90)
    
    # Add a bit of spacing
    st.write("---")
    
    # Display the ELA image
    st.subheader("Error Level Analysis (ELA) Image")
    st.image(ela_image, caption="ELA Image", use_column_width=True)

    # Prediction button and results
    if st.button("🔍 Analyze"):
        prediction, confidence = predict_result(uploaded_file)
        
        # Display the result with improved formatting
        st.write("---")
        st.markdown(f"### Prediction: **{prediction}**")
        st.markdown(f"### Confidence: **{confidence}%**")
        
        # Custom message based on prediction
        if prediction == "Forged":
            st.error("The image is likely to be a forgery.")
        else:
            st.success("The image appears to be authentic.")

else:
    st.info("Please upload an image to start the analysis.")