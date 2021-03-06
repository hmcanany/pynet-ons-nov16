#!/usr/bin/env python
"""
Execute 'show interfaces' on the Arista switch using eapi.
Extract the interfaceCounters inOctets/outOctets for all the interfaces
that have this information.
"""
from pprint import pprint
import pyeapi

def main():
    """
    Use eapi to retrieve 'show ip route' from your arista switch.
    From the returned data structure retrieve the prefixes, the output
    interfaces, and the next hops (if available).
    Print these routes and the associated information to stdout.
    """
    pynet_sw = pyeapi.connect_to("pynet-sw3")
    show_int = pynet_sw.enable("show interfaces")
    show_int = show_int[0]['result']['interfaces']
    print "\n{:>15} {:>15} {:>15}".format("Interface", "inOctets", "outOctets")
    sep = '-' * 15
    print "{:>15} {:>15} {:>15}".format(sep, sep, sep)
    for intf, v in show_int.items():
        intf_counters = v.get('interfaceCounters', 'N/A')
        if intf_counters != 'N/A':
            in_octets = intf_counters.get('inOctets')
            out_octets = intf_counters.get('outOctets')
        else:
            in_octets = 0
            out_octets = 0
        print "{:>15} {:>15} {:>15}".format(intf, in_octets, out_octets)
    print
    
if __name__ == "__main__":
    main()
