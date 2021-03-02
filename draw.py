import cv2 as cv
import numpy as np
blank = np.zeros((500, 500 ,3), dtype='uint8')
cv.imshow('blank ', blank)


 #draw rectangle
#cv.rectangle(blank, (0,0),(250,250),(0, 255, 0), thickness=4)
cv.rectangle(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2),(0,255,0),thickness=-3)
cv.imshow('rectangle', blank)
cv.waitKey(0)


# drawcircle
#cv.circle(blank, (0,0),(250,250),(0, 255, 0,40) ,thickness=-1)
cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2),40,(0,0,250),thickness=-1)
cv.imshow('circle', blank)
cv.waitKey(0)


#draw line


cv.line(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2),(255,255,6),thickness=2)
cv.imshow('line', blank)
cv.waitKey(0)

