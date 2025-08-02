import cv2
import matplotlib.pyplot as plt
import numpy as np

# === 1. Load the original image ===
image = cv2.imread('voacanga.jpeg')

# Check if image is loaded successfully
if image is None:
    print("Error: Could not load image. Make sure 'photo.jpg' exists.")
    exit()

# === 2. Convert image to different color spaces ===
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# === 3. Save the converted images ===
cv2.imwrite('photo_grayscale.jpg', gray)
cv2.imwrite('photo_hsv.jpg', hsv)
cv2.imwrite('photo_lab.jpg', lab)

# === 4. Display the images ===

# Convert BGR to RGB for correct color display with matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
hsv_rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
lab_rgb = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)

plt.figure(figsize=(12, 8))

# Original Image
plt.subplot(2, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis('off')

# Grayscale
plt.subplot(2, 2, 2)
plt.imshow(gray, cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')

# HSV
plt.subplot(2, 2, 3)
plt.imshow(hsv_rgb)
plt.title("HSV Image")
plt.axis('off')

# LAB
plt.subplot(2, 2, 4)
plt.imshow(lab_rgb)
plt.title("LAB Image")
plt.axis('off')

plt.tight_layout()
plt.show()

# === 5. Plot histogram of grayscale image ===

plt.figure(figsize=(6, 4))
plt.hist(gray.ravel(), bins=256, range=(0, 256), color='gray')
plt.title('Histogram of Grayscale Image')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()
