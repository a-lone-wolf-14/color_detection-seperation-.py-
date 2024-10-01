import cv2
import numpy
from stack_function import stackImages

def color(path):
    def empty():
        pass

    img=cv2.imread(path)
    img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    cv2.namedWindow("TRACKBARS")

    cv2.createTrackbar("HUE MIN", "TRACKBARS", 0, 179, empty)
    cv2.createTrackbar("HUE MAX", "TRACKBARS", 179, 179, empty)
    cv2.createTrackbar("SAT MIN", "TRACKBARS", 0, 255, empty)
    cv2.createTrackbar("SAT MAX", "TRACKBARS", 255, 255, empty)
    cv2.createTrackbar("VAL MIN", "TRACKBARS", 0, 255, empty)
    cv2.createTrackbar("VAL MAX", "TRACKBARS", 255, 255, empty)

    while True:
        hue_min = cv2.getTrackbarPos("HUE MIN","TRACKBARS")
        hue_max = cv2.getTrackbarPos("HUE MAX", "TRACKBARS")
        sat_min = cv2.getTrackbarPos("SAT MIN", "TRACKBARS")
        sat_max = cv2.getTrackbarPos("SAT MAX", "TRACKBARS")
        val_min = cv2.getTrackbarPos("VAL MIN", "TRACKBARS")
        val_max = cv2.getTrackbarPos("VAL MAX", "TRACKBARS")

        low=numpy.array([hue_min,sat_min,val_min])
        up=numpy.array([hue_max,sat_max,val_max])

        mask=cv2.inRange(img_hsv,low,up)
        result=cv2.bitwise_and(img,img,mask=mask)

        stack=stackImages(0.5,[img,mask,result])

        cv2.imshow("STACK",stack)
        cv2.waitKey(1)

color(r'C:\Users\Suyash R\Documents\OpenCV\resources\sample6.jpeg')     #to insert the path of the image in the calling of 'color' function, use raw string format [color(r'path')]