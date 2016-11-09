"""
pynet-rtr1 (Cisco IOS)  184.105.247.70
pynet-rtr2 (Cisco IOS)  184.105.247.71
pynet-sw1  (Arista EOS) 184.105.247.72
pynet-sw2  (Arista EOS) 184.105.247.73
juniper-srx             184.105.247.76
nxos-spine1             nxos1.twb-tech.com
nxos-spine2             nxos2.twb-tech.com
"""
from getpass import getpass

std_pwd = getpass("Enter standard password: ")
arista_pwd = getpass("Enter Arista password: ")

pynet_rtr1 = {
    'device_type' : 'ios',
    'hostname' : '184.105.247.70',
    'username' : 'pyclass',
    'password' : std_pwd,
    'optional_args' : {},
}

pynet_rtr2 = {
    'device_type' : 'ios',
    'hostname' : '184.105.247.71',
    'username' : 'pyclass',
    'password' : std_pwd,
    'optional_args' : {},
}

pynet_sw1 = {
    'device_type' : 'eos',
    'hostname' : '184.105.247.72',
    'username' : 'pyclass',
    'password' : arista_pwd,
    'optional_args' : {},
}

pynet_sw2 = {
    'device_type' : 'eos',
    'hostname' : '184.105.247.73',
    'username' : 'pyclass',
    'password' : arista_pwd,
    'optional_args' : {},
}

juniper_srx = {
    'device_type' : 'junos',
    'hostname' : '184.105.247.76',
    'username' : 'pyclass',
    'password' : std_pwd,
    'optional_args' : {},
}

nxos1 = {
    'device_type' : 'nxos',
    'hostname' : 'nxos1.twb-tech.com',
    'username' : 'pyclass',
    'password' : std_pwd,
    'optional_args' : {'nxos_protocol' : 'https', 'port' : 8443},
}

nxos2 = {
    'device_type' : 'nxos',
    'hostname' : 'nxos2.twb-tech.com',
    'username' : 'pyclass',
    'password' : std_pwd,
    'optional_args' : {'nxos_protocol' : 'https', 'port' : 8443},
}

device_list = [
        pynet_rtr1,
        pynet_rtr2,
        pynet_sw1,
        pynet_sw2,
        juniper_srx,
        nxos1,
        nxos2,
]
