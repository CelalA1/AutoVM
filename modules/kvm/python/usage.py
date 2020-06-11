from server import get_arg, get_server, response

serve = get_server()

name = get_arg('ip[ip]')

try:
  machine = serve.lookupByName(name)
except:
  response(False)
  
try:
  stats = machine.memoryStats()
except:
  response(False)

# RAM stats
ram = stats['actual']
used_ram = ram - stats['available']
  
data = {'ram': ram, 'usedRam': used_ram}

response(True, data)