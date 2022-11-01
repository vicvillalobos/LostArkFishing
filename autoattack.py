from models.tasks.autoattack import AutoAttackTask
from models.configuration import Configuration

config = Configuration('config.ini')

task = AutoAttackTask(config)

task.loop()