import cv2 as cv, numpy as np, time
from mss import mss
import configparser

from models.action import AutomatedAction
from models.configuration import Configuration

class ScreenMatchLoopAction(AutomatedAction):

    def __init__(self, config: Configuration, task, *args, **kwargs):
        """
        Constructor
        parameters:
        - config -> Configuration: the configuration object.
        """
        self.config = config
        self.region_resolution = config.fishing_region
        self.screen_number = config.screen_number
        self.screen_resolution = config.screen_resolution
        self.template = config.fishing_template
        self.threshold = config.fishing_threshold
        self.interval = config.fishing_interval
        self.max_time = config.fishing_max_time
        self.task = task

    def grab_screen(self):
        """
        This method will take a grayscale screenshot and return it.
        """

        region_half = (self.region_resolution[0] // 2, self.region_resolution[1] // 2)

        # Generate a rectangle region (top,left,width,height) in the center of the screen with the given resolution.
        region = (int(self.screen_resolution[0]/2-region_half[0]), int(self.screen_resolution[1]/2-region_half[1]), self.region_resolution[0], self.region_resolution[1])

        with mss() as sct:
            
            monitor = sct.monitors[self.screen_number]
            monitor["left"] = region[0]
            monitor["top"] = region[1]
            monitor["width"] = region[2]
            monitor["height"] = region[3]

            img = np.array(sct.grab(monitor))
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            return gray

    def execute(self):
        """
        This method will take a screenshot and return it.
        """

        print("Starting screen image recognition")	

        time_elapsed = 0

        while True:
            self.check_termination()
            screen = self.grab_screen()

            # read template image
            template = cv.imread(self.template, cv.IMREAD_GRAYSCALE)

            # Apply template Matching using cv2.TM_CCOEFF_NORMED method
            res = cv.matchTemplate(screen, template, cv.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

            # Check if the sample is above the threshold
            if max_val > self.threshold:
                # We found a good enough match!
                print("Found a fish!")
                self.task.record_attempt(True)
                return True
            # else:
            #     print(f'No fish found. Sample: {max_val}')

            # Wait for the interval
            time.sleep(self.interval) 

            # Sum the time waited
            time_elapsed += self.interval

            # Check if we have exceeded the max time
            if time_elapsed > self.max_time:
                # We have exceeded the max time
                print("No fish found")
                self.task.record_attempt(False)
                return False