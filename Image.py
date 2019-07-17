import numpy as np
from PIL import Image as Image

from Color import Color


class PyImage:
    def __init__(self, fn, cols, palette):
        self.filename = fn
        self.palette = palette
        self.img = None
        self.num_cols = cols
        self.num_rows = 0
        self.square_h = 0
        self.square_w = 0
        self.data = None

    def load(self):
        self.img = Image.open(self.filename)
        self.data = np.array(self.img)
        self.square_w = float(self.data.shape[1]) / self.num_cols
        self.num_rows = int(round(self.data.shape[0] / self.square_w))
        self.square_h = float(self.data.shape[0]) / self.num_rows

    def all_square_pixels(self, row, col):
        for y in range(int(round(row * self.square_h)), int(round((row + 1) * self.square_h))):
            for x in range(int(round(col * self.square_w)), int(round((col + 1) * self.square_w))):
                yield y, x

    def make_one_square(self, row, col):
        pixels = []

        for y, x in self.all_square_pixels(row, col):
            pixels.append(np.array(self.data[y][x]))

        result = self.palette.min_color_distance(Color(np.mean(np.array(pixels), axis=0)))

        for y, x in self.all_square_pixels(row, col):
            self.data[y][x] = result

    def pyxelate(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.make_one_square(row, col)