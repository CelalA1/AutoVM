from __future__ import print_function
import sys
import libvirt
from xml.dom import minidom

domName = 'generic'
conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)
    

dom = conn.lookupByName(domName)
if dom == None:
    print('Failed to find the domain '+domName, file=sys.stderr)
    exit(1)

dom.setVcpusFlags(2)
dom.setMaxMemory(409600)
dom.setMemoryFlags(409600)


# virsh dumpxml test | grep 'source file'
# qemu-img resize /var/lib/libvirt/images/rhel8.qcow2 +10G
