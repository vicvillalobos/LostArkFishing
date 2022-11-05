import pyautogui, random

from models.action import AutomatedAction
from models.configuration import Configuration

class MouseClickAction(AutomatedAction):
    """
    This class represent the action of clicking the mouse.
    It will expect the following parameters at execution:
    - button -> int: the button to click. e.g. 0 (left) or 1 (right)
    Execution shouldn't return anything.
    """

    MOUSE_BUTTON_LEFT = "left"
    MOUSE_BUTTON_RIGHT = "right"

    def __init__(self, config: Configuration, button: str, *args, **kwargs):
        """
        Constructor
        Accepts parameter data as a dictionary for use on execution.
        """
        self.config = config
        self.button = button
        self.duration_range = config.human_hold_range
    
    def execute(self):
        """
        This method will click the mouse.
        """
        # add a random number between -range and range to the duration
        range = self.duration_range
        duration = random.randint(range[0], range[1]) / 1000

        print("Clicking mouse button " + str("left" if self.button == 0 else "right"))
        pyautogui.click(button=self.button, duration=duration)