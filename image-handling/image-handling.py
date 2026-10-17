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

# 5. Convert the image to grayscale
image2 = cv2.imread('image-handling/photo.png')
gray_image = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
if gray_image is not None:
    print("Grayscale image created successfully.")
    cv2.imshow('Grayscale Image', gray_image)
    cv2.waitKey(0)
    cv2.imwrite('image-handling/gray_photo.png', gray_image)
    cv2.destroyAllWindows()
else:
    print("Error: Could not convert image to grayscale.")
    
## Assignment 
# load the image 
user_input_location = input(
"Please enter the path of the image you want to load: "
).strip()

if not user_input_location:
    print("Error: No path provided.")
    
img = cv2.imread(user_input_location)
# convert to greyscale
if img is None:
    print("Error: Could not load image from the provided path.")
    
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# show the image 
if gray_img is not None:
    print("Grayscale image created successfully.")
    cv2.imshow('Grayscale Image', gray_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# save the image to disk, ask user to provide location to save
user_save_location = input("Please enter the path where you want to save the grayscale image: ").strip()

if not user_save_location:
    print("Error: No save path provided.")
else:
    cv2.imwrite(user_save_location, gray_img)
    print("Grayscale image saved successfully.")