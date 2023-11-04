"""Generic utilities"""
import os
import shutil

root_dir = os.path.abspath(os.curdir)


def create_directory(directory: str):
    """Create a directory
    - Can create a directory three
    - Can create a single directory"""
    path = os.path.join(root_dir, directory)
    if not directory_exists(path):
        os.makedirs(path)


def remove_directory(directory: str):
    """Remove a directory"""
    path = os.path.join(root_dir, directory)
    if directory_exists(path):
        shutil.rmtree(path)


def directory_exists(path) -> bool:
    """Check if a directory exists"""
    return True if os.path.isdir(path) else False


def file_or_directory_exists(path) -> bool:
    """Check if a file or directory exists"""
    return True if os.path.exists(path) else False
