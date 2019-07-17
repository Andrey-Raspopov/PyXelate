from Color import Color
from scipy.spatial import KDTree


class Palette(list):
    def __init__(self, arr):
        super(Palette, self).__init__(map(Color, arr))
        self.tree = KDTree(arr)

    def min_color_distance(self, color):
        distance, result = self.tree.query(color)
        return self[result]
