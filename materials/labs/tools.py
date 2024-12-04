import numpy as np
import matplotlib.pyplot as plt
from jupyter_ui_poll import ui_events
import time
import random
from IPython.display import clear_output

from ipywidgets import Button, widgets


class ButtonPoller:
    ui_choice = None
    ui_done = False

    @staticmethod
    def register(btn):
        btn.on_click(ButtonPoller.on_click)

    @staticmethod
    def on_click(btn):
        ButtonPoller.ui_done = True
        ButtonPoller.ui_choice = btn.description

    @staticmethod
    def get_press():
        ButtonPoller.ui_done = False
        with ui_events() as poll:
            while ButtonPoller.ui_done is False:
                poll(10)  # React to UI events (upto 10 at a time)
                time.sleep(0.1)
            ButtonPoller.ui_done = False  # Reset flag for next time

        return ButtonPoller.ui_choice


def annotate(x_data, y_data, filename):
    buttons = []

    for directions in ["Different", "Same", "QUIT"]:
        button = Button(description=directions)
        buttons.append(button)
        ButtonPoller.register(button)

    label_map = {
        "Different": 0,
        "Same": 1,
    }

    n_completed = 0
    while True:
        index = random.randint(0, len(x_data))
        print(x_data[index].shape)
        image = x_data[index].reshape((2, 62, 47))
        plt.subplot(1, 2, 1)
        plt.imshow(image[0], cmap="gray")
        plt.subplot(1, 2, 2)
        plt.imshow(image[1], cmap="gray")

        display(widgets.HBox((buttons)))
        plt.show()
        print(f"Completed {n_completed}")
        x = ButtonPoller.get_press()
        clear_output(wait=True)
        if x == "QUIT":
            break

        with open(filename, "a") as f:
            f.write(f"{index}, {label_map[x]}, {int(y_data[index])}\n")
        n_completed += 1
    return
