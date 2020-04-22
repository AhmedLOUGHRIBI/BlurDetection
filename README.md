# BlurDetection
The project aims to detect if an image is blurry or not, it may work as filter to keep just not blurry images and delete the blurry ones.

## The pipeline contains 2 parts:
1.	Compute the metric: variance of the Laplacian score.
2.	Classify the image based on the value of this metric.

## Method review:
You simply take a single channel of an image (presumably grayscale) and convolve it with the following 3 x 3 kernel:

![detecting_blur_laplacian_kernel](https://user-images.githubusercontent.com/55580735/80007734-39642480-84b6-11ea-8ca6-fc34e36fcc0e.png)

And then take the variance (i.e. standard deviation squared) of the response.
If the variance falls below a pre-defined threshold, then the image is considered blurry; otherwise, the image is not blurry.

## Laplacian operator definition:
Laplacian operator is used to measure the 2nd derivative of an image. The Laplacian highlights regions of an image containing rapid intensity changes, much like the Sobel and Scharr operators. And, just like these operators, the Laplacian is often used for edge detection. The assumption here is that if an image contains high variance then there is a wide spread of responses, both edge-like and non-edge like, representative of a normal, in-focus image. But if there is very low variance, then there is a tiny spread of responses, indicating there are very little edges in the image. As we know, the more an image is blurred, the less edges there are.

## Project structure:
![Inkedstr project quality check_LI](https://user-images.githubusercontent.com/55580735/80007769-4719aa00-84b6-11ea-9c7f-a5044eadf2b1.jpg)

### The file LaplacienScoreCalculator.py:
contains functions that will be used to load the test images and compute the variance of laplacian score.
### The file ThresholdTunner.py:
uses a validation dataset placed in the directory “tuning_threshold_data” and plot the distributions of this metric for both blurry and not blurry images.
Based on this plot, we can fix a threshold. If the metric value is lower than this threshold the image will be classified as blurry, else the image will be cclassified as not blurry.
### The file Classifier.py:
contains a class that takes as arguments the scores of the different test images and the chosen threshold (fixed based on threshold tunner). It has two methods, the first classify the images based on their scores, the second save the blurry images in the output folder test_results/blurry and the not blurry images in the output folder test_results/not blurry.
### The file main.py:
calls all the pipeline, thus all task will be automated (from loading test images to saving the blurry and not blurry images in their correct folders)

## Tuning threshold:
To do so we will use a validation dataset (2 folders – one for blurry and the other for not blurry images) labeled manually.
### Validation dataset:
##### Not blurry images folder.
<img width="829" alt="not blurry im" src="https://user-images.githubusercontent.com/55580735/80007877-6e707700-84b6-11ea-8c7a-3322fcfd9bc5.PNG">

##### Blurry images folder
<img width="831" alt="blurry im" src="https://user-images.githubusercontent.com/55580735/80007962-8d6f0900-84b6-11ea-945e-36adcbeb0b0b.PNG">

### Output:
Plot showing the distributions of the variance of Laplacien score for these two groups of images:
<img width="320" alt="distr blurry_not blurry" src="https://user-images.githubusercontent.com/55580735/80008004-9b248e80-84b6-11ea-958c-61ccd327fb85.png">

The distribution of this metric for the blurry images is represented in blue.
The distribution of this metric for the not blurry images is represented in orange.

##### => The two distributions are clearly separable by the red line and a threshold of 150 seems to be doing just fine.

## Testing the pipeline using a threshold of 150:
We will test the pipeline on a folder containing test images mixed (blurry and not blurry).
<img width="824" alt="test images mixed blurry non blurry" src="https://user-images.githubusercontent.com/55580735/80008034-a8417d80-84b6-11ea-8d4a-8e26ab5ec5f7.PNG">
And then we run the command line: python main.py
### Output results:
Blurry folder contains now:

<img width="818" alt="blurry tests" src="https://user-images.githubusercontent.com/55580735/80008065-b5f70300-84b6-11ea-832a-071c84fe2933.PNG">

The not blurry folder contains now:

<img width="818" alt="not blurry test" src="https://user-images.githubusercontent.com/55580735/80008085-be4f3e00-84b6-11ea-9751-969f6195d708.PNG">
#####   => The pipeline is accurate.
