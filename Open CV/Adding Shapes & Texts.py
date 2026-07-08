import cv2
import numpy as np

#img = cv2.imread("E:/Python/Python Projects/Web Scraping/test.png",cv2.IMREAD_COLOR)
#you can just write 1 instead of IMREAD_COLOR

#creating a Blank Image:
img = np.zeros(shape=[600,800,3],dtype='uint8')
#img.fill(255)   #use this to conver the the image into white

# img , start_point , end_point , color , thickness
cv2.line(img,(0,0),(150,150),(255,0,0),2)

# img , top_left_corner_point , bottom_right_corner_point , color , thickness
cv2.rectangle(img,(200,150),(250,300),(0,225,0),3)

# img , center , radius, color, thickness
cv2.circle(img,(380,70),70,(0,0,255),4)

#defining the points for a polygen
pts_polygen = np.array([[100,50],[100,300],[500,50],[500,300]], np.int32)
#isClosed : True it will just join all the four point and will be a closed figure not a open figure
cv2.polylines(img,[pts_polygen],True,(0,0,255),1)


font = cv2.FONT_HERSHEY_SIMPLEX #Select a Font
# img , "Text" , coordinates , font , font_scale , color , thickness , Type_of_Line
cv2.putText(img, 'Hello World!', (100, 400), font, 3, (200,150,255), 8, cv2.LINE_AA)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()