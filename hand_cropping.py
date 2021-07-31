import cv2
import os
import mediapipe as mp
import numpy as np
import matplotlib.pyplot as plt
import random

def crop_hand_data(database, hand_num=1):
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(static_image_mode=True,
                        max_num_hands=hand_num,
                        min_detection_confidence=0.5)
    # minimum detection confidence is the interval that detects your hands to a certain degree. 
    #creates an array of RGB images.
    images = np.array([image for image, _ in database])
    print("RGBimg shape:", images.shape)
    #creates an array of RGB labels
    labels = np.array([label for _, label in database])
    print("RGBlabels shape:", labels.shape)
    
    all_results = []
    for img in images:
        img = cv2.resize(img, (60, 60))
        img = cv2.flip(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 1)
        # image processing
        results = hands.process(img)
        # processes landmarks
        if not results.multi_hand_landmarks:
            continue
        results_list = np.array([[[lm.x, lm.y, lm.z] for lm in hand_lms.landmark] for hand_lms in results.multi_hand_landmarks])
        all_results.append(results_list)
        
    all_results = np.array(all_results)
    all_results = all_results.reshape((-1, 21, 3))
    print("all results shape:", all_results.shape)
    return all_results, labels, images

def crop_hand_joint(img, hands):
    # margin gives some space between the tips of fingers and the bounding box (bbox) measured in pixels
    # plays recording from camera and processes each image
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if not results.multi_hand_landmarks:
        return None
    results = np.array([[[lm.x, lm.y, lm.z] for lm in hand_lms.landmark] for hand_lms in results.multi_hand_landmarks])
    del imgRGB, img
    return results[None,...].astype(np.float32)

