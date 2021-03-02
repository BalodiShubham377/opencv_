import cv2 as cv
import  numpy as np
img  =cv.imread('20210208_153009.jpg')
cv.imshow('20210208_153009.jpg', img)

#blank = np.zeros(img.shape[:2],dtype="uint8")
blank = np.zeros(img.shape,dtype="uint8")
cv.imshow("blank", blank)
grey = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow("Grey", grey)

#blur = cv.GaussianBlur(grey , (5,5) , cv.BORDER_DEFAULT)
#cv.imshow("Blur", blur)
#ret, thresh = cv.threshold(grey , 125,255, cv.THRESH_BINARY)
#cv.imshow('THRESH', thresh)

canny = cv.Canny(grey , 125 ,175)
cv.imshow("Canny", canny)
countours , hierarchies =cv.findContours(canny ,cv.RETR_LIST ,cv.CHAIN_APPROX_SIMPLE)
print(f"{len(countours)} countours found")

cv.drawContours(blank , countours, -1 , (0,0,255), 1)
cv.imshow("countours_drawn", blank)
cv.waitKey(0)
