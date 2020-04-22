from cv2 import imread, imwrite
from os.path import join

class Classifier():
    def __init__(self, scores_dictionary, threshold):
        self.blurry = None
        self.not_blurry = None
        self.scores_dictionary = scores_dictionary
        self.threshold = threshold

    def classify_images(self):
        self.blurry = []
        self.not_blurry = []
        for file, score in self.scores_dictionary:
            if score < self.threshold:
                self.blurry.append(file)
            else:
                self.not_blurry.append(file)

    def write_images(self, path_folder):

        for file in self.blurry:
            path_file = join("./test_images", file)
            image = imread(path_file)
            imwrite(join(path_folder+"/blurry", file), image)

        for file in self.not_blurry:
            path_file = join("./test_images", file)
            image = imread(path_file)
            imwrite(join(path_folder+"/not blurry", file), image)