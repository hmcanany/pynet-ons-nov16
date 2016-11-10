#!/usr/bin/env python
import django
from net_system.models import NetworkDevice, Credentials

def main():
    django.setup()
    devices = NetworkDevice.objects.all()
    for a_device in devices:
        if "wrong_OS" in a_device.device_type:
            a_device.delete()

    devices = NetworkDevice.objects.all()
    for a_device in devices:
        print a_device, a_device.vendor

if __name__ == "__main__":
    main()
