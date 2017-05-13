from PIL import Image
from pytesseract import *
a= (pytesseract.image_to_string(Image.open("hindi1.jpg"), lang="hin"))
print a
with open("Output.txt", "w") as text_file:
    text_file.write(" %s" % a)
