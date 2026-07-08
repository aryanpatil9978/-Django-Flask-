import cv2

img = cv2.imread('bird.png')

d = 7#diameter
sigmacolor = 50
sigmaspace = 50

b = cv2.bilateralFilter(img,d,sigmacolor,sigmaspace)

cv2.imshow("Bilateral Filter Image",b)
cv2.imshow("Original Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()