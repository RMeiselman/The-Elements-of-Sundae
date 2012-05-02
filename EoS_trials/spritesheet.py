#!/usr/bin/env python

from resource import load_image

class SpriteSheet(object):
    def __init__(self, image, dimensions, colorkey =-1):
        
        if type(image) is str:
            image = load_image(image)

        if colorkey == -1:
            colorkey = image.get_at((0,0))

        if colorkey:
            image.set_colorkey(colorkey)

        cols, rows = dimensions
        w = self.width = 1.0 * image.get_width() / cols
        h = self.height = 1.0 * image.get_height() / rows

        self._images = []
        for y in range(rows):
            ros = []
            for x in range(cols):
                row.append(image.subsurface((x*w, y*h, w, h)))
            self._images.append(row)

    def get(self, x, y):
        return self._images[y][x]
