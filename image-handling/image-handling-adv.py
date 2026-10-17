import cv2
from utils import loadImage, showImage, printImageInfo

path = 'image-handling/photo.png'
# Load image
img = loadImage(path)

# Check if the image was loaded successfully
if img is None:
    print("Error: Could not load image.")
else:
    print("Image loaded successfully.") 
    
# Show the image 
showImage(img, 'Loaded Image')

# Resize the image 
resized_img = cv2.resize(img, (300, 300))
showImage(resized_img, 'Resized Image')
print("***********Original image info ***********")
printImageInfo(img)
print("**************Resized image info **************")
printImageInfo(resized_img)

# Scale the image by a factor of 0.5
scaled_img = cv2.resize(img, None, fx=0.2, fy=0.2 )
print("**************Scaled image info **************")
showImage(scaled_img, 'Scaled Image')
printImageInfo(scaled_img)