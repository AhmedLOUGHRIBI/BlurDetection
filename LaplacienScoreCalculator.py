import cv2
from os import listdir
from os.path import isfile, join


def CalculatingLaplacien(path_image):
    image = cv2.imread(path_image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.Laplacian(gray, cv2.CV_64F).var()

def LaplacienScoresDirectory(path_directory):
    image_files = [f for f in listdir(path_directory) if isfile(join(path_directory, f))]
    laplaciens = {}
    for image in image_files:
        path_image = join(path_directory, image)
        laplacien_image = CalculatingLaplacien(path_image)
        laplaciens[image] = laplacien_image
    return laplaciens