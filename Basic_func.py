import cv2 as cv
img = cv.imread('IMG_20181003_205513.jpg')
grey = cv.cvtColor(img , cv.COLOR_BGR2RGB)

cv.imshow('Grey', grey)

#cv.waitKey(0)
# blur

blur = cv.GaussianBlur(img,(3,3), cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)
#cv.waitKey(0)

# Edge CASCADE

canny = cv.Canny(blur,125,125)
cv.imshow("Canny", canny)
cv.waitKey(0)
# dilated

dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow("Dilated", dilated)
#cv.waitKey(0)

#eroded

eroded = cv.erode(dilated,(3,3), iterations=1)
cv.imshow('Erode',eroded)
cv.waitKey(0)
