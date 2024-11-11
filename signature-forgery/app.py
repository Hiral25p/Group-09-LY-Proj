# app.py
import streamlit as st
import os
import cv2
from signature import match
from tempfile import NamedTemporaryFile
from PIL import Image

# Match Threshold
THRESHOLD = 75

# Page configuration
st.set_page_config(page_title="Signature Forgery Detection", layout="centered")

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

    /* Title and Subtitle styling */
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #ffffff;
        text-align: center;
        margin-top: 20px;
    }
    .subtitle {
        font-size: 18px;
        color: #ffffff;
        text-align: center;
        margin-bottom: 40px;
    }

    /* Section Header styling */
    h1, h2, h3 {
        color: #ffffff;
        text-align: left;
    }

    /* Button styling */
    .stButton button {
        background-color: lightslategray;
        color: azure;
        font-weight: bold;
        border-radius: 5px;
        padding: 8px 16px;
    }

    /* Image upload section styling */
    .stFileUploader label {
        display: flex;
        justify-content: center;
        font-weight: bold;
        color: #333333;
    }

    /* Compare button alignment */
    .compare-button {
        text-align: center;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Title and Subtitle
st.markdown("<div class='title'>🔍 Signature Forgery Detection</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Verify the authenticity of signatures with precise analysis. Upload or capture two signature images for comparison.</div>", unsafe_allow_html=True)

# Function to capture image from camera
def capture_image_from_cam(sign=1):
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        st.error("Could not open the camera.")
        return None

    st.text("Press 'c' to capture an image, or 'q' to quit.")
    while True:
        ret, frame = cam.read()
        if not ret:
            st.error("Failed to grab frame.")
            break
        cv2.imshow("Camera", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('c'):
            # Save the captured image to a temporary file
            with NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
                img_path = tmpfile.name
                cv2.imwrite(img_path, frame)
            break

    cam.release()
    cv2.destroyAllWindows()
    return img_path

# Function to check similarity between signatures
def checkSimilarity(path1, path2):
    result = match(path1=path1, path2=path2)
    if result <= THRESHOLD:
        st.error(f"❌ Signatures Do Not Match. Similarity: {result:.2f} %")
    else:
        st.success(f"✅ Signatures Match! Similarity: {result:.2f} %")
    return result

# Ensure the 'temp' directory exists
if not os.path.exists("temp"):
    os.makedirs("temp")

# Side-by-side layout for Signature 1 and Signature 2
col1, col2 = st.columns(2)

with col1:
    st.subheader("Signature 1")
    image1_file = st.file_uploader("Upload an Image", type=['jpeg', 'jpg', 'png'], key="image1")
    if st.button("Capture from Camera (1)", key="cam1"):
        image1_path = capture_image_from_cam(sign=1)
        if image1_path:
            st.image(image1_path, caption="Captured Image 1", use_column_width=True)

    # Display uploaded or captured Signature 1
    if image1_file:
        image1_path = os.path.join("temp", "image1.png")
        with open(image1_path, "wb") as f:
            f.write(image1_file.getbuffer())
        st.image(Image.open(image1_path), caption="Signature 1", use_column_width=True)

with col2:
    st.subheader("Signature 2")
    image2_file = st.file_uploader("Upload an Image", type=['jpeg', 'jpg', 'png'], key="image2")
    if st.button("Capture from Camera (2)", key="cam2"):
        image2_path = capture_image_from_cam(sign=2)
        if image2_path:
            st.image(image2_path, caption="Captured Image 2", use_column_width=True)

    # Display uploaded or captured Signature 2
    if image2_file:
        image2_path = os.path.join("temp", "image2.png")
        with open(image2_path, "wb") as f:
            f.write(image2_file.getbuffer())
        st.image(Image.open(image2_path), caption="Signature 2", use_column_width=True)

# Compare button centered below both columns
st.markdown("<div class='compare-button'>", unsafe_allow_html=True)
if st.button("🔍 Compare Signatures"):
    if 'image1_path' in locals() and 'image2_path' in locals():
        checkSimilarity(image1_path, image2_path)
    else:
        st.warning("Please upload or capture both signatures before comparing.")
st.markdown("</div>", unsafe_allow_html=True)
