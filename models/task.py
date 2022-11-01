class AutomatedTask:
    '''
    AutomatedTask is a class that represents a series of actions
    needed to complete a task. 
    The actions can be a combination of:
    - Key presses
    - Mouse clicks
    - Mouse movements
    - Screen template matching (image recognition)
    - Timer (wait + randomized delay)

    '''

    def __init__(self, actions):
        self.actions = actions

    def run(self):
        for action in self.actions:
            action.execute()