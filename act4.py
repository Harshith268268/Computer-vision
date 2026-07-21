import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\nedam\Downloads\ChatGPT Image Jul 21, 2026, 01_29_34 PM.png",0)

noise = np.random.normal(0,25,img.shape).astype(np.uint8)
noisy = cv2.add(img,noise)

filtered = cv2.medianBlur(noisy,5)

plt.subplot(131)
plt.imshow(img,cmap='gray')
plt.title("Original")

plt.subplot(132)
plt.imshow(noisy,cmap='gray')
plt.title("Noisy")

plt.subplot(133)
plt.imshow(filtered,cmap='gray')
plt.title("Filtered")

plt.show()
