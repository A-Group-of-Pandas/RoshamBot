import numpy as np
import cv2

#DATA PROCESSING
def read_data(data_name : str, label_name : str, path:str = "data"):
    # reads in data from the dataset
    # load the data and the labels.
    data = np.load(f'{path}/{data_name}.npy')
    labels = np.load(f'{path}/{label_name}.npy')
    # separates the data into training data/labels and returns them
    #print("data shape: ", data.shape)
    # print(data.min(axis=0), data.max(axis=0), data.mean(axis=0), data.std(axis=0))
    return data, labels

def read_batch(batch_size : int = 32, train : bool = True, joints : bool = True):
    if joints:
        if train:
            #reads the training and labels data
            total_x, total_y = read_data('train_joints','train_labels')
            #print("total x shape train: ", total_x.shape)
        else:
            #reads the testing data if not in training.
            total_x, total_y = read_data('test_joints','test_labels')
            #print("total x shape test: ", total_x.shape)
    # else:
    #     if train:
    #         total_x, total_y = read_data('images','labels')
    #     else:
    #         total_x, total_y = read_data('test_images','test_labels')

    #training with the batch indices.
    indices = np.arange(len(total_y))
    np.random.shuffle(indices)
    for batch_i in range(len(total_y)//batch_size):
        idx = indices[batch_i*batch_size : (batch_i+1)*batch_size]
        if joints:
            yield total_x[idx], total_y[idx]
        # else:
        #     yield normalize(total_x[idx]), total_y[idx]
    # yields a generator for batches of data

#====================================================================================
# DATA AUGMENTATION

def normalize_joints(total_x):
    total_x = total_x - total_x[:, :, :1,:]
    # factor = np.mean(np.linalg.norm(total_x-total_x[:,0:1,:],axis=-1,keepdims=True),axis=-2,keepdims=True)
    # if (factor != 0).all():
    #     total_x /= factor
    return total_x

def random_rotation(total_x):
    rand_a = np.random.uniform(-1,1)*np.pi/20
    rand_b = np.random.uniform(-1,1)*np.pi/20
    rand_c = np.random.uniform(-1,1)*np.pi/3
    rotA = np.array([[1,0,0],[0,np.cos(rand_a),-np.sin(rand_a)],[0,np.sin(rand_a),np.cos(rand_a)]])
    rotB = np.array([[np.cos(rand_b),0,np.sin(rand_b)],[0,1,0],[-np.sin(rand_b),0,np.cos(rand_b)]])
    rotC = np.array([[np.cos(rand_c),-np.sin(rand_c),0],[np.sin(rand_c),np.cos(rand_c),0],[0,0,1]])
    return total_x @ rotA @ rotB @ rotC

def random_scale(total_x):
    rand_scale = np.random.uniform(0.7,1.4)
    return total_x * rand_scale

def random_flip(total_x):
    if np.random.randint(0,2) == 0:
        return -total_x
    else:
        return total_x

def data_augmentation(total_x):
    # (N,1,21,3)
    # total_x = random_rotation(total_x)
    total_x = random_scale(total_x)
    total_x = random_flip(total_x)
    return total_x

#====================================================================================