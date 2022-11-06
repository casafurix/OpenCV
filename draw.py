import cv2 as cv
import numpy as np

img = cv.imread("photos/biebermessi.jpg")
# cv.imshow("FCBieber", img)

blank = np.zeros((500, 500, 3), dtype="uint8")
cv.imshow("blank", blank)


# 1. paint the image a certain color
# blank[200:300, 300:400] = 0, 0, 255
# cv.imshow("red", blank)


# 2. draw a rectangle
cv.rectangle(
    img=blank,
    pt1=(0, 0),
    pt2=(blank.shape[1] // 2, blank.shape[0] // 2),
    color=(255, 255, 0),
    thickness=-1,
)
cv.imshow("rectangle", blank)


# 3. draw a circle
cv.circle(
    img=blank,
    center=(blank.shape[1] // 2, blank.shape[0] // 2),
    radius=30,
    color=(0, 255, 0),
    thickness=-1,
)
cv.imshow("circle", blank)


# 4. draw a line
cv.line(
    img=blank,
    pt1=(0, 0),
    pt2=(blank.shape[1] // 2, blank.shape[0] // 2),
    color=(255, 255, 255),
    thickness=2,
)
cv.imshow("line", blank)


# 5. write text on image
cv.putText(
    blank,
    text="Messi GOAT",
    org=(300, 240),
    fontFace=cv.FONT_HERSHEY_COMPLEX,
    fontScale=0.8,
    color=(0, 255, 0),
    thickness=2,
)
cv.imshow("text", blank)

cv.waitKey(0)
