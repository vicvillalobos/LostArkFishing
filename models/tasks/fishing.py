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

    def __init__(self, config, life_remaining, leap_remaining, *args, **kwargs):

        self.config = config

        self.leap_essence_remaining = leap_remaining
        self.life_energy_remaining = life_remaining

        # Define the actions that will be performed in this task.
        self.actions = [
            KeyPressAction(config, config.fishing_key),
            TimerAction(2, 0),
            ScreenMatchLoopAction(config, self),
            KeyPressAction(config, config.fishing_key),
            TimerAction(10, 1000)
        ]

        self.attempt_history = []

    def record_attempt(self, success):
        self.attempt_history.append(success)

    def run_once(self):
        """
        Run the task once.
        """
        # Start the task by calling the run method of the parent class.
        super().run()

    @property
    def life_energy_required(self):
        activity_base_energy = 60

        energy_multiplier = 1.0 if self.leap_essence_remaining < activity_base_energy * 2 else 2.0

        return activity_base_energy * energy_multiplier

    @property
    def has_energy(self):
        return self.life_energy_remaining > self.life_energy_required

    @property
    def successful_attempts(self):
        return self.attempt_history.count(True)

    @property
    def last_attempt(self):
        return self.attempt_history[-1] if len(self.attempt_history) > 0 else False

    def is_finished(self, max_attempts):
        return self.successful_attempts >= max_attempts and max_attempts != 0

    def loop(self, max_times = 0):
        """
        Run the task in a loop.
        Calculate the life energy and leap essence spent in each loop.
        """
        print(f"Starting fishing task loop with {max_times} times before repairing")

        # Wait 5 seconds before starting the task.
        TimerAction(5, 0).execute()
        
        while self.has_energy and not self.is_finished(max_times):
            self.run_once()

            energy_required = self.life_energy_required
            
            if self.last_attempt:
                self.life_energy_remaining -= energy_required
                self.leap_essence_remaining -= energy_required

            print("Fish caught: " + str(self.successful_attempts))