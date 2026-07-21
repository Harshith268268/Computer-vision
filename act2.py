import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\nedam\Downloads\ChatGPT Image Jul 21, 2026, 01_29_34 PM.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

small = cv2.resize(img, (50,50), interpolation=cv2.INTER_NEAREST)
alias = cv2.resize(small, (500,500), interpolation=cv2.INTER_NEAREST)

plt.imshow(alias)
plt.title("Aliasing Effect")
plt.axis("off")
plt.show()
