import cv2
import numpy as np 
img = cv2.imread("sample.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)   
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.convertScaleAbs(sobely) 
sobel = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
cv2.imshow("Original Image", img)
cv2.imshow("Sobel Edge Detection", sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()
