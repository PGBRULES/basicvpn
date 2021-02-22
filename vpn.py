import os
import psutil
from pathlib import Path
def killovpn():  
    cmd = 'start C:\\"Program Files"\OpenVPN\\bin\openvpn-gui.exe --command exit'
    os.system(cmd)
def vpn_connect(location):
    selfdir = str(Path(__file__).parent.absolute())
    configdir = selfdir + '\\' + location + '.ovpn'
    killovpn()
    cmd = 'start C:\\"Program Files"\OpenVPN\\bin\openvpn-gui.exe --config_dir ' + selfdir + ' --connect ' + location
    os.system(cmd)
vpn_connect('test')
