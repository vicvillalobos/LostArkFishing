import cv2 as cv
import numpy as np

from models.action import AutomatedAction

class TemplateMatchAction(AutomatedAction):
    """
    This class represent the action of template matching using OpenCV.
    Returns True if a match was found, False otherwise.
    """

    def __init__(self, template: str, image: np.array, threshold: float, *args, **kwargs):
        """
        Constructor
        parameters:    
        - template -> string: the path to the image to match
        - image -> numpy.array: the image to match the template to
        - threshold -> float: the threshold to use for the template matching. 0.0 - 1.0
        """
        super().__init__(*args, **kwargs)
        self.template = template
        self.image = image
        self.threshold = threshold

    def execute(self):
        """
        This method will match the template to the image.
        """

        print("TemplateMatchAction.execute()")

        # Apply template Matching using cv2.TM_CCOEFF_NORMED method
        res = cv.matchTemplate(self.image, self.template, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

        # Check if the sample is above the threshold
        if max_val > self.threshold:
            # We found a good enough match!
            return True
        else:
            # No good enough match was found
            return False