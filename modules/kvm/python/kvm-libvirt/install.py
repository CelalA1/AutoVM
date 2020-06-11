import libvirt
import sys
auth = [[libvirt.VIR_CRED_AUTHNAME, libvirt.VIR_CRED_NOECHOPROMPT], 'root', None]


## new vm storage
new_stgvol_xml = """
<volume>
  <name>testvm.img</name>
  <allocation>0</allocation>
  <capacity unit="G">2</capacity>
  <target>
    <path>/var/lib/virt/images/testvm.img</path>
    <permissions>
      <owner>107</owner>
      <group>107</group>
      <mode>0744</mode>
      <label>virt_image_t</label>
    </permissions>
  </target>
</volume>"""

## new vm xml file
xmlconfig = """
<domain type="kvm">
    <name>testvm</name>
    <vcpu placement='static'>1</vcpu>
    <memory unit="MiB">256</memory>
    <currentMemory unit="MiB">256</currentMemory>
    <vcpu placement="static">2</vcpu>
    <os>
      <type arch='x86_64' machine='pc-i440fx-xenial'>hvm</type>
      <boot dev='hd'/>
    </os>
    <features>
        <acpi />
        <apic />
    </features>
    <clock offset="utc" />
    <on_poweroff>destroy</on_poweroff>
    <on_reboot>restart</on_reboot>
    <on_crash>restart</on_crash>
    <devices>
        <emulator>/usr/bin/kvm-spice</emulator>
        <disk device="disk" type="file">
            <driver cache="none" name="qemu" type="raw" />
            <source file="/var/lib/libvirt/images/testvm.img" />
            <target dev="hda" />
            <address bus="0" controller="0" target="0" type="drive" unit="0" />
        </disk>
        <interface type="network">
            <source network="default" />
        </interface>
        <graphics port="-1" type="vnc" />
    </devices>
</domain>"""



## connect to server

conn = libvirt.openAuth('qemu+ssh://root@kvm.autovm.net/system?no_verify=1', auth, 0)


pool_name = 'default'
pool = conn.storagePoolLookupByName(pool_name)



## find old vm and delete
try:
    existvm = conn.lookupByName("testvm")
    existvm.destroy()
    existvm.undefine()
    vol0 = 'testvm.img'
    stgvol2 = pool.storageVolLookupByName(vol0)
    stgvol2.wipe(0)
    stgvol2.delete(0)
except:
    print 'Failed to find old domain'




template = 'ubuntu16.04.qcow2'
templatestgvol = pool.storageVolLookupByName(template)


new_stgvol_xml = pool.createXMLFrom(new_stgvol_xml, templatestgvol, 0)

newvm = conn.defineXML(xmlconfig)

newvm.create()

newvm.blockResize('hda', 100000000000, libvirt.VIR_DOMAIN_BLOCK_RESIZE_BYTES)
