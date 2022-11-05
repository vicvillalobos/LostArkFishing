import time, random

from models.action import AutomatedAction
from models.configuration import Configuration

class TimerAction(AutomatedAction):
    """
    This class represent the action of wating for a timer.
    It will expect the following parameters at execution:
    - time -> int: the time to wait in seconds
    - range -> int: the range of the random delay in milliseconds. e.g. 1000 will add a random number between -1 and 1 seconds to the timer.
    Execution shouldn't return anything.
    """
    def __init__(self, time: int, range: int = 500, *args, **kwargs):
        """
        Constructor
        Accepts parameter data as a dictionary for use on execution.
        """
        self.time = time
        self.range_ms = range


    def execute(self):
        """
        This method will wait for the time specified in the parameters.
        """
        range = (random.randint(-self.range_ms, self.range_ms) / 1000)

        print("Waiting for " + str(self.time + range) + " seconds")

        # wait for the timer + a random number between -range_ms and range_ms, all divided by 1000.
        time.sleep(self.time + range)