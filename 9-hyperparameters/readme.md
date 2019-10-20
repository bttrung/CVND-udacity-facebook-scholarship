## Hyperparameters for Deep Neural Network 


#### 1. Learning Rate
- Learning Rate Decay
- Adaptive Leaning

### 2. Minibatch Size = # of training examples
- Stochastic Training = 1 training example
- Batch Training = entire examples in the dataset 
- Minibatch = any # beetween them

- The recommend # of minibatch is 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048
- Small minibatch size -> more noise. This noise often helpful in preventing the training process from stopping at local minimal
- Too small -> too slow
- Too large -> computationally taxing and result in worse accuracy
- 32 -> 256 are potentially good starting values

### 3. Number of Iterations
- Epoch
- Batch
- Can be optimized automatically using a technique called "early stopping"
- Early Stopping:
    - Monitoring the Validation Error
    - Stop the training when the error stops decreasing
    - We can define the rule like: stop training after 10 or 20 steps that error not decrease

### 4. Number of Hidden Units - Layers
- Number of Hidden Units: is the main measure for a model's learning capacity
    - If too much -> tend to overfit, just try to memorize the training set
    - Can utilize regularization techniques like dropout ot L2 regularization
- For the first hidden layer:
    - Setting number of units larger than the number of input -> beneficial
- Number of layers:
    - 3 layers net will outperform a 2 layers net
    - Going even deeper (4, 5, 6...)rarely helps much more
    - The exception to this is the CNN: the deeper they are -> the better they perform
 
### 5. RNN Hyperparameters
- Choosing cell type
- Choosing how deep is it? How many layers will we stack
- LSTM CELL
- GRU CELL

### References
- [Jay Alammar's Blog](http://jalammar.github.io/)
- [Exponential Decay](https://www.tensorflow.org/versions/r1.14/api_docs/python/tf/train/exponential_decay)
- [AdamOptimizer](https://www.tensorflow.org/versions/r1.14/api_docs/python/tf/train/AdamOptimizer)
- [AdagradOptimizer](https://www.tensorflow.org/versions/r1.14/api_docs/python/tf/train/AdagradOptimizer)
- [CNN for Visual Recognition](https://cs231n.github.io/neural-networks-1/)
- [More about Model Capacity](http://www.deeplearningbook.org/contents/ml.html)
- [Practical Recommendation for Gradient-based training](https://arxiv.org/abs/1206.5533)
- [Selecting Hyperparameters](http://www.deeplearningbook.org/contents/guidelines.html)
- [How to chose NN hyperparameters](http://neuralnetworksanddeeplearning.com/chap3.html#how_to_choose_a_neural_network's_hyper-parameters)
- [Effective Backpropagation](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)
- [Visualizing and Understanding RNN](https://arxiv.org/abs/1506.02078)

