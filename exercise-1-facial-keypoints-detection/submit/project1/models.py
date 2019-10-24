import torch
import torch.nn as nn
import torch.nn.functional as F
# can use the below import should you choose to initialize the weights of your Net
import torch.nn.init as I


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        
        ## TODO: Define all the layers of this CNN, the only requirements are:
        ## 1. This network takes in a square (same width and height), grayscale image as input
        ## 2. It ends with a linear layer that represents the keypoints
        ## it's suggested that you make this last layer output 136 values, 2 for each of the 68 keypoint (x, y) pairs
        

        # As an example, you've been given a convolutional layer, which you may (but don't have to) change:
        # 1 input image channel (grayscale), 32 output channels/feature maps, 5x5 square convolution kernel
        
        self.conv1 = nn.Conv2d(1, 32, 5)
        #self.conv1.weight.data.fill_(0.01)
        #self.conv1.bias.data.fill_(0.01)
        
        # comment from Udacity
        #Is there a reason for why you have set the weights and bias as 0.01?
        #A better approach would be to initialize the weights randomly using something like Xavier initialization
        I.xavier_uniform(self.conv1.weight)

        # output size (W-F)/S +1 = = (224 - 5) / 1 + 1 = 220
        # (32, 220, 220)
        
        self.pool = nn.MaxPool2d(2, 2)
        # output size = (32, 110, 110)
        
        # previous version: self.conv2 = nn.Conv2d(32, 64, 4)
        self.conv2 = nn.Conv2d(32, 64, 3)
        I.xavier_uniform(self.conv2.weight)
        # Comment from Udacity
        #Avoid using even-sized kernels as they do not have a true center. 
        #A 4x4 kernel doesn't have a true center and this might cause the model to have 
        #slight shift in either direction. Since convolution occurs around the center, odd-sized kernels are better.

        # output size: (110 - 4) / 1 + 1 = 107
        # (64, 107, 107)
        # (64, 53, 53)
        
        self.conv3 = nn.Conv2d(64, 128, 3)
        # output size: (53 - 3) / 1 + 1 = 51
        # (128, 51, 51)
        # (128, 25, 25)

        self.conv4 = nn.Conv2d(128, 256, 2)
        # output size: (25 - 2) / 1 + 1 = 24
        # (128, 24, 24)
        # (128, 12, 12)
        
        self.fc1 = nn.Linear(256*12*12, 3000)
        # dropout with p=0.4
        #self.fc_drop1 = nn.Dropout(p=0.2)

        self.fc_drop2 = nn.Dropout(p=0.4)

        #self.fc1_drop = nn.Dropout(p=0.1)
        #self.fc2_drop = nn.Dropout(p=0.2)
        #self.fc3_drop = nn.Dropout(p=0.3)
        #self.fc4_drop = nn.Dropout(p=0.4)
        #self.fc5_drop = nn.Dropout(p=0.5)

        self.fc2 = nn.Linear(3000, 1000)
         

        self.fc3 = nn.Linear(1000, 136)

        
        ## Note that among the layers to add, consider including:
        # maxpooling layers, multiple conv layers, fully-connected layers, and other layers (such as dropout or batch normalization) to avoid overfitting
        

        
    def forward(self, x):
        ## TODO: Define the feedforward behavior of this model
        ## x is the input image and, as an example, here you may choose to include a pool/conv step:
        ## x = self.pool(F.relu(self.conv1(x)))
        
         # two conv/relu + pool layers
        x = self.pool(F.relu(self.conv1(x)))
        x = nn.BatchNorm2d(32)
        # previous version: x = self.fc_drop1(x)
        # Comment from Udacity:
        #Avoid using dropout for conv layers, it might degrade performance in a few cases. 
        #Use BatchNorm2d to regularize your conv layers, it can be up to 20x more 
        #effective than dropout, although it does increase training time
        
        x = self.pool(F.relu(self.conv2(x)))
        #x = self.fc_drop1(x)
        x = nn.BatchNorm2d(64)
        x = self.pool(F.relu(self.conv3(x)))
        x = nn.BatchNorm2d(128)
        #x = self.fc_drop1(x)
        x = self.pool(F.relu(self.conv4(x)))
        x = nn.BatchNorm2d(256)
        #x = self.fc_drop1(x)

        # prep for linear layer
        # this line of code is the equivalent of Flatten in Keras
        x = x.view(x.size(0), -1)
        
        # 3 linear layers with dropout in between
        x = F.relu(self.fc1(x))
        x = self.fc_drop2(x)
        x = self.fc2(x)
        x = self.fc_drop2(x)
        x = self.fc3(x)
        
        # a modified x, having gone through all the layers of your model, should be returned
        return x
