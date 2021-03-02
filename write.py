import cv2 as cv
import numpy as np
blank = np.zeros((500 ,500, 3), dtype='uint8')
cv.imshow('blank', blank)
cv.waitKey(0)
cv.putText(blank, 'hello there ', (225,250), cv.FONT_HERSHEY_PLAIN, 1.0 , (0,250,0), 2)
cv.imshow("text", blank)
cv.waitKey(0)