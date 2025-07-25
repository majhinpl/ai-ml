import cv2 as cv

#Loading and Displaying the image
img = cv.imread(r"I:\MAJHINpl\development\ai-ml\images\NEPSE1D250625.PNG")
resized = cv.resize(img, (800, 700))
cv.imshow("Image", resized)

# Average Blurring
# avg_blur = cv.blur(resized, (5,5))
# cv.imshow("Agerage Blur", avg_blur)

# Median Blurring
# Median_blur = cv.medianBlur(resized, 5)
# cv.imshow("Median Blur", Median_blur)

#Gaussian Blur

# Gauss_Blur = cv.GaussianBlur(resized, (7,7), 9)
# cv.imshow("G_Blur", Gauss_Blur)
#Bilateral Blur
bilateral = cv.bilateralFilter(resized, 15, 20, 20)
cv.imshow("Bilateral_Blur", bilateral)