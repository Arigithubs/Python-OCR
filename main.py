import pytesseract
from PIL import Image

# Path to tesseract executable
# On Windows, it might be something like 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'path_to_tesseract_executable'

# Function to perform OCR
def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

# Example usage
print(ocr_core('path_to_image'))
