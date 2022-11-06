import cv2 as cv

# image
# img = cv.imread("photos/biebermessi.jpg")
# cv.imshow("FCBieber", img)
# cv.waitKey(0)

# video
capture = cv.VideoCapture("videos/enchanted.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF == ord("q"):
        break

capture.release()
cv.destroyAllWindows()
