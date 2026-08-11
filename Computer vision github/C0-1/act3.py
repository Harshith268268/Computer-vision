import cv2

# Image path
image_path = r"C:\Users\nedam\Downloads\ChatGPT Image Jul 21, 2026, 01_29_34 PM.png"

# Read image
img = cv2.imread(image_path)

# Resize original image for display
original_display = cv2.resize(img, (500, 500))

# Apply Gaussian Blur (reduces aliasing)
blurred = cv2.GaussianBlur(img, (5, 5), 0)

# Resize the blurred image
corrected = cv2.resize(blurred, (300, 300), interpolation=cv2.INTER_LINEAR)

# Resize for display
corrected_display = cv2.resize(corrected, (500, 500))

# Display images
cv2.imshow("Original Image", original_display)
cv2.imshow("Corrected Image", corrected_display)

cv2.waitKey(0)
cv2.destroyAllWindows()
