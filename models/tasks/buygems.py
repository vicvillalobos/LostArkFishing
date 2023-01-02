from models.task import AutomatedTask

from models.configuration import Configuration 
from models.actions.log import LogAction
from models.actions.timer import TimerAction
from models.actions.mousemove import MouseMoveAction
from models.actions.mouseclick import MouseClickAction

class BuyGemsTask(AutomatedTask):
    """
    This class represents the task of buying low level gems from the auction house. It will perform the following actions:

    """

    def PointAndClick(config, x, y, click_delay, movement_duration, description = ""):
        return [
            LogAction(description),
            MouseMoveAction(config, x, y, movement_duration),
            #TimerAction(movement_duration, 0),
            MouseClickAction(config, MouseClickAction.MOUSE_BUTTON_LEFT),
            TimerAction(click_delay, 0)
        ]

    def __init__(self, config, *args, **kwargs):

        self.config = config

        ui_delay = 0.5

        # Define the actions that will be performed in this task.
        self.actions = []
        
        # Refresh button (search)
        self.actions.extend(BuyGemsTask.PointAndClick(config, 554, -301, ui_delay, 0.2, "Refresh button (search)"))
        
        self.actions.extend([TimerAction(0.5, 500)])

        # Last Item on page
        self.actions.extend(BuyGemsTask.PointAndClick(config, 562, 308, ui_delay, 0.2, "Last Item on page"))
        # Buy/bid button
        self.actions.extend(BuyGemsTask.PointAndClick(config, 609, 382, ui_delay, 0.2, "Buy/bid button"))
        # Buy now button
        self.actions.extend(BuyGemsTask.PointAndClick(config, 172, 136, ui_delay, 0.2, "Buy now button"))
        # Confirm buy now
        self.actions.extend(BuyGemsTask.PointAndClick(config, 4, 30, ui_delay, 0.2, "Confirm buy now"))

        self.actions.extend([TimerAction(3, 0), LogAction("Waiting 3 seconds")])
        
        # Mail button
        self.actions.extend(BuyGemsTask.PointAndClick(config, config.ui_mail_icon_position[0], config.ui_mail_icon_position[1], ui_delay, 0.2, "Mail button"))
        # First mail
        self.actions.extend(BuyGemsTask.PointAndClick(config, config.ui_first_mail_position[0], config.ui_first_mail_position[1], ui_delay, 0.2, "First mail"))
        # Accept all
        self.actions.extend(BuyGemsTask.PointAndClick(config, config.ui_mail_accept_position[0], config.ui_mail_accept_position[1], ui_delay, 0.2, "Accept all"))
        # Mail Remove
        self.actions.extend(BuyGemsTask.PointAndClick(config, config.ui_mail_remove_position[0], config.ui_mail_remove_position[1], ui_delay, 0.2, "Mail Remove"))

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