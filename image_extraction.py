import imutils
import cv2
import pytesseract

img = "ADD IMG PATH"
image = cv2.imread(img) # READING/OPENING THE IMAGE

# cv2.imshow('Actual Image',image)
# cv2.waitKey(0)
image = imutils.resize(image,1024,665) #RESIZING THE IMGE

image = image[495:540,290:516] #SLICING THE CNIC NUMBER PART FROM IMGAE
cv2.imshow('Image Slice',image)
cv2.waitKey(0)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #CONVERTING THE IMAGE INTO GRAY SCALE
gray = cv2.threshold(gray,50, 2255,cv2.THRESH_BINARY)[1]

# cv2.imshow('gray', gray)
# cv2.waitKey(0)

number = pytesseract.image_to_string(gray)[0:15] #CONVERTING IMAGE TO TEXT

print(number)

