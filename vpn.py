import subprocess
import os
import psutil
from pathlib import Path
def killovpn():  
    for proc in psutil.process_iter():
        if any(procstr in proc.name() for procstr in\
            ['Openvpn', 'openvpn-gui.exe', 'openvpn-gui', 'awooogatest']):
            proc.kill()
def vpn_connect(location):
    location_local = location
    selfdir = str(Path(__file__).parent.absolute())
    configdir = selfdir + '\\' + location + '.ovpn'
    killovpn()
    cmd = 'start C:\\"Program Files"\OpenVPN\\bin\openvpn-gui.exe --config_dir ' + selfdir + ' --connect ' + location
    os.system(cmd)
vpn_connect('test')
