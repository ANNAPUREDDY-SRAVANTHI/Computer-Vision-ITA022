import cv2
import numpy as np
size = int(input("Enter image size: ")) 
img = np.ones((size, size, 3), np.uint8) * 255 
center = (size//2, size//2)
radius = size//4 
cv2.circle(img, center, radius, (0, 0, 255), 3)
cv2.imshow("Circle Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
