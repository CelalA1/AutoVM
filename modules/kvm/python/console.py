import os
import help
import random
from xml.etree import ElementTree
from server import get_arg, get_server, response

# Base directory
base = os.path.dirname(os.path.realpath(__file__))

# Connect
serve = get_server()

# Arguments
server_address = get_arg('server[ip]')
name = get_arg('ip[ip]')
password = get_arg('password')
listen = get_arg('port')

# Find machine
try:
  machine = serve.lookupByName(name)
except:
  response(False)
  
# Status
online = False

try:
  online = machine.isActive()
except:
  response(False)
  
# Stop
if online:
  try:
    machine.destroy()
  except:
    response(False)
    
# Fetch XML
try:
  xml = machine.XMLDesc()
except:
  response(False)
  
# Parse XML
try:
  tree = ElementTree.fromstring(xml)
except:
  response(False)
  
# Find devices
devices = tree.find('devices')

# Find element
element = devices.find('graphics')

if element is None:
  element = ElementTree.Element('graphics')
  
# Generate port
port = random.randint(9000, 9999)
port = str(port)
  
# Attributes
details = {'type': 'vnc', 'port': port, 'passwd': password, 'autoport': 'no', 'listen': '0.0.0.0'}

# Add attributes
for detail in details:
  element.set(detail, details[detail])
  
# Add element
exists = devices.find('graphics')

if exists is None:
  devices.append(element)

# XML output
xml = ElementTree.tostring(tree)

# Configure machine
try:
  serve.defineXML(xml)
except:
  response(False)
  
# Start
try:
  machine.create()
except:
  response(False)
  
# Run VNC
vnc_address = help.append(server_address, ':', port)

try:
  os.system(help.space('bash', help.path(base, '..', '..', '..', 'web/console/utils/launch.sh'), '--vnc', vnc_address, '--listen', listen, '> /dev/null 2>&1 &'))
except:
  response(False)
  
response(True, {'password': password})