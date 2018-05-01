#!/usr/bin/env python3
import argparse
import xml.etree.ElementTree as ET

def get_dhcpd(root):
    for child in root:
        if child.tag == 'dhcpd':
            return child

def get_pf_mappings(fname):
    host_keys = ['mac', 'hostname', 'ipaddr', 'descr']
    tree = ET.parse(fname)
    root = tree.getroot()
    dhcpd = get_dhcpd(root)
    
    interfaces = {}
    for interface in dhcpd:
        interfaces[interface.tag] = []
        for entry in interface:
            if entry.tag == 'staticmap':
                host_data = {}
                for static_entry in entry:
                    if static_entry.tag in host_keys:
                        host_data.update({static_entry.tag: static_entry.text})
                interfaces[interface.tag].append(host_data)
    
    return interfaces

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-c', '--config', help='config.xml location', required=True)
    args = parser.parse_args()
    
    pf_mappings = get_pf_mappings(args.config)
    
    for interface, mappings in pf_mappings.items():
        for mapping in mappings:
            if mapping['ipaddr']:
                print("dhcp-host=%s,%s,%s # %s" % (interface, mapping['mac'], mapping['ipaddr'], mapping['hostname']))
