import cv2 as cv


def rescale_frame(frame, scale=0.75):
    # image, video, live video
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def change_res(capture, width, height):
    # live video only
    capture.set(3, width)
    capture.set(4, height)


# resized image
image = cv.imread("photos/biebermessi.jpg")
resized_image = rescale_frame(image)

cv.imshow("image", image)
cv.imshow("resized image", resized_image)
cv.waitKey(0)


# resized video
capture = cv.VideoCapture("videos/enchanted.mp4")

while True:
    isTrue, frame = capture.read()

    # resized frame
    frame_resized = rescale_frame(frame)

    cv.imshow("video", frame)
    cv.imshow("resized video", frame_resized)

    if cv.waitKey(20) & 0xFF == ord("q"):
        break

capture.release()
cv.destroyAllWindows()
