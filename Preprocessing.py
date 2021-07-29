# loading the training/validation data
import zipfile
import wget
import os
import cv2
import random
import numpy as np
from hand_cropping import crop_hand_data

your_path = "/Users/bobo/Downloads/rock-paper-scissors-master/datasets/final"
database = []
chars = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7']
keys = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

for c in chars:
    for path in os.listdir(f'{your_path}/{c}'):
        if path == '.DS_Store':
            continue
        for img_path in os.listdir(f'{your_path}/{c}/{path}'):
            if img_path == '.DS_Store':
                continue
            image = cv2.imread(f'{your_path}/{c}/{path}/{img_path}')
            database.append((image, keys[int(path[1])])) 
            


"""c0 - rock
c1 - paper
c2 - scissors"""
total_images = len(database)

database_2, labels = crop_hand_data(database=database)

random.shuffle(database_2)  #generate two separate training and testing lists
train_split = 0.8
train_joints = []
train_labels = []
test_joints = []
test_labels = []

for i, joints in enumerate(database_2):
    if i > train_split*len(database_2):
        train_joints.append(joints)
        train_labels.append(labels[i])
    else:
        test_joints.append(joints)
        test_labels.append(labels[i])

save_path = "/Users/bobo/Downloads/CogWorks/RoshamBot/data"
np.save(f'{save_path}/train_joints', train_joints)
np.save(f'{save_path}/train_labels', train_labels)
np.save(f'{save_path}/test_joints', test_joints)
np.save(f'{save_path}/test_labels', test_labels)
np.save(f'{save_path}/database', database_2)
