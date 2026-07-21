import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\nedam\Downloads\ChatGPT Image Jul 21, 2026, 01_29_34 PM.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Reduce resolution
small = cv2.resize(img, (100,100))

# Increase again
blurred = cv2.resize(small, (img.shape[1], img.shape[0]))

plt.imshow(blurred)
plt.title("Blurred due to Low Sampling")
plt.axis("off")
plt.show()
