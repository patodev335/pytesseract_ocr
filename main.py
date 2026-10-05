#PATRICIO MONSALVO dea le ponía copyright a esto re simple.

import cv2
import pytesseract

# so basically the idea is:
# 1) transform the img to grayscale
# 2) take out noise
# 3) define contrast (threshold)
# 4) send to pytesseract (ocr)
# 5) print text

def ocr(img):
    return pytesseract.image_to_string(img)

#1
def img_to_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#2
def remove_noise(img):
    return cv2.medianBlur(img, 5)

#3
def threshold(img):
    return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

img = cv2.imread("example.png") #lit. just read the damn image
img = img_to_grayscale(img)
img = threshold(img)
img = remove_noise(img)

#let's look at the final image!
cv2.imwrite("result.png", img)

print(ocr(img))