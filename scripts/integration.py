# -*- encoding: utf-8 -*-
# kb-plugin v0.0.1
# A plugin manager for kb
# Copyright © 2021, alshapton.
# See /LICENSE for licensing information.

"""
kbplugin integration  module

:Copyright: © 2021, alshapton.
:License: GPLv3 (see /LICENSE).
"""


from typing import Dict


def inject_connect_code(p: str):
    """
    Insert the plugin hook code for the plugin manager .

    Arguments:
    p           -   a string containing the filename of the
                    target plugin_main.py file

    Return:     -   True
    """
    import os

    from lineinfile import ALWAYS, AfterFirst, add_line_to_file

    from scripts.utilities import getnow as getnow

    s = os.linesep
    now = getnow()

    # Set up the "line" to inject into the plugin_main.py file
    # Ignore line lengthd
    line = "    # KB-PLUGIN-CONN                                              #  (KPC)" + s         # noqa: E501
    line = line + "    # Start of kb-plugin connection code                          #  (KPC)" + s  # noqa: E501
    line = line + "    # Connected at : " + now + "                   #  (KPC)" + s                 # noqa: E501
    line = line + "    # DO NOT MODIFY THIS CONNECTION CODE                          #  (KPC)" + s  # noqa: E501
    line = line + "    try:                                                          #  (KPC)" + s  # noqa: E501
    line = line + "        from kb.plugin import loadModules                         #  (KPC)" + s  # noqa: E501
    line = line + "        loadModules('commands','','',COMMANDS,DEFAULT_CONFIG,cmd) #  (KPC)" + s  # noqa: E501
    line = line + "    except ModuleNotFoundError:                                   #  (KPC)" + s  # noqa: E501
    line = line + "        pass                                                      #  (KPC)" + s  # noqa: E501
    line = line + "    # End of kb-plugin connection code                            #  (KPC)" + s  # noqa: E501
    line = line + "    # KB-PLUGIN-CONN                                              #  (KPC)" + s  # noqa: E501
    # There is a comment at the end of each line to aid removal

    # Inject hook code
    add_line_to_file(p, line, inserter=AfterFirst(r"cmd_params = vars"),
                     backup=ALWAYS, backup_ext=".original",)

    return True


def outject_connect_code(p: str):
    """
    Remove the plugin hook code from the plugin manager .

    Arguments:
    p           -   a string containing the filename of the
                    target plugin_main.py file

    Return:     -   True
    """
    from lineinfile import remove_lines_from_file

    # Remove the connectivity code based on the comment (KPC)
    remove_lines_from_file(p, regexp=r"\b(KPC)\b",)
    return True


def connect(args: Dict[str, str], path: str):
    """
    Connect the plugin manager to the main kb infrastructure.

    Arguments:
    args        -   Dictionary containing the command-line arguments
                    (not used but needs to be there)
    path        -   toml file of the kbplugin configuration

    Return:     -   N/A
    """
    import os
    import sys

    from pathlib import Path

    from kb.filesystem import copy_file

    from scripts.utilities import iskbinstalled as iskbinstalled
    from scripts.files import construct_toml_file, write_toml_file, \
        read_toml_file

    data = read_toml_file(path)
    isconnected = data['status']['connected']
    if (not isconnected):
        installation_path = iskbinstalled()
        if (installation_path != ''):
            data['status']['connected'] = True
            write_toml_file(data, construct_toml_file(path), 'w')
            installation_dir = os.path.dirname(installation_path)
            here_path = os.path.dirname(path)
            copy_file(str(Path(here_path, 'plugin.py')),
                      str(Path(installation_dir, 'plugin.py')))
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
    """
    Disconnect the plugin manager from the main kb infrastructure.

    Arguments:
    args        -   Dictionary containing the command-line arguments
                    (not used but needs to be there)
    path        -   toml file of the kbplugin configuration

    Return:     -   N/A
    """
    import os
    import sys

    from pathlib import Path

    from kb.filesystem import remove_file

    from scripts.files import construct_toml_file, \
        write_toml_file, read_toml_file

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

def stat(args: Dict[str, str], path: str):
    from kb.printer.style import BOLD, UND, RESET
    from scripts.utilities import iskbinstalled as iskbinstalled
    from scripts.files import read_toml_file as read_toml_file
    PREFIX = ''
    SUFFIX = ''
    UPREFIX = ''

    if iskbinstalled():
        from kb import __version__ as kb_version
        data = read_toml_file(path)
        isconnected = data['status']['connected']
        if args['no_color']:
            PREFIX = BOLD
            SUFFIX = RESET
            UPREFIX = BOLD + UND

        if (isconnected):
            connectedtext = 'Connected'
        else:
            connectedtext = 'Disconnected'
    else:
        connectedtext = 'Not Installed'
        kb_version = connectedtext

    kb_plugin_version = read_toml_file(path)['info']['version']
    line1 = UPREFIX + "kb-plugin Status Information" + SUFFIX
    line2 = PREFIX + "kb-plugin Version  : " + kb_plugin_version + SUFFIX
    line3 = PREFIX + "kb Version         : " + kb_version + SUFFIX
    line4 = PREFIX + "Status             : " + connectedtext + SUFFIX

    print(line1)
    print(line2)
    print(line3)
    print(line4)
