import numpy as np
import cv2

#DATA PROCESSING
def read_data(data_name : str, label_name : str, path:str = "/Users/bobo/Downloads/CogWorks/RoshamBot/data"):
    # reads in data from the dataset
    # load the data and the labels.
    data = np.load(f'{path}/{data_name}.npy')
    labels = np.load(f'{path}/{label_name}.npy')
    # separates the data into training data/labels and returns them
    print("data shape: ", end="")
    print(data.shape)
    return data, labels

def read_batch(batch_size : int = 32, train : bool = True, joints : bool = True):
    if joints:
        if train:
            #reads the training and labels data
            total_x, total_y = read_data('train_joints','train_labels')
            print("total x shape train: ", end="")
            print(total_x.shape)
        else:
            #reads the testing data if not in training.
            total_x, total_y = read_data('test_joints','test_labels')
            print("total x shape test: ", end="")
            print(total_x.shape)
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
            #print(total_x[idx].shape)
            yield total_x[idx], total_y[idx]
        # else:
        #     yield normalize(total_x[idx]), total_y[idx]
    # yields a generator for batches of data

#====================================================================================
# IMAGE PROCESSING

def resize_crop(image):
    max_dim = np.argmax(image.shape[:2])
    scale_percent = 100 / image.shape[max_dim]
    width = round(image.shape[1] * scale_percent)
    height = round(image.shape[0] * scale_percent) 
    image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)
    if max_dim == 0:
        image = cv2.copyMakeBorder(image, 0,0,0,100-image.shape[1],cv2.BORDER_CONSTANT,0)
    else:
        image = cv2.copyMakeBorder(image, 0,100-image.shape[0],0,0,cv2.BORDER_CONSTANT,0)
    return image


#====================================================================================