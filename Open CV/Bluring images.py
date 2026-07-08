import cv2

img = cv2.imread("resized_Kunfu_Panda.png")

#kernel size for x and y
Gaus_ksize =(7,7)
#kernel size for only one direction is also enough
Median_ksize = 3



#only required for Gaussian blur:
#Standard Deviaton in the x and y direction
sigma_x = 0 # if sigma x is given then sigma y is automatically equal to sigma x unless specifically mentioned
sigma_y = 0 # And if both sigma x and sigma y are zero then they are calculated from the kernel size


#Gaussian Blur
Gaus_blur = cv2.GaussianBlur(img,Gaus_ksize,sigma_x)
#Median Blur
Median_blur = cv2.medianBlur(img,Median_ksize)

cv2.imshow("Original Image",img)
cv2.imshow("Gaussian Blur",Gaus_blur)
cv2.imshow("Median Blur",Median_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()