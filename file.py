""" file.py """
from typing import Union
import os
import json

def replace(file_name: str, content: Union[list, dict]) -> None:
    """Replace a json file an existing file

    Args:
        file_name (str): File name or path
        content (list | dict ) File content.
    """
    os.remove(file_name)
    if len(content) > 0:
        create(file_name, content)


def create_or_update(file_name: str, content: Union[list, dict] = None) -> None:
    """Create a new json file or Updates an existing file

    Args:
        file_name (str): File name or path
        content (list | dict, optional): File content. Defaults to None.
    """

    if os.path.isfile(file_name):
        if valid_json_file(file_name):
            update(file_name, content)
        else:
            create(file_name, content)
    else:
        create(file_name, content)

def valid_json_file(file_name:str) -> bool:
    """Verfify is a valid json file

    Args:
        file_name (str): File name or path
    """
    try:
        file = open(file_name, encoding="utf-8")
        json.loads(file.read())
        file.close()
        return True
    except ValueError as error:
        print(error)
        os.remove(file_name)
        return False

def create(file_name: str, content: Union[list, dict] = None) -> None:
    """Create a new json file

    Args:
        file_name (str): File name or path
        content (list | dict, optional): File content. Defaults to None.
    """
    mode = "w" if content else "x"

    try:
        file = open(file_name, mode, encoding="utf-8")

    except FileExistsError as error:
        raise OSError(f"File '{file_name}' already exists") from error

    except PermissionError as error:
        raise OSError(f"You do not hav permisson to create '{file_name}'") from error

    if content and isinstance(content, (list, dict)):
        content = json.dumps(content)
        file.write(content)

    file.close()


def update(file_name: str, content: Union[list, dict]) -> None:
    """Updates an existing file

    Args:
        file_name (str): File name or path
        content (list | dict): File content.
    """
    if not (isinstance(content, dict) or isinstance(content, list)) or content == "":
        raise ValueError("'content' argument must be specified")

    file = open(file_name, encoding="utf-8")
    file_content = json.loads(file.read())
    file.close()

    if isinstance(file_content, list):
        if isinstance(content, dict):
            file_content.append(content)

        elif isinstance(content, list):
            file_content += content

    elif isinstance(file_content, dict):
        if isinstance(content, dict):
            file_content = [file_content, content]

        elif isinstance(content, list):
            file_content = [file_content] + content

    file = open(file_name, "w", encoding="utf-8")
    file.write(json.dumps(file_content))
    file.close()


def read(file_name: str) -> Union[list, dict]:
    """Returns the content of a text file

    Args:
        file_name (str): File name or path

    Returns(str): File content
    """
    try:
        file = open(file_name, encoding="utf-8")
        file_content = json.loads(file.read())
        file.close()
        return file_content
    except ValueError as error:
        raise OSError(f"File '{file_name}' is invalid json") from error
