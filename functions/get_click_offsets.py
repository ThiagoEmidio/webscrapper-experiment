
import io
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from selenium.webdriver.remote.webelement import WebElement
from typing import Callable
from services.log import log

def get_click_offsets(element:WebElement, once=False):
    try:
        fig, ax = plt.subplots()
        def animate(_):
            screenshot = element.screenshot_as_png

            nparr = np.frombuffer(screenshot, np.uint8)
            img = plt.imread(io.BytesIO(nparr))

            ax.imshow(img)
        if once:
            animate(True)
            ani = None
        else:
            ani = FuncAnimation(fig, animate, interval=1000, cache_frame_data=False)

        x, y = None, None

        def on_mouse_click(event):
            nonlocal x, y
            if event.button == 1:
                x, y = event.xdata, event.ydata
                plt.close()

        fig.canvas.mpl_connect('button_press_event', on_mouse_click)

        plt.show(block=False)

        plt.waitforbuttonpress()
        ani.pause()

        if x is None or y is None:
            raise  AssertionError("Não foi possível obter o x ou y")
        if x is not None and y is not None:
            offset_x = x - element.size["width"] / 2
            offset_y = y - element.size["height"] / 2
            return offset_x, offset_y
    except Exception:
        plt.close()
        log.error("Não foi possível obter o x ou y")
        return None, None
    finally:
        plt.close()

def get_click_offsets2(
    element:WebElement,
    callback: Callable[[float | None, float | None], None],
    shouldSkip: Callable[[], bool] = False,
    ):
    def get_screenshot():
        screenshot = element.screenshot_as_png
        nparr = np.frombuffer(screenshot, np.uint8)
        return plt.imread(io.BytesIO(nparr))

    fig, ax = plt.subplots()
    img = ax.imshow(get_screenshot())
    plt.axis("off")
    plt.tight_layout()

    def onclick(event):
        x, y = event.xdata, event.ydata
        if x is None or y is None:
            callback(None, None)
        if x is not None and y is not None:
            offset_x = x - element.size["width"] / 2
            offset_y = y - element.size["height"] / 2
            callback(offset_x, offset_y)

    fig.canvas.mpl_connect("button_press_event", onclick)

    # Update the image every 0.3 seconds
    while plt.get_fignums():
        if shouldSkip():
            break
        img.set_data(get_screenshot())
        plt.pause(0.3)
    plt.close()
    