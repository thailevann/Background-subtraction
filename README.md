# **Background subtraction** 

Use background subtraction techniques to extract the foreground (desired object) and paste it onto a new background.

**Input:** Consists of 3 images: Original Background Image (Greenscreen), Target Background Image, and Object Image.

**Output:** A new image where the object is extracted from the Object Image and pasted onto the Target Background Image.

(a) Resize all 3 images to the same dimensions.

(b) Use background subtraction techniques with the Object Image and the Original Background Image to obtain the object mask.

(c) The object mask is a binary image (Foreground Mask) with two values: 0 for background and 1 for the regions containing the object.

(d) Create the output image by combining the Object Image and the Target Background Image based on the mask: where the mask pixel value is 1, use the value from the Object Image; where the mask pixel value is 0, use the value from the Target Background Image.


![image](https://github.com/user-attachments/assets/cf0a3546-cded-4b38-a772-c6026e527e8a)


