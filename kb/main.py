# -*- encoding: utf-8 -*-
# kb v0.1.5
# A knowledge base organizer
# Copyright © 2020, gnc.
# See /LICENSE for licensing information.

"""
kb main module

:Copyright: © 2020, gnc.
:License: GPLv3 (see /LICENSE).
"""

__all__ = ()

import sys

from kb.cl_parser import parse_args
from kb.config import DEFAULT_CONFIG

from kb.commands.add import add
from kb.commands.base import base
from kb.commands.delete import delete
from kb.commands.edit import edit
from kb.commands.erase import erase
from kb.commands.export import export
from kb.commands.grep import grep
from kb.commands.ingest import ingest
from kb.commands.kbinfo import kbinfo
from kb.commands.search import search
from kb.commands.template import template
from kb.commands.update import update
from kb.commands.view import view

COMMANDS = {
    'add': add,
    'base': base,
    'delete': delete,
    'edit': edit,
    'erase': erase,
    'export': export,
    'grep': grep,
    'import': ingest,
    'list': search,
    'stats': kbinfo,
    'template': template,
    'update': update,
    'view': view,
}



def dispatch(function, *args, **kwargs):
    """
    Dispatch command line action to proper
    kb function
    """
    return COMMANDS[function](*args, **kwargs)


def main():
    """Main routine of kb."""

    args = parse_args(sys.argv[1:])
    cmd = args.command
    cmd_params = vars(args)
    # KB-PLUGIN-CONN                                              #  (KPC)
    # Start of kb-plugin connection code                          #  (KPC)
    # Connected at : 2021-01-30 23:00:53.882984                   #  (KPC)
    # DO NOT MODIFY THIS CONNECTION CODE                          #  (KPC)
    try:                                                          #  (KPC)
        from kb.plugin import loadModules                         #  (KPC)
        loadModules('commands','','',COMMANDS,DEFAULT_CONFIG,cmd) #  (KPC)
    except ModuleNotFoundError:                                   #  (KPC)
        pass                                                      #  (KPC)
    # End of kb-plugin connection code                            #  (KPC)
    # KB-PLUGIN-CONN                                              #  (KPC)
    dispatch(cmd, cmd_params, config=DEFAULT_CONFIG)

