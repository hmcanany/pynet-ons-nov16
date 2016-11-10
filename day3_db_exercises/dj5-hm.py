#!/usr/bin/env python
import django
from net_system.models import NetworkDevice, Credentials
from netmiko import ConnectHandler
from datetime import datetime

#def save_file(filename, show_version):
#    """Save the show version to a file"""
#    with open(filename, "a") as f:
#        f.write(show_version_output)

def show_version(a_device):
    '''
    Execute show version command using Netmiko
    '''
    creds = a_device.credentials
    remote_conn = ConnectHandler(device_type=a_device.device_type,
                                 ip=a_device.ip_address,
                                 username=creds.username,
                                 password=creds.password,
                                 port=a_device.port, secret='')
    print
    print '@' * 80
    show_ver_output = remote_conn.send_command_expect("show version") 
    print show_ver_output
    print '*-' * 40
    print
    def save_file(filename, show_version):
        """Save the show version to a file"""
        with open(filename, "a") as f:
            f.write(show_version_output)
    return (show_ver_output)

def main():
    '''
    Use Netmiko to connect to each of the devices in the database. Execute
    'show version' on each device.
    '''
    django.setup()

    starttime = datetime.now()
    devices = NetworkDevice.objects.all()
    for a_device in devices:
        output = show_version(a_device)
        save_file(filename, output)
    elapsed_time = datetime.now() - starttime
    print "Elapsed time: {}".format(elapsed_time)
    filename = "show_versions.txt"
    print "Saving show version output to file...: {}\n".format(filename)

if __name__ == "__main__":
    main()
