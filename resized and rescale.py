import cv2 as cv
img = cv.imread("20210121_180005.jpg")
def rescaleFrame(Frame, scale = .05):
    width = int(Frame.shape[1]*scale)
    hight = int(Frame.shape[0]*scale)

    dimension =(width,hight)
    return cv.resize(Frame, dimension , interpolation= cv.INTER_AREA)
resized_image = rescaleFrame(img)
cv.imshow('image',resized_image)
cv.waitKey(0)