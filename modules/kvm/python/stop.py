from server import get_arg, get_server, response

serve = get_server()

name = get_arg('ip[ip]')

try:
  machine = serve.lookupByName(name)
except:
  response(False)
  
try:
  online = machine.isActive()
except:
  response(False)
  
if online:
  try:
    machine.destroy()
  except:
    response(False)
    
response(True)