import cv2 as cv 
import numpy as np 

blank_img = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank_img)

cv.waitKey(0)
cv.destroyAllWindows()

# 1. Paint the image a color
img = blank_img.copy()
img[:] = (0, 255, 0) # Not RGB, but BGR for some reason...
cv.imshow('Green', img)

cv.waitKey(0)
cv.destroyAllWindows()

# 2. Paint part of the image a color
img = blank_img.copy()
img[150:350, 150:350] = (0, 0, 255) # Not RGB, but BGR for some reason...
cv.imshow('Red part', img)

cv.waitKey(0)
cv.destroyAllWindows()

# 3. Draw a rectangle
img = blank_img.copy()
cv.rectangle(img, (100, 150), (400, 350), (255, 0, 0), thickness=2) # thickness=cv.FILLED or =-1 to fill the rectangle
cv.imshow('Rectangle', img)

cv.waitKey(0)
cv.destroyAllWindows()

# 4. Draw a circle
img = blank_img.copy()
cv.circle(img, (250, 250), 100, (0, 255, 255), thickness=cv.FILLED)
cv.imshow('Circle', img)

cv.waitKey(0)
cv.destroyAllWindows()

# 5. Draw a line
img = blank_img.copy()
cv.line(img, (0, 0), (500, 500), (0, 0, 255), thickness=2)
cv.line(img, (500, 0), (0, 500), (0, 0, 255), thickness=2)
cv.imshow('Lines', img)

cv.waitKey(0)
cv.destroyAllWindows()

# 6. Write text on image
img = blank_img.copy()
cv.putText(img, 'Hello World!', (150, 260), cv.FONT_HERSHEY_TRIPLEX, 1., (0, 255, 0), thickness=2)
# cv.line(img, (0, 250), (500, 250), (255, 255, 255), thickness=1)

cv.imshow('Text', img)

cv.waitKey(0)
cv.destroyAllWindows()