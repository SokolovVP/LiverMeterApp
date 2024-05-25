import cv2
import numpy as np
from ImageThresholder import ImageThresholder


class CVThresholdImageSegmenter:

    @staticmethod
    def segment_image(image: np.array, threshold_value=67.0, upper_value=255.0) -> (np.array, np.array, np.array):
        _, threshold_image = ImageThresholder.threshold(image, threshold_value, upper_value)

        contours = cv2.findContours(threshold_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        