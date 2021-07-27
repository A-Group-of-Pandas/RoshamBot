import pytorch
import cv2
from hand_cropping import crop_hand

img = crop_hand()

cv2.imwrite('image.jpg', img)
