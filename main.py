from models.tasks.fishing import FishingTask
from models.configuration import Configuration

config = Configuration('config.ini')

task = FishingTask(config)

task.loop()