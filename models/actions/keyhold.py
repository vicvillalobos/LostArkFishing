import keyboard, random, time

from models.action import AutomatedAction
from models.configuration import Configuration

class KeyHoldAction(AutomatedAction):
    """
    This class represent the action of pressing and holding a key.
    execution shouldn't return anything.
    """

    def __init__(self, key: str, hold_time: int, *args, **kwargs):
        """
        Constructor
        parameters:
        - key -> string: the key to press. e.g. 'a' or 'ctrl'
        """
        self.key = key
        self.hold_time = hold_time

    def execute(self):
        """
        This method will press and hold the key specified in the parameters.
        """

        print("Holding key: " + self.key)

        # hold the key for a random time between the range
        keyboard.press(self.key)

        # Wait for a random time between hold_range[0] and hold_range[1]
        time.sleep(self.hold_time / 1000)

        print("Releasing key: " + self.key)
        keyboard.release(self.key)


