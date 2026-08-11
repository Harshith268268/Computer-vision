import cv2

# Image path
image_path = r"C:\Users\nedam\Downloads\ChatGPT Image Jul 21, 2026, 01_29_34 PM.png"

# Read image in grayscale
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Enhance brightness and contrast
enhanced = cv2.equalizeHist(img)

# Resize both images for display
original_display = cv2.resize(img, (500, 500))
enhanced_display = cv2.resize(enhanced, (500, 500))

# Display
cv2.imshow("Original Image", original_display)
cv2.imshow("Enhanced Image", enhanced_display)

cv2.waitKey(0)
cv2.destroyAllWindows()
