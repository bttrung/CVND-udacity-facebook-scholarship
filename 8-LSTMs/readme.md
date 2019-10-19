## Long Short-Term Memory Networks


### Definitions
- LSTMs - Long Short-Term Memory Networks
- LSTMs - useful when our neural network needs to switch between remembering recent things, and things from long time ago
- LTM: Long Term Memory
- STM: Short Term Memory
- The Learn Gate: takes a STM and the event and combine them. Then it ignores a bit, keeping the important part. The output of this gate is a new STM
- The Forget Gate: takes a LTM and decides what parts to keep and to forget. The output of this gate is a new LTM
- The Remember Gate: takes a LTM comming out from the Forget Gate, and the STM comming out from the Learn Gate, then simply combine together. The Output is a new LTM
- The Use Gate: takes what's useful from LTM that just came out from the Forget Gate, and what useful from the STM from Learn Gate. The output is a new STM

### References
- [Understand LSTM](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [Exploring LSTMs](http://blog.echen.me/2017/05/30/exploring-lstms/)
- [LSTMs lecture](https://www.youtube.com/watch?v=iX5V1WpxxkY)
- [Pytorch LSTM Tutorial](https://pytorch.org/tutorials/beginner/nlp/sequence_models_tutorial.html#lstm-s-in-pytorch)
- [Guide to LSTMs for beginner](https://skymind.ai/wiki/lstm)
