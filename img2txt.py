from importlib.resources import path
import pytesseract as tess
from PIL import Image
import pytesseract as tess

class img2txt :
    def img2txt (ref,path):
        img = Image.open(path)
        print("converting img into text...")
        text = tess.image_to_string(img)
        print (text)
        return text
        

# obj = img2txt()
# path = "img.png"
# obj.img2txt(path)