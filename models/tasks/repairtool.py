from models.task import AutomatedTask

from models.actions.keypress import KeyPressAction
from models.actions.timer import TimerAction
from models.actions.mousemove import MouseMoveAction
from models.actions.mouseclick import MouseClickAction

class RepairToolsTask(AutomatedTask):
    """
    This class represents the task of repairing all tools. It will perform the following actions:
    - Press 'Alt + P' to open the pet inventory screen
    - Move the mouse to the repair tool button
    - Click the repair tool button
    - Wait 1 second
    - Move the mouse to the 'Repair All' button
    - Click the 'Repair All' button
    - Wait 1 second
    - Press 'Enter' to confirm the repair
    - Wait 1 second
    - Press 'Esc' to close the pet function screen
    - Wait 1 second
    - Press 'Esc' to close the pet inventory screen
    """

    def __init__(self, config, *args, **kwargs):

        self.config = config

        # Define the actions that will be performed in this task.
        self.actions = [
            KeyPressAction(config, 'alt+p'),
            TimerAction(1, 0),
            MouseMoveAction(config, 262, 162, 0.2),
            TimerAction(1, 0),
            MouseClickAction(config, MouseClickAction.MOUSE_BUTTON_LEFT),
            TimerAction(1, 0),
            MouseMoveAction(config, -237, 264, 0.2),
            TimerAction(1, 0),
            MouseClickAction(config, MouseClickAction.MOUSE_BUTTON_LEFT),
            TimerAction(1, 0),
            KeyPressAction(config, 'return'),
            TimerAction(1, 0),
            KeyPressAction(config, 'esc'),
            TimerAction(1, 0),
            KeyPressAction(config, 'esc'),
            TimerAction(1, 0)
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

        # Wait 5 seconds before starting the task.
        TimerAction(5, 0).execute()
        
        while True:
            super().run()