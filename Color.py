import numpy as np


class Color(np.ndarray):
    def __new__(cls, arr):
        self = np.asarray(arr).view(cls)
        return self

    def __hash__(self):
        return hash(self.tostring())
