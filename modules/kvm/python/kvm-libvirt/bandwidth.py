import libvirt
import sys
from xml.etree import ElementTree

auth = [[libvirt.VIR_CRED_AUTHNAME, libvirt.VIR_CRED_NOECHOPROMPT], 'root', None]

conn = libvirt.openAuth('qemu+ssh://root@kvm.autovm.net/system?no_verify=1', auth, 0)
 
Hamster = conn.lookupByName('testvm')

tree = ElementTree.fromstring(Hamster.XMLDesc())
iface = tree.find('devices/interface/target').get('dev')
stats = Hamster.interfaceStats(iface)
print('read:    '+str(stats[0]))
print('write:   '+str(stats[4]))

