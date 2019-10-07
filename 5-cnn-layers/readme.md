## CNN Layers and Feature Visualization

### Definitions
- CNN's: Convolutional Neural Networks. There are some major components:
  - Convolutional layers: is a stack of feature maps - where we have one feature map for each filter
  - Pooling layer: take in an image (usually a filtered image) and output a reduced version of that image 
  - Maxpooling layers: look at areas in an input image (like the 4x4 pixel area) and choose to keep the maximum pixel value in that area, in a new, reduced-size area
  - Fully-connected (linear) layers: to connect the input it sees to a desired form of output, means converting a matrix of image features into a feature vector whose dimensions are 1xC, where C is the number of classes
  - Softmax function: take any vector of values as input and returns a vector of the same length whose values are all in the range (0, 1) and, together, these values will add up to 1
  - Dropout layer: to prevent overfitting. Dropout layers essentially turn off certain nodes in a layer with some probability, p. This ensures that all nodes get an equal chance to try and classify different images during training, and it reduces the likelihood that only a few, heavily-weighted nodes will dominate the process

- Loss function
- Optimizer
- Cross Entropy Loss

### Tips
- How can you decide on a network structure? How many layers? When to include dropout layers?...
--> You are encouraged to:
  - Change the number of convolutional layers and see what happens
  - Increase the size of convolutional kernels for larger images
  - Change loss/optimization functions to see how your model responds (especially change your hyperparameters such as learning rate and see what happens -- you will learn more about hyperparameters in the second module of this course)
  - Add layers to prevent overfitting
  - Change the batch_size of your data loader to see how larger batch sizes can affect your training
  - Always watch how much and how quickly your model loss decreases, and learn from improvements as well as mistakes!



### References
- [FashionMNIST](https://github.com/zalandoresearch/fashion-mnist)
- [Pytorch NN](https://pytorch.org/docs/stable/nn.html) 
- [Pytorch Pooling](https://pytorch.org/docs/stable/nn.html#pooling-layers)
- [Dropout Layer](https://pytorch.org/docs/stable/nn.html#dropout-layers)
- [Loss Function](https://pytorch.org/docs/master/nn.html#loss-functions)
- [Optimizer](https://pytorch.org/docs/master/optim.html)

- [Implement CNN in details](https://www.deeplearningwizard.com/deep_learning/practical_pytorch/pytorch_convolutional_neuralnetwork/)
