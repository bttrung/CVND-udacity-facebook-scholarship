## Types of Features in image
- Edges: are with a high intensity gradient
- Corners: the intersection of two edges. It's unique and match exactly
- Blobs: a region based features, area of extreme brightness or unique texture

## Definitions
- Diliation: enlarges bright, white areas in an image by adding pixels to the perceived boundaries of objects in the image
- Erosion: does the opposite: it removes pixels along object boundaries and shrinks the size of objects
- Opening: erosion followed by dilation -> useful for noice reduction
- Closing: is the reverse combination of opening: it’s dilation followed by erosion, which is useful in closing small holes or dark areas within an object

- Contours: continous curves that follow the edges along a boundary
- K-mean clustering

## References
- [Harris Corner Detection](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_features_harris/py_features_harris.html)
- [Contours features](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contour_properties/py_contour_properties.html)
- [K-mean clustering](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_ml/py_kmeans/py_kmeans_opencv/py_kmeans_opencv.html)
