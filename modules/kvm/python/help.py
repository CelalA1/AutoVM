import os

def append(*args):
  
  result = ''
  
  for arg in args:
    result = result + str(arg)
    
  return result

def path(*args):
  
  result = ''
  
  for arg in args:
    result = os.path.join(result, str(arg))
    
  return result

def space(*args):
  
  result, space = ['', ' ']
  
  for arg in args:
    result = result + str(arg) + space
    
  return result

def replace(text, first, second):
  
  return text.replace(first, str(second))