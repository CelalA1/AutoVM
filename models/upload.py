import os
import ssl
import spur
import argparse

ssl._create_default_https_context = ssl._create_unverified_context

# Parse arguments
parser = argparse.ArgumentParser()

args = ['--address', '--username', '--password', '--content']

for arg in args:
  parser.add_argument(arg)
  
args = parser.parse_args()

# Generate path
def path(*args):
  
  result = ''
  
  for arg in args:
    result = os.path.join(result, str(arg))
    
  return result

# Append with space
def space(*args):
  
  result, space = ['', ' ']
  
  for arg in args:
    result = result + str(arg) + space
    
  return result

# Connect to SSH
try:
  ssh = spur.SshShell(hostname=args.address, username=args.username, password=args.password, missing_host_key=spur.ssh.MissingHostKey.accept)
except:
  raise Exception
  
# Remote file
rfile = path('/root', '.ssh', 'authorized_keys')

# Upload
try:
  ssh.run(['sh', '-c', space('echo', args.content, '>', rfile)])
except:
  raise Exception