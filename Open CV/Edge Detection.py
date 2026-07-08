import cv2
import numpy as np

img = cv2.imread("bird.png")
#everything above the max_threshold value is converted to White Pixel
#everything below the min_threshold value is converted to Black Pixel
min_threshold = 100
max_threshold = 200
edges = cv2.Canny(img,min_threshold,max_threshold)

cv2.imshow("Original",img)
cv2.imshow("Edge Detetion Image",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()