import cv2

# Load an image from file
image = cv2.imread('example.jpeg')

# Display the image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
