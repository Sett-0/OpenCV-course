import cv2 as cv 

# Reading photos
img1 = cv.imread("Images/cat.jpg")
img2 = cv.imread("Images/dogs.jpg")

cv.imshow('Cat', img1)
# cv.waitKey(0)
cv.imshow('Dogs', img2)
cv.waitKey(0)

# Reading videos
capture = cv.VideoCapture(0)

while(True):
    isTrue, frame = capture.read()
    cv.imshow('Webcam', frame)
    
    if (cv.waitKey(20) == ord('d')):
        break 
    
capture.release()
cv.destroyAllWindows()

