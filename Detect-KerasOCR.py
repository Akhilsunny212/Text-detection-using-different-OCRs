import keras_ocr
from keras_ocr import detection,recognition
import matplotlib.pyplot as plt
import pandas as pd
import cv2
import pytesseract
import os
import glob


k={}
images = [keras_ocr.tools.read(img) for img in ["image_path"]]
pipeline = keras_ocr.pipeline.Pipeline()
results=pipeline.recognize(images)
margin=5
width, height = images[0].shape[:2]
df = pd.DataFrame(results[0],columns=["Text","Bounding_Boxes"])
Bounding_boxes = df["Bounding_Boxes"].values
text1=df["Text"].values
k["test"]=list(text1)


cv2.imwrite("image.jpg",keras_ocr.tools.drawBoxes(cv2.imread("image_path"),Bounding_boxes,thickness=1))