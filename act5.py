import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\nedam\Downloads\ChatGPT Image Jul 21, 2026, 01_29_34 PM.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

low = cv2.resize(img,(100,100))
high = cv2.resize(img,(600,600))

plt.subplot(121)
plt.imshow(low)
plt.title("Low Resolution")

plt.subplot(122)
plt.imshow(high)
plt.title("High Resolution")

plt.show()
