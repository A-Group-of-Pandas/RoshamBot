import torch
from torch import nn

class SignRecogJoint(nn.Module):
    def __init__(self):
        super(SignRecogJoint, self).__init__()
        self.dense1 = nn.Linear(63,128)
        self.batch_norm1 = nn.BatchNorm1d(128)
        self.dense2 = nn.Linear(128,128)
        self.batch_norm2 = nn.BatchNorm1d(128)
        self.dense3 = nn.Linear(128,128)
        self.batch_norm3 = nn.BatchNorm1d(128)
        self.dense4 = nn.Linear(128,3)
        self.relu = nn.ReLU()

    def forward(self,x):
        x = self.batch_norm1(self.relu(self.dense1(x)))
        x = self.batch_norm2(self.relu(self.dense2(x)))
        x = self.batch_norm3(self.relu(self.dense3(x)))
        return self.dense4(x)

path_images = r'C:\Dev\Tools\Python\condabin\SiLT Project\rock-paper-scissors-master\datasets\final\data\images'
path_labels = r'C:\Dev\Tools\Python\condabin\SiLT Project\rock-paper-scissors-master\datasets\final\data\labels'