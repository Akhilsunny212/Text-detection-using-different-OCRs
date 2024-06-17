import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "Path to your Tesseract location in local"
# Load your image
image = cv2.imread("Path to your image")

text = pytesseract.image_to_string(image, config='--psm 11')
# provide psm values based on the requirement
print(text)