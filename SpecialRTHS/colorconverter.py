# RGB to Hex color converter

def rgb_to_hex(r, g, b):
    """
    Convert RGB values to a hex color string.
    Args:
        r (int): Red value (0-255)
        g (int): Green value (0-255)
        b (int): Blue value (0-255)
    Returns:
        str: Hex color string in the format '#RRGGBB'
    """
    if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
        raise ValueError("RGB values must be in the range 0-255.")
    return '#{:02X}{:02X}{:02X}'.format(r, g, b)


def hex_to_rgb(hex_str):
    """
    Convert a hex color string to RGB values.
    Args:
        hex_str (str): Hex color string in the format '#RRGGBB' or 'RRGGBB'
    Returns:
        tuple: (r, g, b) where each is an int in 0-255
    """
    hex_str = hex_str.lstrip('#')
    if len(hex_str) != 6:
        raise ValueError("Hex string must be in the format RRGGBB or #RRGGBB.")
    r = int(hex_str[0:2], 16)
    g = int(hex_str[2:4], 16)
    b = int(hex_str[4:6], 16)
    return (r, g, b)


# Example usage:
print(rgb_to_hex(255, 0, 128))  # Output: #FF0080
print(hex_to_rgb('#FF0080'))    # Output: (255, 0, 128)
