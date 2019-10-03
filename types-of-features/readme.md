## Types of Features in image
- Edges: are with a high intensity gradient
- Corners: the intersection of two edges. It's unique and match exactly
- Blobs: a region based features, area of extreme brightness or unique texture

## Definitions
- Diliation: enlarges bright, white areas in an image by adding pixels to the perceived boundaries of objects in the image
- Erosion: does the opposite: it removes pixels along object boundaries and shrinks the size of objects
- Opening: erosion followed by dilation -> useful for noice reduction
- Closing: is the reverse combination of opening: it’s dilation followed by erosion, which is useful in closing small holes or dark areas within an object

- Image Contours: continous curves that follow the edges along a boundary

## References
- [Harris Corner Detection](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_features_harris/py_features_harris.html)
