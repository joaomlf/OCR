import pytesseract
import pandas as pd
import cv2 as cv

from PIL import Image, ImageFilter, ImageEnhance

class Output:
    BYTES = 'bytes'
    DATAFRAME = 'data.frame'
    DICT = 'dict'
    STRING = 'string'

### directoria do programa Tesseract-OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
#    text = pytesseract.image_to_data(Image.open(filename), lang='por', output_type=Output.DATAFRAME)  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    text = pytesseract.image_to_string(Image.open(filename), lang='por')
    return text

### CC - frente
img = Image.open("CC1.jpg")
img.save("CC1.jpg", dpi=(300,300))

imga = cv.imread('CC1.jpg')
# RGB to BW
imga = cv.cvtColor(imga, cv.COLOR_BGR2GRAY)
# Gaussian filtering
blur1 = cv.GaussianBlur(imga, (5,5), 0)
cv.imwrite('frente.jpg', blur1)
# binarizing image
imga1 = cv.imread('frente.jpg', 2)
#bw_img = cv.adaptiveThreshold(img1,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
ret, bw_img1 = cv.threshold(imga1, 74, 255, cv.THRESH_BINARY)
cv.imwrite('frente_a.jpg',bw_img1)

#df = pd.DataFrame(ocr_core('frente_a.jpg'))
#print(df.text)
print(ocr_core('frente_a.jpg'))

print("\n----------------------------------------\n")

### CC - verso
img = Image.open("CC2.jpg")
img.save("CC2.jpg", dpi=(300,300))

imgb = cv.imread('CC2.jpg')
# RGB to BW
imgb = cv.cvtColor(imgb, cv.COLOR_BGR2GRAY)
# Gaussian filtering
blur2 = cv.GaussianBlur(imgb, (5,5), 0)
cv.imwrite('verso.jpg', blur2)
# binarizing image
imgb1 = cv.imread('verso.jpg', 2)
#bw_img = cv.adaptiveThreshold(img1,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
ret2, bw_img2 = cv.threshold(imgb1, 106, 255, cv.THRESH_BINARY)
cv.imwrite('verso_a.jpg',bw_img2)

#df2 = pd.DataFrame(ocr_core('verso_a.jpg'))
#print(df2.text)
print(ocr_core('verso_a.jpg'))

#### TEXTO
#img = Image.open("pt_text.png")
#img.save("pt_text.png", dpi=(300,300))
#
#imga = cv.imread('pt_text.png')
## RGB to BW
#imga = cv.cvtColor(imga, cv.COLOR_BGR2GRAY)
## Gaussian filtering
#blur1 = cv.GaussianBlur(imga, (5,5),0)
#cv.imwrite('pt_text_a.png', blur1)
#
## binarizing image
#imga1 = cv.imread('pt_text_a.png', 2)
##bw_img = cv.adaptiveThreshold(img1,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
#ret, bw_img1 = cv.threshold(imga1,84,255,cv.THRESH_BINARY)
#cv.imwrite('pt_text_final.png', bw_img1)
#
##df = pd.DataFrame(ocr_core('frente_a.jpg'))
##print(df.text)
#print(ocr_core('pt_text.png'))