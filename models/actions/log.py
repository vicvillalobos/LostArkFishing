from models.action import AutomatedAction

class LogAction(AutomatedAction):
    """
    Logs a message to the console.
    """

    def __init__(self, text, *args, **kwargs):
        """
        Constructor
        Accepts parameter data as a dictionary for use on execution.
        """
        self.text = text
    
    def execute(self):
        """
        This method will click the mouse.
        """
        self.check_termination()

        print("Executing: " + self.text)