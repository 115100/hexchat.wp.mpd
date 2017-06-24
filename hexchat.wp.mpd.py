import subprocess

import hexchat

__module_name__ = 'MPD'
__module_version__ = '0.1.0'
__module_description__ = 'MPD currently playing script'


def now_playing(*dummy):
    proc = subprocess.check_output(['mpc',
                                    'current', '-f', '%artist% - %title% 「%album%」'])
    hexchat.command('SAY np: ' + proc.decode('utf-8').strip())
    return hexchat.EAT_ALL


def unload_callback(dummy):
    hexchat.prnt('RIP MPD wp script')

hexchat.hook_command('wp', now_playing, help='"/wp" to display currently playing MPD track')
hexchat.hook_unload(unload_callback)
hexchat.prnt('hexchat.wp.MPD.py loaded')
