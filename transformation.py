import cv2 as cv
import numpy as np
img = cv.imread("165.jpg")
cv.imshow('165.jpg', img)

def translate(img ,x, y):

    transMat =np.float32([[1,0,x],[0,1,y]])
    dimension= (img.shape[0], img.shape[1])
    return cv.warpAffine(img , transMat , dimension)
translated = translate(img, -100, -50)
cv.imshow('translated', translated)
#cv.waitKey(0)


#    rotation

def rotate(img , angle , rotpoint = None):
    (hight ,width) = img.shape[:2]
    if rotpoint is None:
        rotpoint  = (width//2 , hight//2)
    rotMat = cv.getRotationMatrix2D(rotpoint , angle , 1.0)
    dimension = (width, hight)
    
    return cv.warpAffine(img,rotMat , dimension)
rotated = rotate(img , 45)
cv.imshow('Rotated', rotated)
#cv.waitKey(0)
rotated_rotated = rotate(rotated , -45)
cv.imshow("Rotated_rotated", rotated_rotated)
#resize

resized  = cv.resize(img ,(500 ,500), interpolation=cv.INTER_AREA)
cv.imshow("Resized",resized)

# flip
flip = cv.flip(img , 1)
cv.imshow('Flip', flip)
# cropped 

#cropped =cv. img(200 ,400 ,300 ,400))
#cv.imshow('Cropped', cropped)





cv.waitKey(0)

    

