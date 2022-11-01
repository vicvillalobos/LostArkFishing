from models.task import AutomatedTask

from models.actions.keypress import KeyPressAction
from models.actions.timer import TimerAction
from models.actions.screenmatchloop import ScreenMatchLoopAction

class FishingTask(AutomatedTask):
    """
    This class represents the task of fishing. It will perform the following actions:
    - Wait 5 seconds to allow the player to get ready
    - Press the 'e' key to cast the fishing rod
    - Wait 2 seconds
    - Start a template match action loop to find the fish icon every 0.125 seconds
    - If the fish icon is found, press the 'e' key to reel in the fish, if not, 
      wait until the max_reel_timeout is reached and then press 'e' to reel in.
    - Wait 12 seconds
    - Repeat task
    """

    def __init__(self, config, *args, **kwargs):
        human_hold_range = (50, 300) # https://stackoverflow.com/questions/22505698/what-is-a-typical-keypress-duration

        # Define the actions that will be performed in this task.
        self.actions = [
            TimerAction(config, 5, 0),
            KeyPressAction(config, config.fishing_key),
            TimerAction(config, 2, 0),
            ScreenMatchLoopAction(config),
            KeyPressAction(config, config.fishing_key),
            TimerAction(config, 10, 1000)
        ]

    def run_once(self):
        """
        Run the task once.
        """
        # Start the task by calling the run method of the parent class.
        super().run()

    def loop(self):
        """
        Run the task in a loop.
        """
        
        while True:
            super().run()