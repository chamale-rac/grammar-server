import base64
import os


def readFile(file_path: str) -> list[str]:
    """
    Reads the lines of a file and returns them as a list of strings.

    Args:
        file_path (str): The path to the file to read.

    Returns:
        list[str]: A list of strings representing the lines of the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().splitlines()


def fileInPath(file_path: str) -> bool:
    """
    Checks if a file exists in the given path.

    Args:
        file_path (str): The path to the file.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.isfile(file_path)


def extract_svg_height_width(svg_string, HEIGHT_REGEX, WIDTH_REGEX):
    '''
    Extracts the height and width of an svg string.
    '''
    height_match = HEIGHT_REGEX.search(svg_string)
    width_match = WIDTH_REGEX.search(svg_string)
    if height_match is None or width_match is None:
        return None, None
    height = float(height_match.group(1))
    if height_match.group(2) == 'pt':
        height *= 1.25
    width = float(width_match.group(1))
    if width_match.group(2) == 'pt':
        width *= 1.25
    return height, width


def to_base64(svg_string, HEIGHT_REGEX, WIDTH_REGEX):
    '''
    Converts an svg string to base64.
    '''
    height, width = extract_svg_height_width(
        svg_string.decode('utf-8'),  HEIGHT_REGEX, WIDTH_REGEX)
    return base64.b64encode(svg_string).decode('utf-8'), width, height
