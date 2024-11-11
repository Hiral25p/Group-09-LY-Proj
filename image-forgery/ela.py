import os
from PIL import Image, ImageChops, ImageEnhance

# Converts the input image to an ELA-applied image
def convert_to_ela_image(file, quality):
    """
    Converts an image to Error Level Analysis (ELA) format.
    
    Parameters:
    - file: file path or an in-memory file (Streamlit upload).
    - quality: Quality setting for resaving the image to create ELA.
    
    Returns:
    - ELA image in PIL format.
    """
    
    # Open the original image, whether from file path or in-memory
    original_image = Image.open(file).convert("RGB")
    
    # Resave the image at the specified quality to create subtle compression artifacts
    resaved_file_name = "resaved_image.jpg"
    original_image.save(resaved_file_name, "JPEG", quality=quality)
    resaved_image = Image.open(resaved_file_name)
    
    # Calculate the difference between the original and resaved images
    ela_image = ImageChops.difference(original_image, resaved_image)
    
    # Determine the maximum difference for scaling
    extrema = ela_image.getextrema()
    max_difference = max([pix[1] for pix in extrema])
    scale = 350.0 / max_difference if max_difference != 0 else 1
    
    # Enhance the brightness to highlight differences
    ela_image = ImageEnhance.Brightness(ela_image).enhance(scale)
    
    # Save the ELA image for visualization, or return it directly
    ela_image.save("ela_image.png")
    
    return ela_image