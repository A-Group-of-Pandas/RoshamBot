import torch
from torch import nn
import numpy as np
from data_processing import read_batch
from data_processing import data_augmentation
from data_processing import normalize_joints
from Model import RecogJoint
from torch.utils.tensorboard import SummaryWriter

loss_fn = nn.CrossEntropyLoss()
writer = SummaryWriter()
minLoss = 1e9

def train(model, optimizer, batch_size, epochs):
    model = model.float()
    counter = 0
    for epoch in range(epochs):
        losses = []
        accs = []
        train_gen = read_batch(batch_size,True)
        test_gen = read_batch(batch_size,False)
        # creates a generator for batch data and iterates through it below
        for batch_i,(train_x_batch, truth) in enumerate(train_gen):
            train_x_batch = torch.tensor(train_x_batch).to('cpu')
            truth = torch.tensor(truth).to('cpu')
            #print(truth.shape)
            #print(train_x_batch.shape)
            train_x_batch = normalize_joints(train_x_batch)
            train_x_batch = data_augmentation(train_x_batch)
            train_x_batch = train_x_batch.reshape((train_x_batch.shape[0], -1))
            preds = model(train_x_batch.float())
            # (N, 3)
            loss = loss_fn(preds, truth)
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()
            with torch.no_grad():
                losses.append(loss.detach())
                acc = torch.mean((torch.argmax(preds, dim=1) == truth).float())
                accs.append(acc)
                writer.add_scalar('loss/train', loss.item(), counter)
                writer.add_scalar('acc/train', acc, counter)
                counter+=1
        with torch.no_grad():
            loss = np.mean(losses)
            acc = np.mean(accs)
            # calculates accuracy, graphes on tensorboard
            if epoch%5==0:
                print(f'train {epoch}, loss: {loss}, acc: {acc}')
                model.eval()
                eval(model, test_gen, epoch)
                model.train()

def eval(model, test_gen, epoch):
    # evaluates the loss using test data
    global minLoss
    model = model.float()
    loss, count, acc = 0,0,0
    for test_x_batch, truth in test_gen:
        test_x_batch = normalize_joints(test_x_batch)
        test_x_batch = test_x_batch.reshape((test_x_batch.shape[0], -1))
        test_x_batch = torch.tensor(test_x_batch).to('cpu')
        truth = torch.tensor(truth).to('cpu')
        preds = model(test_x_batch.float()) 

        loss += loss_fn(preds, truth)
        acc += torch.mean((torch.argmax(preds, dim=1) == truth).float())
        count += 1
    loss /= count
    acc /= count
    writer.add_scalar('loss/eval', loss.item(), epoch)
    writer.add_scalar('acc/eval', acc, epoch)
    # calculates accuracy, graphes on tensorboard
    print(f'eval {epoch}, loss: {loss}, acc: {acc}')
    if loss < minLoss:
        minLoss = loss
        torch.save(model.state_dict(), 'rps_recogn_joint')
        # saves the model params whenever the loss goes below minLoss
    #torch.save(model.state_dict(), 'rps_recogn_joint')

epochs = 500
batch_size = 64
model = RecogJoint().to('cpu')
optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)
train(model, optimizer, batch_size, epochs)


