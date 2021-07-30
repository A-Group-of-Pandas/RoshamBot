# loading the training/validation data

import os
import cv2
import random
import numpy as np
from hand_cropping import crop_hand_data
import matplotlib.pyplot as plt

your_path = "data"
database = []
chars = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7']

# we can process the databse in this way.
for c in chars:
    for path in os.listdir(f'{your_path}/{c}'):
        if path == '.DS_Store':
            continue
        for img_path in os.listdir(f'{your_path}/{c}/{path}'):
            if img_path == '.DS_Store':
                continue
            image = cv2.imread(f'{your_path}/{c}/{path}/{img_path}')
            database.append((image, int(path[1]))) 
            
"""c0 - rock
c1 - paper
c2 - scissors"""
total_images = len(database)

print("database length: ", end="")

database_2, labels, images = crop_hand_data(database=database)
zipped = list(zip(database_2, labels, images))

# print("database 2 shape: ", end="")
# print(database_2.shape)
random.shuffle(zipped)  #generate two separate training and testing lists
database_2, labels, images = zip(*zipped)
train_split = 0.8
train_joints = []
train_labels = []
test_joints = []
test_labels = []

keys = ["rock", 'paper', 'scissors']
counter = [0]*3
for i, joints in enumerate(database_2):
    if i < train_split*len(database_2):
        # if i % 100 == 0:
        #     plt.imshow(images[i])
        #     plt.show()
        #     print(keys[labels[i]])
        train_joints.append(joints)
        train_labels.append(labels[i])
        counter[labels[i]]+=1
    else:
        test_joints.append(joints)
        test_labels.append(labels[i])
        counter[labels[i]]+=1

idx = [np.random.randint(0,len(train_labels)) for i in range(15)]
for i in idx:
    print(train_joints[i].shape)
    plt.scatter(train_joints[i][:,0],train_joints[i][:,1])
    plt.show()
    print(train_labels[i])

print(counter)
save_path = "data"
np.save(f'{save_path}/train_joints', train_joints)
np.save(f'{save_path}/train_labels', train_labels)
np.save(f'{save_path}/test_joints', test_joints)
np.save(f'{save_path}/test_labels', test_labels)
np.save(f'{save_path}/database', database_2)
