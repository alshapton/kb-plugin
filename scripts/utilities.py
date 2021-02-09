# -*- encoding: utf-8 -*-
# kb-plugin v0.0.1
# A plugin manager for kb
# Copyright © 2021, alshapton.
# See /LICENSE for licensing information.

"""
kbplugin utilities  module

:Copyright: © 2021, alshapton.
:License: GPLv3 (see /LICENSE).
"""


def iskbinstalled():
    """
    Determining if kb is installed.

    Return
    kb installed        :       the location of the kb installation
    kb not installed    :       ''
    """
    try:
        import kb.main
        return kb.main.__file__
    except ModuleNotFoundError:
        return ''


def getnow():
    """
    Return current date/time.

    Return
    Date/Time in    2021-02-09 13:40:06.803692
                    YYYY-mm-DD HH:MM:ss.ffffff
    """
    from datetime import datetime
    return str(datetime.now())


def clear():
    """
    Platform-independent clear terminal screen.

    Return
            N/A
    """
    from subprocess import call
    from sys import platform

    if platform not in ('win32', 'cygwin'):
        command = 'clear'
    else:
        command = 'cls'
    call(command)
    return None
