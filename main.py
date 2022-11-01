###############################
# CONFIGURATION
###############################

# Screen number
screen_number = 1

# Screen resolution
screen_resolution = (1920, 1080)

# Capture region resolution. This is the rectangle segment at the center of the screen used for image detection. 
# Try to adjust this to suit your screen resolution. The idea is to have a rectangle region that is as small as possible,
# to avoid looking at UI and other non-relevant details but still big enough to contain the fish exclamation mark icon. 
#
# i.e. for a 1920x1080 resolution, a 300x300 region is a good value.
region_resolution = (300, 300)

# Time in seconds between each detection
detection_interval = 0.125

# Template threshold 
template_threshold = 0.88

# Fishing key
fishing_key = 'e'

# Time to wait (in seconds) between throwing lure and starting the detection.
first_wait = 3

# Max time to spend in the detection mode. After this time, the script will press {fishing_key} again.
max_reel_timeout = 13

# Time to wait between reel attempt and next lure throw.
reel_wait = 10


###############################
###############################

import cv2 as cv
import numpy as np
from mss import mss
import time
import keyboard
import random

def main():
    """
    Main function.
    Initializes the region and template, then starts the fishing function.
    """
    region_half = (int(region_resolution[0] / 2), int(region_resolution[1] / 2))

    # rectangle region in the center of the screen.
    region = (int(screen_resolution[0]/2-region_half[0]), int(screen_resolution[1]/2-region_half[1]), region_resolution[0], region_resolution[1])

    # load the template. e.g. what we are trying to detect.
    template = cv.imread('template.png',0)

    start_fish_detection(template, region, template_threshold, detection_interval)


def randomize_timer(timer, range_ms):
    '''
    Returns timer + a random number between -range_ms and range_ms, all divided by 1000.
    '''
    return timer + (random.randint(-range_ms, range_ms) / 1000)


def grab_screen(region=None):
    """
    Returns an array with the image information in grayscale of the screen region.
    """
    with mss() as sct:
        if region:
            monitor = sct.monitors[screen_number]
            monitor["top"] = region[1]
            monitor["left"] = region[0]
            monitor["width"] = region[2]
            monitor["height"] = region[3]
        else:
            monitor = sct.monitors[screen_number]
        img = np.array(sct.grab(monitor))
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        return gray


def detect(template, image, threshold):
    """
    Detects the template in the image using TM_CCOEFF_NORMED method.
    """

    # get the width and height of the received image
    img2 = image.copy()
    w, h = template.shape[::-1]
    image = img2.copy()

    # Apply template Matching using TM_CCOEFF_NORMED method
    res = cv.matchTemplate(image,template,cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    top_left = max_loc
    sample = max_val

    # Check if the sample is above the threshold
    if sample > threshold:
        # We found a good enough match!
        return True
    else:
        # No good enough match was found
        return False


def press_key(event_key):
    # Press and release key
    #! The 'keyboard.press_and_release' does instant key presses, which could be detected by the game.
    #TODO: Release the key after a randomized, human-like amount of time.
    #TODO: Investigate further if the keyboard library is the best option for this.
    # Better safe than sorry.
    keyboard.press_and_release(event_key)

def start_fish_detection(template, region, threshold, interval):
    """
    Starts the fishing detection loop.
    First we wait 5 seconds for the player to get ready, then we enter the main loop.
    In the main loop, we will press the fishing key, wait for a couple of seconds 
    (to avoid detecting mistakes before the camera puts the lure in the center), and then
    start the detection loop. The detection loop will run for a maximum of {max_reel_timeout} seconds,
    and if no fish is detected, it will press the fishing key again and end the detection loop.
    If a fish is detected in the detection loop, it will press the fishing key to reel it in and stop the detection loop.
    
    After the detection loop ends, the main loop will wait for {reel_wait} seconds 
    (wait for the reel animation + cooldown) before starting again.

    All key input waits are given a randomized delay to make it a little harder to detect.
    """

    active = True
    # First, wait 5 seconds to get into the game.
    print('Starting in 5 seconds... Switch to the game window, make sure you are looking at fishing spot with the trade skill mode activated.')
    print('Press CTRL+C anytime to stop.')
    time.sleep(5)

    # Then, start the loop.
    while True:

        # press {fishing_key}.
        press_key(fishing_key)
        print(f'Lure thrown! Waiting for lure to settle... ({first_wait} seconds)')

        # wait for {first_wait} seconds.
        first_wait_randomized = randomize_timer(first_wait, 500)
        time.sleep(first_wait_randomized)

        # execute every {interval} seconds
        interval_sum = 0
        while active:
            # grab the screen
            screen = grab_screen(region)

            # detect the template
            res = detect(template, screen, threshold)
            if res:
                active = False
                print('Fish detected! Reeling in...')
                press_key(fishing_key)
            else:
                time.sleep(interval)
                interval_sum += interval
                if interval_sum > max_reel_timeout:
                    print(f'Fish not detected after {max_reel_timeout} seconds. Reeling in...')
                    press_key(fishing_key)
                    active = False
        # End of detection loop

        # wait for {reel_wait} seconds
        print(f'Waiting {reel_wait} seconds before next lure throw...')
        reel_wait_randomized = randomize_timer(reel_wait, 1000)
        time.sleep(reel_wait_randomized)
        active = True

    # End of main loop


# Start the script
main()