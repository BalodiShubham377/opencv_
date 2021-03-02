import cv2 as cv 
img  = cv.imread("20210208_155225.jpg")
cv.imshow("20210208_155225.jpg",img)

#Averaging
average = cv.blur(img , (3,3))
cv.imshow("Average blur", average)

# Gaussion
gauss = cv.GaussianBlur(img , (3,3) , 0)
cv.imshow("Gaussion blur", gauss)

# median blur
median = cv.medianBlur(img , 3)
cv.imshow("Median", median)

# Bilateral blur
bilateral = cv.bilateralFilter(img , 10 , 35 , 25)
# 5--> diameter , sigmacolour -->  , sigmapace -->

cv.imshow("Bilteral ", bilateral)

cv.waitKey(0)