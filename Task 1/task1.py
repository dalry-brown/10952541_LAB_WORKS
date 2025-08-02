import cv2
import matplotlib.pyplot as plt

# Load the original image
image = cv2.imread('voacanga.jpeg')

# Check if image is loaded successfully
if image is None:
    print("Error: Could not load image. Make sure 'photo.jpg' exists.")
    exit()

# Convert image from BGR (OpenCV default) to RGB for correct color display
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert the original image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Save the grayscale image to disk
cv2.imwrite('photo_gray.jpg', gray_image)

# Display original and grayscale images side by side
plt.figure(figsize=(10, 4))

# Show original image
plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title('Original Image')
plt.axis('off')

# Show grayscale image
plt.subplot(1, 2, 2)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

# Display the images
plt.tight_layout()
plt.show()
