



import cv2
from PIL import Image
from googletrans import Translator
import pytesseract

def tesseract(img):
    # image = 'test.jpg'
    # pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(img)
    txt = str(text[:-1])
    print(txt)
    return txt


cap = cv2.VideoCapture(0)



while True:
    ref, img = cap.read()
    
    # print(pytesseract.image_to_string(img))
    # cv2.imwrite('test.jpg',img)
    en_text = tesseract(img)
    translator = Translator()
    txt = translator.translate(en_text, dest='hi')
    print(txt.text)

    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xff== 27:
        break

cap.release()
cv2.destroyAllWindows() 

