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
