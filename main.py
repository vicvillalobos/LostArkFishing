import cv2 as cv
import numpy as np
# from matplotlib import pyplot as plt
from mss import mss
import time
import keyboard
import random

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

def main():
    default_region = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}
    # square region in the center of the screen, 300x300
    region = (int(1920/2-150), int(1080/2-150), 300, 300)

    # load the template
    template = cv.imread('template.png',0)

    start_fish_detection(template, region, template_threshold, detection_interval)

def randomize_timer(timer, range_ms):
    '''
    Returns timer + a random number between -range_ms and range_ms, all divided by 1000.
    '''
    return timer + (random.randint(-range_ms, range_ms) / 1000)

def grab_screen(region=None):
    with mss() as sct:
        if region:
            monitor = sct.monitors[1]
            monitor["top"] = region[1]
            monitor["left"] = region[0]
            monitor["width"] = region[2]
            monitor["height"] = region[3]
        else:
            monitor = sct.monitors[1]
        img = np.array(sct.grab(monitor))
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        return gray


def detect(template, image, threshold):
    # image = cv.imread('screenshot_sm_fish.png',0)
    img2 = image.copy()
    # template = cv.imread('template.png',0)
    w, h = template.shape[::-1]
    # All the 6 methods for comparison in a list
    methods = ['cv.TM_CCOEFF_NORMED']
    for meth in methods:
        image = img2.copy()
        method = eval(meth)
        # Apply template Matching
        res = cv.matchTemplate(image,template,method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
            sample = 1 - min_val
        else:
            top_left = max_loc
            sample = max_val

        # matchStr = 'Not found'
        if sample > threshold:
            bottom_right = (top_left[0] + w, top_left[1] + h)
            cv.rectangle(image,top_left, bottom_right, 255, 2)
            # matchStr = 'Detected Point'
            print(f"Fish found at {top_left} by {meth} with {sample}")
            return True
        else:
            # print(f"Fish not found by {meth} with {sample}")
            return False


def press_key(event_key):
    # Press and release key
    keyboard.press_and_release(event_key)

def start_fish_detection(template, region, threshold, interval):

    active = True
    # First, wait 5 seconds to get into the game.
    print('Starting in 5 seconds...')
    time.sleep(5)

    # Then, start the loop.
    while True:

        # press {fishing_key}.
        press_key(fishing_key)
        print('Lure thrown! Waiting for lure to settle... ({first_wait} seconds)')

        # wait for {first_wait} seconds.
        first_wait_randomized = randomize_timer(first_wait, 500)
        time.sleep(first_wait_randomized)

        print('Detection started!')
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
        
        print('Detection ended!')

        # wait for {reel_wait} seconds
        print(f'Waiting {reel_wait} seconds before next lure throw...')
        reel_wait_randomized = randomize_timer(reel_wait, 1000)
        time.sleep(reel_wait_randomized)
        active = True

main()