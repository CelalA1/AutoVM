from server import get_arg, get_server, response

serve = get_server()

name = get_arg('ip[ip]')

try:
  machine = serve.lookupByName(name)
except:
  response(False)
  
try:
  machine.reboot()
except:
  response(False)
  
response(True)