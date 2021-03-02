import cv2 as cv
img  = cv.imread("20210208_153009.jpg")
cv.imshow("20210208_153009.jpg",img)
#bgr to grey
grey = cv.cvtColor(img ,cv.COLOR_BGR2GRAY)
cv.imshow("GREY", grey)
#bgr to hsv
hsv = cv.cvtColor(img , cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)
#bgr to lab
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

cv.waitKey(0)