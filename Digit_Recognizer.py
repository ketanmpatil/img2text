import easyocr
import cv2
import numpy


reader=easyocr.Reader(['en']) # Easy OCR imager Reader


def OCR(image): # Image = Image path
    result = reader.readtext(image) # Used to read text from images
    return str(result[0][1]) # Returns result in integer format