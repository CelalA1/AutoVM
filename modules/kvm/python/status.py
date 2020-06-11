from server import get_arg, get_server, online, response

name = get_arg('ip[ip]')

serve = get_server()

try:
  machine = serve.lookupByName(name)
except:
  response(False)
  
data = {'power': 'off', 'network': 'down'}

try:
  active = machine.isActive()
except:
  response(False)
  
if active:
  data.update({'power': 'on'})
  
if online(name):
  data.update({'network': 'up'})
  
response(True, data)