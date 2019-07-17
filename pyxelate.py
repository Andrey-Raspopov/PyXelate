import PIL.Image as Image
from imageio import imwrite

from Image import PyImage
from Palettes import Palettes

color_palette = Palettes['bw']

if __name__ == "__main__":
    img = PyImage('test.png', 400, Palettes['bw'])
    img.load()
    img.pyxelate()

    filename_parts = img.filename.rsplit('.', 1)
    filename_parts[0] += '_pixelated'
    filename = '.'.join(filename_parts)
    print("Saving as", filename)
    imwrite(filename, img.data)

    img1 = Image.open(filename)
    img1.thumbnail((img.num_cols, img.num_rows))
    img1.save(filename, 'PNG')
