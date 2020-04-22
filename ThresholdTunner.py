from LaplacienScoreCalculator import LaplacienScoresDirectory
from matplotlib import pyplot

path_hign_quality_directory = "./tuning_threshold_data/high quality images/"
path_low_quality_directory = "./tuning_threshold_data/Low quality images/"

Laplaciens_high_quality = LaplacienScoresDirectory(path_hign_quality_directory)
Laplaciens_low_quality = LaplacienScoresDirectory(path_low_quality_directory)


x = Laplaciens_low_quality.values()
y = Laplaciens_high_quality.values()


pyplot.hist(x, alpha=0.5, label='x')
pyplot.hist(y, alpha=0.5, label='y')
pyplot.legend(loc='upper right')
pyplot.show()

# based on distributions of laplacien scores for both blurry images and not blurry images, a threshold of 150 seems doing weel
# to classify new images.