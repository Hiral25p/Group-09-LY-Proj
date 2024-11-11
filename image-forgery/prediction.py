import numpy as np
from keras.models import load_model
from ela import convert_to_ela_image
from PIL import Image

# Load the trained model once to avoid reloading it multiple times
model = load_model("trained_model.h5")
class_names = ["Forged", "Authentic"]

def prepare_image(file):
    """
    Prepares the image for model prediction by applying ELA, resizing, and normalizing.
    
    Parameters:
    - file: file path or in-memory file for the image.
    
    Returns:
    - A normalized numpy array ready for model prediction.
    """
    image_size = (128, 128)  # Expected input size for the model
    
    # Convert the image to an ELA format and resize it
    ela_image = convert_to_ela_image(file, 90)
    ela_image = ela_image.resize(image_size)
    
    # Convert ELA image to a normalized numpy array
    ela_array = np.array(ela_image).astype('float32') / 255.0
    ela_array = ela_array.reshape(-1, 128, 128, 3)  # Reshape to match model input
    
    return ela_array

def predict_result(file):
    """
    Predicts whether the given image is "Forged" or "Authentic".
    
    Parameters:
    - file: file path or in-memory file for the image.
    
    Returns:
    - prediction: "Forged" or "Authentic"
    - confidence: Confidence score as a percentage
    """
    # Prepare the image for prediction
    test_image = prepare_image(file)
    
    # Make the prediction
    y_pred = model.predict(test_image)
    y_pred_class = int(y_pred[0][0] > 0.5)  # Rounds to 0 or 1 for class index
    
    prediction = class_names[y_pred_class]
    confidence = (y_pred[0][0] if y_pred_class == 1 else 1 - y_pred[0][0]) * 100
    confidence = f"{confidence:.2f}"
    
    return prediction, confidence
