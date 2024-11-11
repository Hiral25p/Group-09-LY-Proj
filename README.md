# ForgeGuard: Fortifying Authenticity, One Scan at a Time.

An AI-powered solution that detects signature and image forgery with precision, ensuring document authenticity and safeguarding against digital fraud.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)

## Introduction

ForgeGuard is a robust AI-driven tool designed to detect forgeries in images and signatures, ensuring document integrity and trustworthiness. As digital transactions and document exchanges increase, so does the risk of forgery and fraud. ForgeGuard addresses this need by offering precise, easy-to-use verification, fortifying authenticity in personal and professional exchanges and safeguarding against identity theft and legal complications.

## Features

- Signature Verification: Accurately detects forged signatures by analyzing unique patterns, ensuring the authenticity of signed documents.
- Image Forgery Detection: Uses advanced AI techniques to identify alterations, manipulations, and inconsistencies in images, safeguarding against tampered visuals.
- User-Friendly Interface: Simple and intuitive interface for seamless uploads or real-time image capture, making it easy for anyone to verify authenticity.
- High Accuracy and Speed: Powered by advanced algorithms that quickly analyze and provide reliable results, saving time without compromising accuracy.

## Requirements

Make sure you have the following Python packages installed:

- `numpy`: A library for numerical computations and array manipulations.
- `pandas`: A powerful data manipulation and analysis library.
- `matplotlib`: A library for creating static, animated, and interactive visualizations in Python.
- `scikit-learn`: A machine learning library that provides simple and efficient tools for data mining and data analysis.
- `streamlit`: A framework for building interactive web applications, especially useful for data science projects.

You can install these packages using the `requirements.txt` file:

```sh
pip install -r requirements.txt
```

## Installation

1. Clone the repo
   ```sh
    https://github.com/Hiral25p/Group-09-LY-Proj
   ```
2. Change your working directory to the project folder:
   ```sh
   cd Group-09-LY-Proj
   ```
   _Ensure that you have the required packages installed (see the "Requirements" section)._
3. Run the program:
   ```sh
   streamlit run app.py
   ```
   Or
    ```sh
   python -m streamlit run app.py
   ```
    
## Usage

![WhatsApp Image 2024-11-11 at 06 23 27_58eae5ee](https://github.com/user-attachments/assets/bc7430f9-62b3-40f0-bb2b-b344f827c787)

- Upload your signature image documents through the provided interface for processing and get a result.

![image](https://github.com/user-attachments/assets/6109673b-f527-4995-bbe4-399affd37416)
  
- Image anomaly detection interface.

![image](https://github.com/user-attachments/assets/9f6c4980-210d-4a67-a8a7-9497a056f0a4)

- ELA being performed on the document.

![image](https://github.com/user-attachments/assets/cd9094b0-1e93-4128-b5b0-d68c8d679846)

- Final outcome of the processed file.

![WhatsApp Image 2024-11-11 at 07 37 11_a8cdb47c](https://github.com/user-attachments/assets/ebe6adc6-4449-448b-a36c-a702e0c1ec3c)

- Confusion Matrix.

![WhatsApp Image 2024-11-11 at 07 39 35_4e76a6cc](https://github.com/user-attachments/assets/27899cd1-a8ca-4f55-9afb-160fa4b8e93a)

- Performance Metrics.

## File Structure

```
📦 
├─ __pycache__
│  ├─ ela.cpython-310.pyc
│  ├─ image_forgery.cpython-310.pyc
│  └─ prediction.cpython-310.pyc
├─ image-forgery
│  ├─ IFD.ipynb
│  ├─ __pycache__
│  │  ├─ ela.cpython-310.pyc
│  │  └─ prediction.cpython-310.pyc
│  ├─ app.py
│  ├─ ela.py
│  ├─ ela_image.png
│  ├─ gui.ui
│  ├─ model_history.json
│  ├─ prediction.py
│  ├─ requirements.txt
│  ├─ resaved_image.jpg
│  ├─ trained_model.h5
│  └─ ui.py
├─ main.py
└─ signature-forgery
   ├─ __pycache__
   │  └─ signature.cpython-310.pyc
   ├─ app.py
   ├─ main.py
   ├─ signature.py
   └─ temp
      ├─ image1.png
      └─ image2.png
```
