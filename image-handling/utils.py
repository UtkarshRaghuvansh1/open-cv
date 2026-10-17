import cv2


def loadImage(path):
    """
    Load an image from the specified path.

    Parameters:
    path (str): The path to the image file.

    Returns:
    image: The loaded image.
    """
    image = cv2.imread(path)
    return image

def showImage(image, window_name='Image'):
    """
    Display the image in a window.

    Parameters:
    image: The image to be displayed.
    window_name (str): The name of the window.
    """
    print("Displaying image...")
    cv2.imshow(window_name, image)
    print("Press any key to close the image window.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def printImageInfo(image):
    """
    Print information about the image.

    Parameters:
    image: The image for which to print information.
    """
    if image is not None:
        print(f"Image shape: {image.shape}")
        print(f"width: {image.shape[1]}, height: {image.shape[0]}, channels: {image.shape[2] if len(image.shape) > 2 else 1}")
        print(f"Image data type: {image.dtype}")
        print(f"Image size (in bytes): {image.nbytes}")
        print("Image size in MB: {:.2f} MB".format(image.nbytes / (1024 * 1024)))
    else:
        print("No image data available.")