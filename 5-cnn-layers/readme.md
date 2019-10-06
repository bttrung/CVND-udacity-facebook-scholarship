## CNN Layers and Feature Visualization

### Definitions
- CNN's: Convolutional Neural Networks. There are some major components:
  - Convolutional layers: is a stack of feature maps - where we have one feature map for each filter
  - Pooling layer: take in an image (usually a filtered image) and output a reduced version of that image 
  - Maxpooling layers: look at areas in an input image (like the 4x4 pixel area) and choose to keep the maximum pixel value in that area, in a new, reduced-size area
  - Fully-connected (linear) layers: to connect the input it sees to a desired form of output, means converting a matrix of image features into a feature vector whose dimensions are 1xC, where C is the number of classes
  - Softmax function: take any vector of values as input and returns a vector of the same length whose values are all in the range (0, 1) and, together, these values will add up to 1
  - Dropout layer: to prevent overfitting. Dropout layers essentially turn off certain nodes in a layer with some probability, p. This ensures that all nodes get an equal chance to try and classify different images during training, and it reduces the likelihood that only a few, heavily-weighted nodes will dominate the process

### References
- [FashionMNIST](https://github.com/zalandoresearch/fashion-mnist)
- [Pytorch NN](https://pytorch.org/docs/stable/nn.html) 
- [Pytorch Pooling](https://pytorch.org/docs/stable/nn.html#pooling-layers)
- [Dropout Layer](https://pytorch.org/docs/stable/nn.html#dropout-layers)
