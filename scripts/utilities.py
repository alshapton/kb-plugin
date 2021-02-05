def iskbinstalled():
    try:
        import kb.main
        return kb.main.__file__
    except ModuleNotFoundError:
        return ''


def getnow():
    from datetime import datetime
    return str(datetime.now())

def clear():
    from subprocess import call
    from sys import platform

    if platform not in ('win32', 'cygwin'):
        command = 'clear'
    else:
        command = 'cls'
    call(command)
    return None