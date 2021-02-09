# -*- encoding: utf-8 -*-
# kb-plugin v0.0.1
# A plugin manager for kb
# Copyright © 2021, alshapton.
# See /LICENSE for licensing information.

"""
kbplugin files module

:Copyright: © 2021, alshapton.
:License: GPLv3 (see /LICENSE).
"""


def construct_toml_file(file: str):
    """
    Construct the path for the base configuration file.

    Arguments:
    file        -   a string containing a file with no .toml extension

    Return:
                -   a string with the complete filename with
                    the .toml extension
    """
    return str(file + '.toml')


def write_toml_file(data: str, path: str, mode: str):
    """
    Write/append data to a toml file.

    Arguments:
    data    -   the data to write to the file.
    path    -   the path of the filename
    mode    -   'w' for write, 'a' for append

    Return  -   True
    """
    import toml
    # Write information to the .toml file.
    with open(path, mode) as tcf:
        tcf.write(toml.dumps(data))
    return True


def read_toml_file(path: str):
    """
    Read a given toml file
    Arguments:
    path    -   the path of the filename

    Return  -   the data from the file in a dictionary format
    """
    import toml
    data = toml.load(construct_toml_file(path))
    return (data)


def write_file(data: str, path: str, mode: str):
    """
    Write data to a file.
    Arguments:
    data    -   the data to write to the file.
    path    -   the path of the filename
    mode    -   'w' for write, 'a' for append

    Return  -   True
    """
    f = open(path, mode)
    f.write(data)
    f.close()
    return True


def read_file(file: str):
    """
    Read data from a file.
    Arguments:
    file    -   the path of the filename

    Return  -   the data from the file in a dictionary format
    """
    fhandle = open(file, "r")
    data = fhandle.read()
    fhandle.close()
    return data


def append_file(file1: str, file2: str):
    """
    Append one file to another.
    Arguments:
    file1   -   the path of the first filename
    file2   -   the path of the second filename to append to the first

    Return  -   None
    """
    fin = open(file1, "r")
    data2 = fin.read()
    fin.close()

    fout = open(file2, "a")
    fout.write(data2)
    fout.close()
    return None


def create_structure(base_dir: str, plugin_name: str):
    """
    Create a directory structure to hold the plugin code

    Arguments:
    base_dir    -   the path for the directory structure
    plugin_name -   name of the plugin to use as the root
                    of the directory structure

    Return      -   None
    """
    from pathlib import Path

    from kb.filesystem import create_directory, touch_file

    # Create specific plugin named directories
    plugin_dir = Path(base_dir, 'plugins', plugin_name)
    create_directory(Path(plugin_dir, 'actions'))
    create_directory(Path(plugin_dir, 'api'))
    create_directory(Path(plugin_dir, 'commands'))
    create_directory(Path(plugin_dir, 'printer'))

    # Populate with __init__.py files to enable package recognition
    touch_file(Path(plugin_dir, '__init__.py'))
    touch_file(Path(plugin_dir, 'actions', '__init__.py'))
    touch_file(Path(plugin_dir, 'api', '__init__.py'))
    touch_file(Path(plugin_dir, 'commands', '__init__.py'))
    touch_file(Path(plugin_dir, 'printer', '__init__.py'))

    return None
