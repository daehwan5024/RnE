import cv2

cap = cv2.VideoCapture(cv2.CAP_DSHOW+1)
cap2 = cv2.VideoCapture(cv2.CAP_DSHOW+2)

while(True):
    ret, frame = cap.read()    # Read 결과와 frame
    ret1, frame1 = cap2.read()

    if(ret and ret1) :

        cv2.imshow('frame_color', frame)    # 컬러 화면 출력
        cv2.imshow('frame_2', frame1)    # Gray 화면 출력
        if cv2.waitKey(1) == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()