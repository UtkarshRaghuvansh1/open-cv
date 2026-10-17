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

## 6. Grey Scale Conversion

- We can use cvtColor() function to change color of image

### Why in grey scale?

- Grey Scale image has less processing time
- It has less complexity

```py
grey = cv2.cvtColor(image_location, cv.COLOR_BGR2GRAY)
```

- COLOR_CVR2GRAY => converts color image to gray

---

---

---

---

# Advance Techniques

## Image Resizing and Scaling

### Resizing

- It changes the image's width and height
- Example -:

```txt
Original: 1200 × 1600
Resized:   600 × 800
```

- We use cv2.resize() function to resize the image

```py
resized = cv2.resize(src_img, dsize, fx,fy, interpolation)
```

- src_img ==> Image to be resized location
- dsize ==> New Size (width,height)

      - Important: OpenCV expects dimensions in this order:

#### Notes : Problem with resizing - distortion

Suppose the original image is:

```txt
1200 × 1600
```

Its aspect ratio is:

```txt
1200 ÷ 1600 = 0.75
```

If we resize it to 600 × 600, its new aspect ratio becomes:

```txt
600 ÷ 600 = 1
```

- The image will appear stretched or squeezed because its proportions changed.

### Scaling

- Instead of setting an exact size, use fx and fy:

```py
resized_image = cv2.resize(
    image,
    None,
    fx=0.5,
    fy=0.5
)
```

- fx is the horizontal scale factor.
- fy is the vertical scale factor.
- None tells OpenCV to calculate the dimensions.

### Reduce to 50%

```py
smaller_image = cv2.resize(
    image,
    None,
    fx=0.5,
    fy=0.5
)
```

### Calculation

```txt
New width  = 1200 × 0.5 = 600
New height = 1600 × 0.5 = 800
```

#### Using the same value for fx and fy preserves the aspect ratio.
