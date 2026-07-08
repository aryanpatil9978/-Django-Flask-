import cv2

img = cv2.imread("resized_Kunfu_Panda.png")

flipped_img_hor = cv2.flip(img, 1)#flipped horizontal
flipped_img_ver = cv2.flip(img, 0)#flipped vertically
flipped_img_both =cv2.flip(img, -1) #flipped horizont ally and vertically

cv2.imshow('Original Image', img)
cv2.imshow("flipped vertically", flipped_img_ver)
cv2.imshow("flipped horizontally", flipped_img_hor)
cv2.imshow("Horizontal and Vertical flipped",flipped_img_both)

cv2.waitKey(0)
cv2.destroyAllWindows()

