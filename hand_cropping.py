import cv2
import os
import mediapipe as mp
import numpy as np
from data_processing import resize_crop

def crop_hand_data(database, hand_num=1):
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(static_image_mode=True,
                        max_num_hands=hand_num,
                        min_detection_confidence=0.5)

    RGBimgs = np.array([image for image, _ in database])
    RGBlabels = np.array([label for _, label in database])

    # RGBimgs = np.array([resize_crop(cv2.flip(cv2.cvtColor(cv2.imread(f'{image_folder}/{file}'), cv2.COLOR_BGR2RGB),1)) for file in os.listdir(image_folder) if not 'DS_Store' in file])
    
    all_results = []
    for img in RGBimgs:
        results = hands.process(img)
        if not results.multi_hand_landmarks:
            continue
        # (#hands, #landmarks, 3)
        results_list = np.array([[[lm.x, lm.y, lm.z] for lm in hand_lms.landmark] for hand_lms in results.multi_hand_landmarks])
        all_results.append(results_list)

    return np.array(all_results), RGBlabels


