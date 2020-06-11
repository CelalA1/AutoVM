import os
import re
import help
import random
from server import get_arg, get_server, response

# Address
address = get_arg('ip[ip]')

# Server address
server_address = get_arg('server[ip]')

# Base directory
base = os.path.dirname(os.path.realpath(__file__))

serve = get_server()

try:
  machine = serve.lookupByName(address)
except:
  response(False)
  
try:
  xml = machine.XMLDesc()
except:
  response(False)

# Find port
port = re.findall("port='([0-9]+)'", xml)

if port:
  port = port[0]  

# Find password
password = re.findall("passwd='(.*?)'", xml)

if password:
  password = password[0]
  
if not port and not password:
  
  # New port
  port = random.randint(9000, 9999)
  
  # New password
  password = get_arg('password')
  
  try:
    online = machine.isActive()
  except:
    response(False)
  
  if online:
    try:
      machine.destroy()
    except:
      response(False)
  
  xml = re.sub('<devices>', "<devices><graphics type='vnc' port='{}' autoport='no' listen='0.0.0.0' passwd='{}'></graphics>".format(port, password), xml)

  try:
    serve.defineXML(xml)
  except:
    response(False)

  try:
    machine.create()
  except:
    response(False)
  
# VNC address
vnc_address = help.append(server_address, ':', port)

try:
  os.system(help.space('bash', help.path(base, '..', '..', '..', 'web/console/utils/launch.sh'), '--vnc', vnc_address, '--listen', get_arg('port'), '> /dev/null 2>&1 &'))
except:
  response(False)
  
response(True, {'password': password})