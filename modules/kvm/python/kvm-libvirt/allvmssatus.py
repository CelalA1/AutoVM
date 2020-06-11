import libvirt
import sys
from xml.etree import ElementTree

auth = [[libvirt.VIR_CRED_AUTHNAME, libvirt.VIR_CRED_NOECHOPROMPT], 'root', None]

conn = libvirt.openAuth('qemu+ssh://root@kvm.autovm.net/system?no_verify=1', auth, 0)


STATE = {1: 'RUNNING', 5: 'SHUTOFF'}

for vm in conn.listAllDomains():
    vm_name, vm_id = vm.name(), vm.ID()
    vm_state, vm_reason = vm.state()
    print('[{}:{}]---> state: {}, reason code {}'.format(vm_name, vm_id, STATE[vm_state], vm_reason))
