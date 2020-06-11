import help
from server import get_server, response

serve = get_server()

try:
  machines = serve.listAllDomains()
except:
  response(False)
  
output = str()

for machine in machines:
  
  try:
    online = machine.isActive()
  except:
    online = False
    
  try:
    name = machine.name()
  except:
    online = False
    
  if online:
    output = help.append(output, '@', name)
    
response(True, output)