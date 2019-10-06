## Feature Vectors

### Definitions
- Feature vectors
- ORB algorithm: is a very fast algorithm that creates feature vectors from detected keypoints
  - Oriendted FAST and Rotated BRIEF
  - ORB uses FAST to locate the keypoints in an image
  - ORB has some great properties: being invariant to rotations, changes in illumination, and noise
  
- Keypoint: a small region in an image that particulaly distinctive 
- Binary Feature Vectors
- FAST: 
  - Feature from Accelerated Segments Test
  - The keypoints found by FAST give us info about the location of object defining edges in an image, dont include any info about the direction of the change of intensity

- BRIEF algorithm:
  - Binary, Robust, Independent Elementary Features
  - Purpose: create binary feature vectors from a set of keypoints
  
- Image pyramid: is a multi-scale representation of a single image that consists of sequence of images at different of resolution

- Intensity centroid
- Feature matching
- [HOG algorithm](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_histograms/py_table_of_contents_histograms/py_table_of_contents_histograms.html):
  - Histogram of Oriented Gradients
  - Oriented Gradients: the direction of image gradients
  - HOG feature vectors
