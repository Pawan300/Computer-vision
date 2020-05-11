import cv2
import numpy as np


class Invisible:
    def __init__(self, background):
        self.background = background

    def process(self, frame, rectangle):
        print(rectangle)
        x = rectangle[0][0]
        y = rectangle[0][1]
        z = rectangle[0][2]
        h = rectangle[0][3]
        mask = np.zeros(frame.shape)
        a = 2
        x = x - a
        y = y - a
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        mask[y: h + a, x: z + a] = 255
        frame[np.where(mask == 255)] = self.background[np.where(mask == 255)]
        return frame
