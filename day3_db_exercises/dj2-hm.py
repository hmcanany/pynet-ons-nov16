#!/usr/bin/env python
import django
from net_system.models import NetworkDevice, Credentials

def main():
    '''
    Set the vendor field for each NetworkDevice to the appropriate vendor. Save
    this field to the database.
    '''
    django.setup()
    devices = NetworkDevice.objects.all()
    for a_device in devices:
        if 'cisco' in a_device.device_type:
            a_device.vendor = "Cisco"
        elif 'arista' in a_device.device_type:
            a_device.vendor = "Arista"
        elif 'juniper' in a_device.device_type:
            a_device.vendor = "Juniper"
        a_device.save()

    for a_device in devices:
        print a_device, a_device.vendor

if __name__ == "__main__":
    main()
