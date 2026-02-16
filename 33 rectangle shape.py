import cv2
import numpy as np
size = int(input("Enter image size: ")) 
img = np.ones((size, size, 3), np.uint8) * 255
cv2.rectangle(img, (50, 50), (size-50, size-50), (0, 0, 255), 3)
cv2.imshow("Rectangle Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
