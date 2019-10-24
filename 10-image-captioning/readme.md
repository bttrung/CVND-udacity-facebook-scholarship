### Image Captioning

### Definitions & Explains
- Captioning model: CNN + RNN -> merging most powerful attributes of them
- CNN: exel at preserving spatial info and images
- RNN: work well at sequence data
- CNN-RNN model: 
    - Remove the final Fully Connected Layer that classify the image
    - CNN is the encoder to extract feature vector
    - Pre-process the feature vector
    - RNN is the decoder to the processed feature vector to the natural language
    - RNN responsibilities:
        - Remember spatial information from the input feature vector
        - Predict the next word

- The Glue
- Tokenization: turn any strings into a list of integers
- Tokenizing words

### References
- [COCO dataset](http://cocodataset.org/#home)
- [NLTK - Python lib for Tokenize](http://www.nltk.org/api/nltk.tokenize.html)