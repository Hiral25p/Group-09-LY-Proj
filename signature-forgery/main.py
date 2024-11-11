import streamlit as st
import os
import cv2
from signature import match
from tempfile import NamedTemporaryFile
from PIL import Image

# Match Threshold
THRESHOLD = 85

# Ensure the 'temp' directory exists
if not os.path.exists('temp'):
    os.makedirs('temp')

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

def checkSimilarity(path1, path2):
    result = match(path1=path1, path2=path2)
    if result <= THRESHOLD:
        st.error(f"Failure: Signatures Do Not Match. Similarity: {result} %")
    else:
        st.success(f"Success: Signatures Match! Similarity: {result} %")
    return result

# Streamlit Interface
st.title("Signature Matching")
st.write("Compare two signatures to check similarity.")

# Upload and capture options for Signature 1
st.subheader("Signature 1")
col1, col2 = st.columns(2)
with col1:
    image1_file = st.file_uploader("Upload an Image", type=['jpeg', 'jpg', 'png'])
with col2:
    if st.button("Capture from Camera (1)"):
        image1_path = capture_image_from_cam(sign=1)
        if image1_path:
            st.image(image1_path, caption="Captured Image 1", use_column_width=True)

# Display uploaded or captured Signature 1
if image1_file:
    image1_path = os.path.join("temp", "image1.png")
    with open(image1_path, "wb") as f:
        f.write(image1_file.getbuffer())
    st.image(Image.open(image1_path), caption="Signature 1", use_column_width=True)

# Upload and capture options for Signature 2
st.subheader("Signature 2")
col1, col2 = st.columns(2)
with col1:
    image2_file = st.file_uploader("Upload an Image", type=['jpeg', 'jpg', 'png'], key="image2")
with col2:
    if st.button("Capture from Camera (2)"):
        image2_path = capture_image_from_cam(sign=2)
        if image2_path:
            st.image(image2_path, caption="Captured Image 2", use_column_width=True)

# Display uploaded or captured Signature 2
if image2_file:
    image2_path = os.path.join("temp", "image2.png")
    with open(image2_path, "wb") as f:
        f.write(image2_file.getbuffer())
    st.image(Image.open(image2_path), caption="Signature 2", use_column_width=True)

# Compare button
if st.button("Compare Signatures"):
    if image1_path and image2_path:
        checkSimilarity(image1_path, image2_path)
    else:
        st.warning("Please upload or capture both signatures before comparing.")