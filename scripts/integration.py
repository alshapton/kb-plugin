from typing import Dict

def inject_connect_code(p: str):
    import os
    from pathlib import Path

    from lineinfile import ALWAYS, AfterFirst, add_line_to_file
  
    from scripts.utilities import getnow as getnow
    
    s = os.linesep
    now = getnow()

    line = "    # KB-PLUGIN-CONN                                              #  (KPC)" + s
    line = line + "    # Start of kb-plugin connection code                          #  (KPC)" + s
    line = line + "    # Connected at : " + now + "                   #  (KPC)" + s
    line = line + "    # DO NOT MODIFY THIS CONNECTION CODE                          #  (KPC)" + s
    line = line + "    try:                                                          #  (KPC)" + s
    line = line + "        from kb.plugin import loadModules                         #  (KPC)" + s
    line = line + "        loadModules('commands','','',COMMANDS,DEFAULT_CONFIG,cmd) #  (KPC)" + s
    line = line + "    except ModuleNotFoundError:                                   #  (KPC)" + s
    line = line + "        pass                                                      #  (KPC)" + s
    line = line + "    # End of kb-plugin connection code                            #  (KPC)" + s
    line = line + "    # KB-PLUGIN-CONN                                              #  (KPC)" + s

    add_line_to_file(
        p,
        line,
        inserter=AfterFirst(r"cmd_params = vars"),
        backup=ALWAYS,
        backup_ext=".original",
        )


def outject_connect_code(p: str):
    from pathlib import Path

    from lineinfile import ALWAYS, remove_lines_from_file

    remove_lines_from_file(
        p,
        regexp=r"\b(KPC)\b",
    )


def connect(args: Dict[str, str],path: str):
    import os
    import sys
    
    from pathlib import Path
    
    from kb.filesystem import copy_file
    
    from scripts.utilities import iskbinstalled as iskbinstalled
    from scripts.files import construct_toml_file, write_toml_file, read_toml_file
    
    data = read_toml_file(path)
    isconnected = data['status']['connected']
    if (not isconnected):
        installation_path = iskbinstalled()
        if (installation_path != ''):
            data['status']['connected'] = True
            write_toml_file(data, construct_toml_file(path), 'w')
            installation_dir = os.path.dirname(installation_path)
            here_path = os.path.dirname(path)
            copy_file(str(Path(here_path, 'plugin.py')), str(Path(installation_dir, 'plugin.py')))
            inject_connect_code(installation_path)
            print('Connected to kb instance')
            sys.exit(0)
        else:
            print('Cannot connect to kb - kb is not installed')
            sys.exit(1)
    else:
        print('kb-plugin is already connected to the kb instance')
        sys.exit(1)


def disconnect(args: Dict[str, str], path: str):
    import os
    import sys

    from pathlib import Path

    from kb.filesystem import remove_file

    from scripts.files import construct_toml_file, write_toml_file, read_toml_file

    from scripts.utilities import iskbinstalled as iskbinstalled

    data = read_toml_file(path)
    isconnected = data['status']['connected']
    if (isconnected):
        installation_path = iskbinstalled()
        if (installation_path != ''):
            data['status']['connected'] = False
            write_toml_file(data, construct_toml_file(path), 'w')
            outject_connect_code(installation_path)
            p = os.path.dirname(installation_path)
            remove_file(str(Path(p, 'plugin.py')))
            print('Disconnected from kb instance')
            sys.exit(0)
        else:
            print('Cannot disconnect from kb - kb is not installed')
            sys.exit(1)
    else:
        print('kb-plugin is already disconnected from the kb instance')
        sys.exit(1)