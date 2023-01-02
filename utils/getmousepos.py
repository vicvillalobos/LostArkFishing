import pyautogui, time

screen_resolution = (2560, 1080)

def get_mouse_pos():
    pos = pyautogui.position()

    # convert to relative coordinates from center of the screen
    x = pos[0] - screen_resolution[0] / 2
    y = pos[1] - screen_resolution[1] / 2

    return (x, y)


def get_relative_position(position, reference):
    """
    Get the entered position relative to the reference point.
    """
    return (position[0] - reference[0], position[1] - reference[1])

while True:
    #print(get_relative_position(get_mouse_pos(), (1203, -335)))
    print(get_mouse_pos())
    time.sleep(1)