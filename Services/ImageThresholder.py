import cv2
import numpy as np


class ImageThresholder:

    @staticmethod
    def threshold(image: np.array, threshold_value: float, upper_value: float) -> (np.array, np.array):
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        threshold_image = cv2.threshold(grayscale_image, threshold_value, upper_value, cv2.THRESH_BINARY)

        return image, threshold_image   
