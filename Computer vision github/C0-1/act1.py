import cv2

# Image path
image_path = r"C:\Users\nedam\Downloads\ChatGPT Image Jul 21, 2026, 01_29_34 PM.png"

# Read image
img = cv2.imread(image_path)

# Resize original image for display
original_display = cv2.resize(img, (500, 500))

# Resize image (simulating processed image)
resized = cv2.resize(img, (300, 300))
resized_display = cv2.resize(resized, (500, 500))

# Display both images with the same window size
cv2.imshow("Original Image", original_display)
cv2.imshow("Resized Image", resized_display)

cv2.waitKey(0)
cv2.destroyAllWindows()
