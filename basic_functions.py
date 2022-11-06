import cv2 as cv

img = cv.imread("photos/biebermessi.jpg")
cv.imshow("FCBieber", img)


# 1. converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# 2. blurring
blur = cv.GaussianBlur(img, (69, 69), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

# 3. edge cascade
canny = cv.Canny(img, threshold1=125, threshold2=175)
cv.imshow("canny", canny)

# 4. dilating image
dilated = cv.dilate(canny, kernel=(7, 7), iterations=3)
cv.imshow("dilated", dilated)

# 5. eroding image, for getting back edge cascade for diluted images
eroded = cv.erode(dilated, kernel=(7, 7), iterations=3)
cv.imshow("eroded", eroded)

# 6. resize
resized = cv.resize(img, dsize=(500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("resized", resized)

# 7. crop
cropped = img[50:200, 200:400]
cv.imshow("cropped", cropped)

cv.waitKey(0)
