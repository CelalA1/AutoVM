import re
import sys
import time
import help
import shutil
import libvirt
from server import get_arg, get_server, write, delete

# Log
delete('log')

# Status
write('status', '1:5')

# VM name
name = get_arg('ip[ip]')

# Template
template = get_arg('os[kvm_type]')

# Pool data
pool_name = get_arg('datastore[pool_name]')
pool_path = get_arg('datastore[pool_path]')

# Connect to KVM
serve = get_server()

# Default pool
try:
  default_pool = serve.storagePoolLookupByName(pool_name)
except:
  raise Exception
  
# Template pool
try:
  template_pool = serve.storagePoolLookupByName('template')
except:
  raise Exception
  
write('status', '1:15')
  
# Find machine
machine = None

try:
  machine = serve.lookupByName(name)
except:
  pass # Do not anything

# Destroy machine
if machine:
  
  try:
    xml = machine.XMLDesc()
  except:
    raise Exception
  
  if machine.isActive():
    try:
      machine.destroy()
    except:
      raise Exception
      
    time.sleep(5)
    
  try:
    machine.undefine()
  except:
    raise Exception

  try:
    pools = serve.listStoragePools()
  except:
    raise Exception
    
  for pool in pools:
    try:
      pool = serve.storagePoolLookupByName(pool)
    except:
      raise Exception
      
    try:
      volumes = pool.listAllVolumes()
    except:
      raise Exception
      
    for volume in volumes:
      if name in volume.name():
        try:
          volume.delete()
        except:
          raise Exception
    
  time.sleep(5)
  
# Find template
try:
  template = template_pool.storageVolLookupByName(template)
except:
  raise Exception
  
# Prepare volume
with open('volume') as file:
  volume = file.read()
  
# HARD
hard = get_arg('plan[hard]')

if get_arg('vps[vps_hard]'):
  hard = get_arg('vps[vps_hard]')
  
items = {'@name': name, '@hard': hard, '@pool': pool_path}

for item in items:
  volume = help.replace(volume, item, items[item])
  
# Prepare config
with open('config') as file:
  config = file.read()

# MEMORY
memory = get_arg('plan[ram]')

if get_arg('vps[vps_ram]'):
  memory = get_arg('vps[vps_ram]')
  
# CPU
cpu_cores = get_arg('plan[cpu_core]')

if get_arg('vps[vps_cpu_core]'):
  cpu_cores = get_arg('vps[vps_cpu_core]')
  
# MHZ
cpu_mhz = get_arg('plan[cpu_mhz]')

if get_arg('vps[vps_cpu_mhz]'):
  cpu_mhz = get_arg('vps[vps_cpu_mhz]')
  
items = {'@name': name, '@memory': memory, '@cpu': cpu_cores, '@mhz': cpu_mhz, '@pool': pool_path}

for item in items:
  config = help.replace(config, item, items[item])
  
# Create volume
try:
  storage = default_pool.createXMLFrom(volume, template)
except:
  raise Exception
  
# Status
write('status', '2:25')
  
# Define XML
try: 
  machine = serve.defineXML(config)
except:
  raise Exception
  
# Status
write('status', '2:35')
  
# Create VM
try:
  machine.create()
except:
  raise Exception
  
time.sleep(20)

# Status
write('status', '2:45')

# Apply hard
bytes = int(hard) * 1024 * 1024 * 1024

try:
  machine.blockResize('hda', bytes, libvirt.VIR_DOMAIN_BLOCK_RESIZE_BYTES)
except:
  raise Exception
  
# Status
write('status', '2:55')