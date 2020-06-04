"""What can be done?!"""
import numpy as np
import pynput.mouse as m
import pynput.keyboard as k
import pyautogui
import cv2


REFRESH_BUTTON = cv2.imread('./data/refresh_button.png')
WIDTH, HEIGHT, _ = REFRESH_BUTTON.shape[:]

MOUSE = m.Controller()


def on_press(key):
    print('{0} pressed'.format(key))


def on_release(key):
    print('{0} release'.format(key))
    if key == k.Key.ctrl_l:
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        # cv2.imwrite("in_memory_to_disk.png", image)

        res = cv2.matchTemplate(screenshot, REFRESH_BUTTON, cv2.TM_SQDIFF)
        out = cv2.minMaxLoc(res)

        MOUSE.position = (out[2][0] + WIDTH / 2, out[2][1] + HEIGHT / 2)

        MOUSE.press(m.Button.left)
        MOUSE.release(m.Button.left)

    if key == k.Key.esc:
        # Stop listener
        return False


# blocking
with k.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

"""
# non-blocking:

listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
listener.start()
"""
