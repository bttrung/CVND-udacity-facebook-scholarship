## RNN's


### Definitions
- RNN: Recurrent Neural Networks - give us a way to incorporate memory into our neural networks, and will be critical in analyzing sequential data
- FFNN: Feedfoward Neural Network
- Vanishing Gradient

- Feedforward
- Backpropagation
- MSE: Mean Squared Error
- Cross Entropy
- Activation function
- Partial Derivaties
- Learning Rate
- Loss Function
- Linear Combination
- Chain Rule
- Mini Batch Training: update the weight once every N steps
- Elman Network
- RNN Folded Model
- RNN Unfolded Model
- Backpropagation Through Time

### Explains
There are two main differences between FFNNs and RNNs. The Recurrent Neural Network uses:
- sequences as inputs in the training phase, and
- memory elements

Memory is defined as the output of hidden layer neurons, which will serve as additional input to the network during next training step.

The basic three layer neural network with feedback that serve as memory inputs is called the Elman Network

### References
- [Video Classification Method](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/May/5af0e03b_video-classification/video-classification.pdf)
- [Sketch RNN](https://magenta.tensorflow.org/assets/sketch_rnn_demo/index.html)
- [Vanishing gradient problem](https://en.wikipedia.org/wiki/Vanishing_gradient_problem)
- [Time Delay Neural Network](https://en.wikipedia.org/wiki/Time_delay_neural_network)
- [MSE](https://en.wikipedia.org/wiki/Mean_squared_error)
- [ReLU and Softmax Activation Functions](https://github.com/Kulbear/deep-learning-nano-foundation/wiki/ReLU-and-Softmax-Activation-Functions)
- [Backpropagation example](https://www.anotsorandomwalk.com/backpropagation-example-with-numbers-step-by-step/)
- [Backpropagation step by step](https://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/)
- [Partial Derivatives](http://www.columbia.edu/itc/sipa/math/calc_rules_multivar.html)
- [Common Derivatives](http://tutorial.math.lamar.edu/pdf/Common_Derivatives_Integrals.pdf)
- [Turning learning rate](http://blog.datumbox.com/tuning-the-learning-rate-in-gradient-descent/)
- [Loss Function](http://cs231n.github.io/neural-networks-3/#loss)
