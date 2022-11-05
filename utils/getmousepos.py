import pyautogui, time

screen_resolution = (2560, 1080)

def get_mouse_pos():
    pos = pyautogui.position()

    # convert to relative coordinates from center of the screen
    x = pos[0] - screen_resolution[0] / 2
    y = pos[1] - screen_resolution[1] / 2

    return (x, y)

while True:
    print(get_mouse_pos())
    time.sleep(1)