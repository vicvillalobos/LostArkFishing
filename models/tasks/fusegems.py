from models.task import AutomatedTask

from models.configuration import Configuration 
from models.actions.log import LogAction
from models.actions.timer import TimerAction
from models.actions.mousemove import MouseMoveAction
from models.actions.mouseclick import MouseClickAction
from models.actions.keypress import KeyPressAction

class FuseGemsTask(AutomatedTask):
    """
    This class represents the task of fusing gems.
    """

    def PointAndClick(config, x, y, click_delay, movement_duration, description = ""):
        return [
            LogAction(description),
            MouseMoveAction(config, x, y, movement_duration),
            TimerAction(movement_duration, 0),
            MouseClickAction(config, MouseClickAction.MOUSE_BUTTON_LEFT),
            TimerAction(click_delay, 0)
        ]

    def __init__(self, config, *args, **kwargs):

        self.config = config

        ui_delay = 0.5

        # Define the actions that will be performed in this task.
        self.actions = [
            KeyPressAction(config, config.inventory_key),
        ]
        
        # Refresh button (search)
        
        # Positions Relative to inventory X button
        self.actions.extend(FuseGemsTask.PointAndClick(config, -340 + config.ui_inventory_close_button_position[0], 600 + config.ui_inventory_close_button_position[1], ui_delay, 0.2, "Open Fuse Menu"))
        self.actions.extend(FuseGemsTask.PointAndClick(config, -870 + config.ui_inventory_close_button_position[0], 523 + config.ui_inventory_close_button_position[1], ui_delay, 0.2, "Click Level 6"))
        self.actions.extend(FuseGemsTask.PointAndClick(config, -634 + config.ui_inventory_close_button_position[0], 592 + config.ui_inventory_close_button_position[1], ui_delay, 0.2, "Click Fuse"))
        ## 

        self.actions.extend(FuseGemsTask.PointAndClick(config, -44, 45, ui_delay, 0.2, "Confirm Fuse"))


        self.actions.extend([TimerAction(1, 0), KeyPressAction(config, config.inventory_key)])

    def run_once(self):
        """
        Run the task once.
        """
        # Start the task by calling the run method of the parent class.
        super().run()

    def loop(self, timer = 5):
        """
        Run the task in a loop.
        """

        # Wait 5 seconds before starting the task.
        TimerAction(timer, 0).execute()
        
        while True:
            super().run()