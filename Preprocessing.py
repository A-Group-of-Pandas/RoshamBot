# loading the training/validation data
import zipfile
import wget
import os
import cv2
import random
import numpy as np

your_path = "C:\Dev\\Tools\\Python\\condabin\SiLT Project\\rock-paper-scissors-master\\datasets\\final"
database = []
chars = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7']
keys = ['rock', 'paper', 'scissors']

for c in chars:
    for path in os.listdir(f'{your_path}\\{c}'):
        if path == '.DS_Store':
            continue
        for img_path in os.listdir(f'{your_path}\\{c}\\{path}'):
            if img_path == '.DS_Store':
                continue
            image = cv2.imread(f'{your_path}\\{c}\\{path}\\{img_path}')
            database.append((image, keys[int(path[1])])) 
            # scales/pads the images so that they're all shape (100, 100, 3):
            #image = resize_crop(image)

"""c0 - rock
c1 - paper
c2 - scissors"""
total_images = len(database)

random.shuffle(database) 
images = [i for i in database]
labels = [l for l in database] #generate two separate training and testing lists
train_split = 0.8
image_train = []
label_train = []
image_test = []
label_test = []

for i, (img, lab) in enumerate(database):
    if i > train_split*len(database):
        image_train.append(img)
        label_train.append(lab)
    else:
        image_test.append(img)
        label_test.append(lab)

np.save(f'{your_path}\\data\\images', image_train)
np.save(f'{your_path}\\data\\labels', label_train)
np.save(f'{your_path}\\data\\test_images', image_test)
np.save(f'{your_path}\\data\\test_labels', label_test)