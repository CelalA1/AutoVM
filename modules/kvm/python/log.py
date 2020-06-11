import os
import help
from server import get_arg, response

machine = get_arg('vps[id]')
  
first = help.path(os.path.dirname(os.path.realpath(__file__)), 'runtime', machine, 'log')

if not os.path.exists(first):
  response(False)
  
lines = []

with open(first) as file:
  lines = file.readlines()
  
last = lines.pop().strip()

if not last:
  response(False)

response(True, {'log': last})