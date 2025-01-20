import cv2
import easyocr

image = cv2.imread("Path to your image")


reader = easyocr.Reader(['en'], gpu=False)
text_detections = reader.readtext(image)
text1=text_detections.split("\n")