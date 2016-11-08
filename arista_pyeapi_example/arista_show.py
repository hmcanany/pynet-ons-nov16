#!/usr/bin/env python
from pprint import pprint
import pyeapi
import sys

print "\n\nshow interfaces:"
pynet_sw = pyeapi.connect_to("pynet-sw2")
show_int = pynet_sw.enable("show interfaces")
pprint(show_int)
raw_input("\n\nHit a key to continue: ")

print "\n\nshow arp:"
output = pynet_sw.enable("show arp")
pprint(output)
raw_input("\n\nHit a key to continue: ")

print "\n\nshow route:"
output = pynet_sw.enable("show ip route")
pprint(output)
raw_input("\n\nHit a key to continue: ")

print "\n\nshow VLAN:"
output = pynet_sw.enable("show vlan")
output = output[0]['result']['vlans']
pprint(output)
raw_input("\n\nHit a key to continue: ")

print "\n\nVLAN API:"
vlan = pynet_sw.api('vlans')
pprint(vlan.getall())
raw_input("\n\nHit a key to continue: ")
print vlan.get(1)
raw_input("\n\nHit a key to continue: ")
print vlan.get(101)
raw_input("\n\nHit a key to continue: ")
