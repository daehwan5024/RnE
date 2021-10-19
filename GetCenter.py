import cv2
import numpy as np

class GetCenter:
    def __init__(self):
        self.lower_blue1 = np.array([95, 95, 95])
        self.upper_blue1 = np.array([105, 255, 255])
        self.lower_blue2 = np.array([85, 95, 95])
        self.upper_blue2 = np.array([95, 255, 255])
        self.lower_blue3 = np.array([85, 95, 95])
        self.upper_blue3 = np.array([95, 255, 255])


    def get_center(self, img, name):
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        img_mask1 = cv2.inRange(img_hsv, self.lower_blue1, self.upper_blue1)
        img_mask2 = cv2.inRange(img_hsv, self.lower_blue2, self.upper_blue2)
        img_mask3 = cv2.inRange(img_hsv, self.lower_blue3, self.upper_blue3)
        img_mask = img_mask1 | img_mask2 | img_mask3

        kernel = np.ones((11, 11), np.uint8)
        img_mask = cv2.morphologyEx(img_mask, cv2.MORPH_OPEN, kernel)
        img_mask = cv2.morphologyEx(img_mask, cv2.MORPH_CLOSE, kernel)

        # 마스크 이미지로 원본 이미지에서 범위값에 해당되는 영상 부분을 획득
        img_result = cv2.bitwise_and(img, img, mask=img_mask)

        numOfLabels, img_label, stats, centroids = cv2.connectedComponentsWithStats(img_mask)
        returnX = -1
        returnY = -1
        for idx, centroid in enumerate(centroids):
            if stats[idx][0] == 0 and stats[idx][1] == 0:
                continue

            if np.any(np.isnan(centroid)):
                continue

            x, y, width, height, area = stats[idx]
            centerX, centerY = int(centroid[0]), int(centroid[1])
            print(centerX, centerY)

            if area > 900:
                returnX = centerX
                returnY = centerY
                cv2.circle(img, (centerX, centerY), 10, (0, 0, 255), 10)
                cv2.rectangle(img, (x, y), (x + width, y + height), (0, 0, 255))

        cv2.imshow(name, img)
        cv2.imshow(name, img_mask)
        cv2.imshow(name, img_result)

        self.returnX = returnX
        self.returnY = returnY
        self.img = img
        self.mask = img_mask
        self.result = img_result

        return self.returnX, self.returnY