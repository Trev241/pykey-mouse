import time

from pynput.keyboard import Key, Listener
from pynput.mouse import Controller

SENSITIVITY = 1
INPUT_KEYS = set([Key.left, Key.right, Key.up, Key.down])
X_OFFSET = {Key.left: -1, Key.right: 1}
Y_OFFSET = {Key.up: -1, Key.down: 1}


class InputMapper:
    def __init__(self):
        self.keys_down = set()
        self.dx = 0
        self.dy = 0

        self.mouse = Controller()

    def update(self):
        self.mouse.move(self.dx * SENSITIVITY, self.dy * SENSITIVITY)

    def on_press(self, key):
        if key not in INPUT_KEYS:
            return

        if key not in self.keys_down:
            self.keys_down.add(key)
            self.dx += X_OFFSET.get(key, 0)
            self.dy += Y_OFFSET.get(key, 0)

    def on_release(self, key):
        if key in INPUT_KEYS:
            self.keys_down.remove(key)
            self.dx -= X_OFFSET.get(key, 0)
            self.dy -= Y_OFFSET.get(key, 0)


input_mapper = InputMapper()
with Listener(
    on_press=input_mapper.on_press, on_release=input_mapper.on_release
) as listener:
    while True:
        input_mapper.update()
        time.sleep(0.005)

    listener.join()
