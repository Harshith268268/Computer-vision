import cv2

# Image path
image_path = r"C:\Users\nedam\Downloads\ChatGPT Image Jul 21, 2026, 01_29_34 PM.png"

# Read image in grayscale
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Resize original image for display
original_display = cv2.resize(img, (500, 500))

# Reduce pixel resolution
low_pixel = cv2.resize(img, (128, 128))
low_pixel_display = cv2.resize(low_pixel, (500, 500), interpolation=cv2.INTER_NEAREST)

# Reduce intensity resolution (8-bit to 4-bit)
low_intensity = (img // 16) * 16
low_intensity_display = cv2.resize(low_intensity, (500, 500))

# Display images
cv2.imshow("Original Image", original_display)
cv2.imshow("Low Pixel Resolution", low_pixel_display)
cv2.imshow("Low Intensity Resolution", low_intensity_display)

cv2.waitKey(0)
cv2.destroyAllWindows()
