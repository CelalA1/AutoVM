from xml.etree import ElementTree
from server import get_server, response

serve = get_server()

try:
  machines = serve.listAllDomains()
except:
  response(False)
  
servers = {}
  
for machine in machines:
  
  address = machine.name()
  
  try:
    xml = machine.XMLDesc()
  except:
    continue
    
  try:
    tree = ElementTree.fromstring(xml)
  except:
    continue
    
  try:
    face = tree.find('devices/interface/target').get('dev')
  except:
    continue
    
  try:
    stats = machine.interfaceStats(face)
  except:
    continue
    
  servers[address] = int(stats[0]) + int(stats[1])
  
response(True, servers)