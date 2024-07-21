#background substraction để trích xuất forgeground (object mong muốn) và dán vào background mới.
#input: Original Background Image (Greenscreen), Target Background Image và Object Image.
#output: Ảnh mới khi trích xuất object từ Object Image và dán vào Target Back-ground Image.

import numpy as np
import cv2
import matplotlib.pyplot as plt

bg1_image = cv2.imread("./image/GreenBackground.png",1)
bg1_image = cv2.resize(bg1_image, (678, 678))

ob_image = cv2.imread("./image/Object.png",1)
ob_image = cv2.resize(ob_image, (678, 678))

bg2_image = cv2.imread("./image/NewBackground.jpg", 1)
bg2_image = cv2.resize(bg2_image, (678, 678))
def show_img(img, title = ""):
    plt.imshow(difference_single_channel, cmap='gray')
    plt.colorbar()
    plt.title(title)
    plt.show()
def compute_difference(bg_img, input_img):
    difference_single_channel = np.abs(bg_img - input_img)
    return difference_single_channel
difference_single_channel = compute_difference ( bg1_image , ob_image )
#show_img(difference_single_channel)

def compute_binary_mask(difference_single_channel, threshold = 0):
    difference_binary = (difference_single_channel > threshold).astype(np.uint8)
    return difference_binary
binary_mask = compute_binary_mask(difference_single_channel)
show_img(binary_mask)

def replace_background(bg1_image, bg2_image, ob_image):
    difference_single_channel = compute_difference(bg1_image, ob_image)
    binary_mask = compute_binary_mask(difference_single_channel)
    output = np.where(binary_mask == 255, ob_image, bg2_image)
    return output
output = replace_background(bg1_image, bg2_image, ob_image)
show_img(output)