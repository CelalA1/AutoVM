import os
import sys
import help
import json
import libvirt
import urlparse

# Arguments
args = sys.argv[1]
args = urlparse.parse_qsl(args, keep_blank_values=True)
args = dict(args)

def get_arg(name):
  
  return args.get(name)

def get_server():
  
  auth = [
    [libvirt.VIR_CRED_AUTHNAME, libvirt.VIR_CRED_NOECHOPROMPT], get_arg('server[username]'), None
  ]
  
  address = help.append('qemu', '+', 'ssh://', get_arg('server[username]'), '@', get_arg('server[ip]'), '/system?no_verify=1')
  
  try:
    server = libvirt.openAuth(address, auth)
  except:
    return None
  
  return server

def online(address):
  
  response = os.system(help.space('ping', '-c 1', address, '> /dev/null'))
  
  if response == 0:
    return True
  
  return False

def write(name, content):
  
  machine = get_arg('vps[id]')
  
  if not machine:
    return False
  
  first = help.path(os.path.dirname(__file__), 'runtime', machine)
  
  if not os.path.exists(first):
    os.mkdir(first)
    
  second = help.path(first, name)
  
  with open(second, 'a') as file:
    file.write(str(content))
    file.write('\n')
    
  return True

def delete(name):
  
  machine = get_arg('vps[id]')
  
  if not machine:
    return False
  
  first = help.path(os.path.dirname(__file__), 'runtime', machine, 'log')
  
  if os.path.exists(first):
    os.remove(first)
    
  return True

def response(ok, data = None, log = None):
  
  if data:
    print json.dumps({'ok': ok, 'data': data})
  else:
    print json.dumps({'ok': ok})
    
  if log:
    write('log', log)
    
  sys.exit(0)