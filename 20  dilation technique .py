import cv2

# Read original color image
image = cv2.imread("sample.jpg")

# Create kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# Apply dilation directly on color image
dilated = cv2.dilate(image, kernel, iterations=1)

# Display
cv2.imshow("Original Color Image", image)
cv2.imshow("Dilated Color Image", dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()
