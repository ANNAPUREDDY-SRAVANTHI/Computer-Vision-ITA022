import cv2
import numpy as np 
img = cv2.imread("sample.jpg")
orig = img.copy() 
roi = img[50:113, 100:126] 
x, y = 50, 200 
h, w = img.shape[:2]
th = min(roi.shape[0], h - y)
tw = min(roi.shape[1], w - x) 
img[y:y+th, x:x+tw] = roi[:th, :tw] 
cv2.imshow("Original Image", orig)
cv2.imshow("ROI Cropped & Pasted", img)
cv2.imwrite("roi_image.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
