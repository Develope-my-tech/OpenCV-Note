from PIL import Image
from pytesseract import *

filename = "image/04_tesseract_test2.PNG"
img = Image.open(filename)
text = image_to_string(img, lang="kor")
print(text)
