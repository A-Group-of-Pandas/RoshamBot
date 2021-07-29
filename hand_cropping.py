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
                        min_detection_confidence=0.05)
    # minimum detection confidence is the interval that detects your hands to a certain degree. 
    #creates an array of RGB images.
    RGBimgs = np.array([image for image, _ in database])
    print("RGBimg shape:", RGBimgs.shape)
    #creates an array of RGB labels
    RGBlabels = np.array([label for _, label in database])
    print("RGBlabels shape:", RGBlabels.shape)
    
    all_results = []
    for img in RGBimgs:
        # making the collection of images.
        # creates landmarks with xs on the image
        results = hands.process(img)
        if not results.multi_hand_landmarks:
            # if (random.randint(0, 100) < 1):
            #     plt.imshow(img)
            #     plt.show()
            continue
        # (#hands, #landmarks, 3)
        # if (random.randint(0, 100) < 1):
        #         plt.imshow(img)
        #         plt.show()
        results_list = np.array([[[lm.x, lm.y, lm.z] for lm in hand_lms.landmark] for hand_lms in results.multi_hand_landmarks])
        all_results.append(results_list)
        
    all_results = np.array(all_results)
    all_results = all_results.reshape((-1, 21, 3))
    print("all results shape:", all_results.shape)
    return all_results, RGBlabels

