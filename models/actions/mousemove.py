import pyautogui, random

from models.action import AutomatedAction
from models.configuration import Configuration

class MouseMoveAction(AutomatedAction):
    """
    This class represent the action of moving the mouse.
    It will expect the following parameters at execution:
    - x -> int: the x coordinate to move the mouse to
    - y -> int: the y coordinate to move the mouse to
    - duration -> float: the time in seconds to take to move the mouse from its current position to the specified position
    Execution shouldn't return anything.
    """

    def __init__(self, config: Configuration, x: int, y: int, duration: float = 0.5, relative : bool = True, *args, **kwargs):
        """
        Constructor
        Accepts parameter data as a dictionary for use on execution.
        """
        self.config = config

        # Get absolute position from relative x if relative is true.
        # Relative position is relative to the center of the screen
        if relative:
            x = config.screen_resolution[0] / 2 + x
            y = config.screen_resolution[1] / 2 + y
        
        self.x = x
        self.y = y


        self.duration = duration
        self.duration_range = config.human_mouse_movement_duration_range
        self.position_range = config.human_mouse_movement_range

    def execute(self):
        """
        This method will move the mouse to the specified coordinates.
        """

        # add a random number between -range and range to the x and y coordinates
        pos_range = self.position_range
        x = self.x + random.randint(-pos_range, pos_range)
        y = self.y + random.randint(-pos_range, pos_range)

        # add a random number between -range and range to the duration
        range = self.duration_range
        duration = self.duration + (random.randint(-range, range) / 1000)

        print("Moving mouse to " + str(x) + ", " + str(y))
        pyautogui.moveTo(x, y, duration=duration)