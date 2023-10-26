"""Generic utilities"""
import os
import shutil

root_dir = os.path.abspath(os.curdir)


def create_directory(directory: str):
    """Create a directory
    - Can create a directory three
    - Can create a single directory"""
    parent_dir = root_dir
    path = os.path.join(parent_dir, directory)
    os.makedirs(path)


def remove_directory(directory: str):
    """Remove a directory"""
    parent_dir = root_dir
    path = os.path.join(parent_dir, directory)
    shutil.rmtree(path)
