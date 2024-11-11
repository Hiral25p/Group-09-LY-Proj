# main.py
import streamlit as st
import os

# Set the page configuration
st.set_page_config(page_title="Forgery Detection", layout="centered")

# CSS styling for the main page
st.markdown("""
    <style>
    /* Background */
    .main {
        background: rgb(64,85,187);
        background: linear-gradient(18deg, rgba(64,85,187,1) 23%, rgba(141,135,206,1) 70%);
        font-family: 'Arial', sans-serif;
    }
    body {
        background-color: #f0f8ff;
        color: #333333;
    }
    /* Title styling */
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #ffffff;
        text-align: center;
        margin-top: 20px;
    }
    /* Subtitle styling */
    .subtitle {
        font-size: 18px;
        color: #ffffff;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Title and Description
st.markdown("<div class='title'>Forgery Detection Hub</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Ensuring the authenticity and integrity of documents and images with advanced forgery detection.</div>", unsafe_allow_html=True)

# Explanation Section
st.write("## Why Forgery Detection Matters")
st.write("""
Forgery detection is crucial in safeguarding authenticity in legal, financial, and personal documents. 
Our tools empower you to detect fraudulent signatures and image manipulations quickly and accurately.

### How We Do It:
1. **Signature Forgery Detection** - Verifies if two signatures match by comparing unique patterns.
2. **Image Forgery Detection** - Identifies potential alterations in images by analyzing for inconsistencies.
""")

# User Choice Section
st.write("## Choose a Forgery Detection Tool:")
choice = st.selectbox("Select Detection Type", ["Select an option", "Signature Forgery Detection", "Image Forgery Detection"])

# Navigate based on the user's choice
if choice == "Signature Forgery Detection":
    os.system("streamlit run signature-forgery/app.py")
elif choice == "Image Forgery Detection":
    os.system("streamlit run image-forgery/app.py")