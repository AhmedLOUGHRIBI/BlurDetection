from Classifier import Classifier
from LaplacienScoreCalculator import LaplacienScoresDirectory

path_test_images = "./test_images"
test_LaplacienScores = LaplacienScoresDirectory(path_test_images)

#after analysing distributions of scores with ThresholdTunner it seems a threshold of 150 will do well
threshold = 150

classifier = Classifier(test_LaplacienScores.items(), threshold)
classifier.classify_images()

results_path_folder = "test_results"
classifier.write_images(results_path_folder)

