def construct_toml_file(file: str):
    return str(file + '.toml')


def write_toml_file(data: str, path: str, mode: str):
    """
    Write the config to the kbplugin.toml file.
    Argument:
    data    -   the data to write to the file.
    """
    import toml
    # Write information to the .toml file.
    with open(path, mode) as tcf:
        tcf.write(toml.dumps(data))
    return True


def read_toml_file(path: str):
    import toml
    data = toml.load(construct_toml_file(path))
    return (data)


def write_file(data: str, path: str, mode: str):
    """
    Write data to a file.
    Argument:
    data    -   the data to write to a file.
    """
    f = open(path, mode)
    f.write(data)
    f.close()
    return True


def create_structure(base_dir: str, plugin_name: str):
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


def append_file(file1: str, file2: str):
    fin = open(file1, "r")
    data2 = fin.read()
    fin.close()

    fout = open(file2, "a")
    fout.write(data2)
    fout.close()
    return None

def read_file(file: str):
    fhandle = open(file, "r")
    data = fhandle.read()
    fhandle.close()
    return data
