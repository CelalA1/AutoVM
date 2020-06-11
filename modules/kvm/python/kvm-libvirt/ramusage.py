from __future__ import print_function
import sys
import libvirt
from xml.dom import minidom

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)


dom = 'testvm'
if dom == None:
    print('Failed to find the domain '+domName, file=sys.stderr)
    exit(1)



stats  = dom.memoryStats()
print('memory used:')
for name in stats:
    print('  '+str(stats[name])+' ('+name+')')

dom.getCPUStats(False)
