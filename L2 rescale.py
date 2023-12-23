import cv2 as cv 

# Works for images, videos and live videos
def rescale_frame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    return cv.resize(frame, (width, height), interpolation=cv.INTER_AREA)

# Works for live videos only
def change_res(width, height):
    capture.set(3, width)
    capture.set(4, height)


img = cv.imread("Images/cat.jpg")
cv.imshow('Cat', img)
cv.imshow('Cat_resized', rescale_frame(img, scale=.5))
cv.waitKey(0)
cv.destroyAllWindows()

capture = cv.VideoCapture(0)
# width = int(300)
# height = int(300)
# change_res(width, height)

while(True):
    isTrue, frame = capture.read()
    
    cv.imshow('Webcam', frame)
    # cv.imshow('Webcam_resized', rescale_frame(frame))
    
    if (cv.waitKey(20) == ord('q')):
        break 
    
capture.release()
cv.destroyAllWindows()