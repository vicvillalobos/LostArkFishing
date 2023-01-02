import keyboard
from termcolor import cprint
class AutomatedAction:
    """
    This class represent the action to be performed by the bot.
    It provides a method to perform the action and should be extended
    """

    def __init__(self):
        """
        Constructor
        Accepts parameter data as a dictionary for use on execution.
        """
        pass
    
    def execute(self):
        """
        This method should be implemented by the child class
        """
        pass

    def check_termination(self):
        """
        This method should be implemented by the child class
        """
        if keyboard.is_pressed('shift+alt'):
            # Kill the bot
            cprint("Terminating bot", 'red')
            exit(0)