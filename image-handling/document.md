# Open CV basics and image handling

## Project

- load the image
- convert to grayscale
- save image

## Basic Terms

1. Image - 2d grid (matrix) of pixels
2. Pixel - :
   - smallest individual unit of image
   - each pixel defines small pat of the image
   - if image is colored, pixels hold 3 values (red, green, blue)
3. Width and Height
   - Width : total number of pixels left to right (horizontally)
   - Hight : total number of pixels vertically

4. Color Channel - It store information about 1 color component, A typical color image has red green blue channels.
5. Image format - how the image data is stored
   - .jpg => smaller files, some quality is lossed
   - .png => Loassless and supoorts transparency
   - .bmp => large and minimal. compressed

## Installation

```bash
python -m pip install opencv-python
```

- Verify Installation

```py
import cv2

print(cv2.__version__)
```

## 1. How to read/load the image

- Using imread() function provided by open cv we can read/load the image
- cv2.imread() reads the file and converts it into a NumPy array.

```txt
[
  [[Blue, Green, Red], [Blue, Green, Red], ...],
  [[Blue, Green, Red], [Blue, Green, Red], ...],
  ...
]
```

- Unlike many other libraries, OpenCV uses BGR, not RGB:

```txt
Channel 0 → Blue
Channel 1 → Green
Channel 2 → Red
```

```py
image = cv2.imread('filename.jpg', flag)
/*
flag = 1 --> color image
flag = 0 --> grey scale image
flag = -1 --> unchanged image
*/
```

## 2. Check image is loaded

```py
if image is None:
   print('Error Loading the image')
else:
   print('Image loaded successfully!!')
```

## 3. Inspect the Image

```py
height, width, channels = image.shape
print("Width:", width)
print("Height:", height)
print("Channels:", channels)
print("Data type:", image.dtype)
print("Total number of values:", image.size)
```

- width 1200
- height 1600
- channels 3 --> Each pixel will contains 3 values (R, G, B)
  size = 1200 x 1600 x 3 = 5760000

## 4. Display the Image

- To display the image we have 3 functions -:
  - imshow() - creates a window to see the image
  - waitkey(0) - waits until user press any key on the keyboard
  - Without waitKey(), the program may terminate before you can see the image.
  - destroyAllWindows() - close all windows

```py
cv2.imread("Image Showing", image)
cv.waitKey(0)
cv2.destroyAllWindows()
```

## 5. Saving the Image

- We use imwrite() function to save the image

```py
cv2.imwrite('output.jpg', image)
```
