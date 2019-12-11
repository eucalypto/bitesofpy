def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    for color_value in rgb:
        if not 0 <= color_value <= 255:
            raise ValueError
    return f"#{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}"
