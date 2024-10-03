from pytesseract import image_to_string
import pytesseract
from pypdf import PdfReader
from pdf2image import convert_from_path
import cv2
import numpy as np
from PIL import Image

# Function to apply OCR to an image
def extract_text_from_image(image):
    open_cv_image = np.array(image)
    open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2BGR)

    # Convert to grayscale for better OCR results
    gray = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)

    # Optional: Apply binary thresholding for better OCR results
    gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)[1]

    # Perform OCR using pytesseract
    text = image_to_string(gray, config='--psm 6')
    return text



    return None

print(summarizer('/Users/amitanand/Downloads/resume1.pdf'))