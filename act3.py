import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\nedam\Downloads\ChatGPT Image Jul 21, 2026, 01_29_34 PM.png",0)

# Reduce gray levels
quantized = (img//64)*64

plt.imshow(quantized,cmap='gray')
plt.title("Quantized Image")
plt.axis("off")
plt.show()
