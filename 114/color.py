import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, 'color_values.py')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/color_values.py',
    color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.color = color
        self.rgb = COLOR_NAMES[self.color.upper()] \
            if self.color.upper() in COLOR_NAMES \
            else None

    @staticmethod
    def hex2rgb(hex_str):
        """Class method that converts a hex value into an rgb one

        Example: input: "#0000ff", output: (0, 0, 255)

        """
        return tuple(int('0x' + hexnum, 16)
                     for hexnum in (hex_str[1:3], hex_str[3:5], hex_str[5:7]))

    @staticmethod
    def rgb2hex(rgb):
        """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
           boundaries (0, 255) and returns its converted hex, for example:
           Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
        if type(rgb) != tuple:
            raise ValueError
        for color_value in rgb:
            if not 0 <= color_value <= 255:
                raise ValueError
        return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

    def __repr__(self):
        """Returns the repl of the object"""
        return f"Color('{self.color}')"

    def __str__(self):
        """Returns the string value of the color object"""
        return str(self.rgb) if self.rgb is not None else 'Unknown'

if __name__ == '__main__':
    print(COLOR_NAMES)
    print(COLOR_NAMES['BROWN'])
