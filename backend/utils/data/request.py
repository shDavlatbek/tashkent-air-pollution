import os
import requests

def download_file(url: str, filename: str = None) -> str:
    """
    Downloads a file from the given URL to the root folder of the project.

    Args:
        url (str): The URL to download the file from.
        filename (str, optional): The name to save the file as. Defaults to the last part of the URL.

    Returns:
        str: The path to the downloaded file.
    """
    if not filename:
        filename = os.path.basename(url)
    filepath = os.path.join(os.getcwd(), filename)

    response = requests.get(url)
    response.raise_for_status()

    with open(filepath, 'wb') as file:
        file.write(response.content)

    return filepath