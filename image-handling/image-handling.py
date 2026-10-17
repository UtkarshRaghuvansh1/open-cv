import cv2

# 1. load the image
image = cv2.imread('image-handling/test.jpg')

#2. check whether load is succesfull
if image is None:
    print("Error: Could not load image.")
else:
    print("Image loaded successfully.")
    
# 3. INspect  the image
height, width, channels = image.shape
print("Width:", width)
print("Height:", height)
print("Channels:", channels)
print("Data type:", image.dtype)
print("Total number of values:", image.size)

# 4. Display the image
cv2.imshow('Loaded Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()