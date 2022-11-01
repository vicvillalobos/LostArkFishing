import numpy as np, cv2 as cv
from mss import mss

from models.action import AutomatedAction

class ScreenAction(AutomatedAction):
    """
    This class represent the action of taking a screenshot using mss.
    execution should return the screenshot as a numpy array.
    """

    def __init__(self, region: tuple[int, int], screen_number: int, *args, **kwargs):
        """
        Constructor
        parameters:
        - region -> tuple(int,int): the region resolution to take the screenshot in pixels.
        - screen_number -> int: the screen number to take the screenshot from.
        """
        super().__init__(*args, **kwargs)
        self.region = region
        self.screen_number = screen_number

    def execute(self):
        """
        This method will take a screenshot and return it.
        """
        with mss() as sct:
            if self.region:
                monitor = sct.monitors[self.screen_number]
                monitor["top"] = self.region[1]
                monitor["left"] = self.region[0]
                monitor["width"] = self.region[2]
                monitor["height"] = self.region[3]
            else:
                monitor = sct.monitors[self.screen_number]
            img = np.array(sct.grab(monitor))
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            return gray

        