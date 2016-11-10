#!/usr/bin/env python
import django
from net_system.models import NetworkDevice, Credentials


def main():
    '''
    Create two new test NetworkDevices in the database. Use both direct object creation
    and the .get_or_create() method to create the devices.
    '''
    django.setup()
    # Example object creation
    Dummy_Dev1 = NetworkDevice(
        device_name='Dummy_Dev1',
        device_type='wrong_OS',
        ip_address='13.13.13.13',
        port=22,
        )
    Dummy_Dev1.save()

    # Example object creation using get_or_create
    Dummy_Dev2 = NetworkDevice.objects.get_or_create(
        device_name='Dummy_Dev2',
        device_type='wrong_OS',
        ip_address='14.14.14.14',
        port=8022,
    )
    # Verify devices that currently exist
    print
    devices = NetworkDevice.objects.all()
    for a_device in devices:
        print a_device
    print

if __name__ == "__main__":
    main()
