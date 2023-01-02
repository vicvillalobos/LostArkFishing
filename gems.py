import time
from termcolor import colored, cprint

from models.tasks.buygems import BuyGemsTask
from models.tasks.fusegems import FuseGemsTask
from models.configuration import Configuration

config = Configuration('config.ini')

count = 1

bought_count = 0

interval = 4

buy_task = BuyGemsTask(config)
fuse_task = FuseGemsTask(config)

# Sleep 5 seconds
print("Sleeping 5 seconds")
time.sleep(5)

# Get current time in seconds
initial_time = int(round(time.time()))
interval_time = int(round(time.time()))

while(True):
    if count % interval == 0:
        cprint("### Running fuse task", 'green')
        fuse_task.run_once()
        # Print time difference in minutes
        cprint(f"### Interval Time: {(int(round(time.time())) - interval_time)/60} minutes", 'cyan')
        cprint(f"### Total Time: {(int(round(time.time())) - initial_time)/60} minutes", 'cyan')
        print("")
        interval_time = int(round(time.time()))
    else:
        cprint("### Running buy gem task", 'green')
        buy_task.run_once()
        bought_count += 1
        cprint(f"### Bought {bought_count} gems so far.", 'yellow')
    count += 1 