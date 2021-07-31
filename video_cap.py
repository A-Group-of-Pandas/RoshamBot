import cv2
import numpy as np
import torch
from Model import RecogJoint
from hand_cropping import crop_hand_joint
from data_processing import normalize_joints
import time
import mediapipe as mp
from collections import Counter

def videoCap(dur: float=5.):
    model = RecogJoint()
    model.load_state_dict(torch.load('recogn_joint',map_location=torch.device('cpu')))
    model.eval()
    st = time.time()
    keys = ['paper', 'scissors', 'rock']
    print("Make your choice! Recording for " + str(int(dur)) + " seconds...")
    with torch.no_grad():
        cap = cv2.VideoCapture(0)
        texts = []
        pred_scores = []
        hands = mp.solutions.hands.Hands(static_image_mode=False,
                        max_num_hands=1,
                        min_detection_confidence=0.5,
                        min_tracking_confidence=0.45)
        while True:
            def detect(texts,pred_scores,cap,model):
                suc, img = cap.read()
                if suc is None:
                    time.sleep(0.01)
                    return -1
                results = crop_hand_joint(img,hands)
                if results is None:
                    texts.append(' ')
                    pred_scores.append(0)
                    time.sleep(0.01)
                    return -1
                results = normalize_joints(results)
                preds = model(torch.flatten(torch.tensor(results).to('cpu'),start_dim=1)).detach().numpy()[0]
                # N, 3
                pred_scores.append(np.max(preds))
                guess = keys[np.argmax(preds)]
                texts.append(guess)
                #print(guess)
                cv2.imshow('image',img)
            if detect(texts,pred_scores,cap,model) == -1:
                continue
            if cv2.waitKey(1) & 0xFF == ord('q') or time.time() > st + dur:
                cv2.destroyAllWindows()
                break
        pred_scores = np.stack(pred_scores,axis=0)
        return Counter(texts).most_common(1)[0][0]

# result = videoCap()
# print("You played:", result)