import re
import libvirt

# Connect
auth = [[libvirt.VIR_CRED_AUTHNAME, libvirt.VIR_CRED_NOECHOPROMPT], 'root', None]
conn = libvirt.openAuth('qemu+ssh://root@kvm.autovm.net/system?no_verify=1', auth)
    
# Find
domain = conn.lookupByName('testvm')

domain.destroy()

# Fetch XML
xml = domain.XMLDesc()

# Add graphic
xml = re.sub('<devices>', "<devices><graphics type='vnc' port='-1' autoport='yes' listen='127.0.0.1' passwd='112444aa'></graphics>", xml)

# Define XML
conn.defineXML(xml)

domain.create()
