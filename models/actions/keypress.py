import keyboard, random, time

from models.action import AutomatedAction
from models.configuration import Configuration

class KeyPressAction(AutomatedAction):
    """
    This class represent the action of pressing a key.
    execution shouldn't return anything.
    """

    def __init__(self, config: Configuration, key: str, *args, **kwargs):
        """
        Constructor
        parameters:
        - key -> string: the key to press. e.g. 'a' or 'ctrl'
        """
        self.config = config
        self.key = key
        self.hold_range = config.human_hold_range

    def execute(self):
        """
        This method will press the key specified in the parameters.
        """
        self.check_termination()

        print("Pressing key: " + self.key)

        # Get a random number between hold_range[0] and hold_range[1]
        hold_time = random.randint(int(self.hold_range[0]), int(self.hold_range[1]))

        # hold the key for a random time between the range
        keyboard.press(self.key)

        # Wait for a random time between hold_range[0] and hold_range[1]
        time.sleep(hold_time / 1000)

        keyboard.release(self.key)


