import time

from models.tasks.repairtool import RepairToolsTask
from models.configuration import Configuration

config = Configuration('config.ini')

task = RepairToolsTask(config)

print('Waiting 5 seconds...')
time.sleep(5)

task.run_once()