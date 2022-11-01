from models.task import AutomatedTask

from models.actions.keyhold import KeyHoldAction
from models.actions.timer import TimerAction

class AutoAttackTask(AutomatedTask):
    """
    This class represents the task of autoattacking.
    It should press the attack key and release it after a while.
    then repeat.
    """

    def __init__(self, config, *args, **kwargs):

        self.config = config

        # Define the actions that will be performed in this task.
        self.actions = [
            KeyHoldAction('c', 10000),
            TimerAction(1, 500)
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