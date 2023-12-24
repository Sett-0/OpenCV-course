import cv2 as cv
import numpy as np 

def show_window(img_name='Window', image=np.zeros((50, 50, 3)), dtype='uint8'):
    cv.imshow(img_name, image)
    cv.waitKey(0)
    cv.destroyAllWindows()

img = cv.imread('Images/fox.jpg')
# show_window('Fox', img)

# Grayscale 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
show_window('Grayscale fox', gray)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
show_window('Blurred fox', blur)

# Edge cascade
canny = cv.Canny(img, 30, 75)
show_window('Edges fox', canny)

# Dilating (increasing edge thichness)
dilated = cv.dilate(canny, (7,7), iterations=2)
show_window('Dilated fox', dilated)

# Eroding (decreasing edge thickness)
eroded = cv.erode(dilated, (7,7), iterations=2)
show_window('Eroded fox', eroded)

# Resized
resized = cv.resize(img, (int(img.shape[1]*1.2), int(img.shape[0]*1.2)), interpolation=cv.INTER_CUBIC)
show_window("Resized fox", resized)

# Cropped
cropped = img[200:500, 200:500]
show_window("Cropped fox", cropped)