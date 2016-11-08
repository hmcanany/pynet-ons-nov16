#!/usr/bin/env python
from pprint import pprint
import pyeapi
import sys

###show_run = pynet_sw.running_config
###print show_run

print "\n\nConfig VLAN 901:"
pynet_sw = pyeapi.connect_to("pynet-sw2")
return_val = pynet_sw.config(['vlan 901', 'name red'])
print return_val
raw_input("\n\nHit a key to continue: ")


print "\n\nVLAN API:"
vlan = pynet_sw.api('vlans')
vlan.create(902)
vlan.set_name(902, name='blue')
raw_input("\n\nHit a key to continue: ")

print "\n\nVLAN 902 Status:"
print vlan.get(902)

#set_state
#set_trunk_groups

# Other APIs
#intf = pynet_sw.api('switchports')

print "\n\nSave Config"
pynet_sw.enable("write memory")
