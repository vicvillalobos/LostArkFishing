from models.tasks.fishing import FishingTask
from models.tasks.repairtool import RepairToolsTask
from models.configuration import Configuration

life_energy_left = int(input('How much life energy do you have left? '))

leap_essence_left = int(input('How much leap essence do you have left? '))

config = Configuration('config.ini')

fishing_task = FishingTask(config, life_energy_left, leap_essence_left)
repair_task = RepairToolsTask(config)

while fishing_task.has_energy:
    fishing_task.loop(config.times_to_repair)
    repair_task.run_once()
    fishing_task.reset_attempts()

print('')
print('Not enough life energy.')
print('')
    