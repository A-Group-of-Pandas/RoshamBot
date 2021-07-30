from Model import RecogJoint
import torch

model = RecogJoint()
model.load_state_dict(torch.load('recogn_joint',map_location=torch.device('cpu')))
model.eval()
image = 0 # whatever image is taken from the rock paper scissors
pred = model(image)
