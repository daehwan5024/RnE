import cv2 as cv
import numpy as np
from GetCenter import GetCenter

hsv = 95
lower_blue1 = np.array([95, 95, 95])
upper_blue1 = np.array([105, 255, 255])
lower_blue2 = np.array([85, 95, 95])
upper_blue2 = np.array([95, 255, 255])
lower_blue3 = np.array([85, 95, 95])
upper_blue3 = np.array([95, 255, 255])


cap = cv.VideoCapture(cv.CAP_DSHOW+1)
print("1번 카메라 : 가로 : {} 세로 : {}".format(cap.get(cv.CAP_PROP_FRAME_WIDTH), cap.get(cv.CAP_PROP_FRAME_HEIGHT)))

cap2 = cv.VideoCapture(cv.CAP_DSHOW+2)
print("2번 카메라 : 가로 : {} 세로 : {}".format(cap.get(cv.CAP_PROP_FRAME_WIDTH), cap.get(cv.CAP_PROP_FRAME_HEIGHT)))

while (True):
    ret, img = cap.read()
    if (cv.waitKey(1) & 0xff) == 27:
        break
    GetCenter Get1 = GetCenter()
    GetCenter

    x, y = GetCenter(img)
cap.release()
cv.destroyAllWindows()
