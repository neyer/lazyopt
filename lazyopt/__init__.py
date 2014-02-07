import inspect
import os
import sys

class ConfigurationError(Exception):
  """Invalid option specified."""


def get_as_number(value):
  """Return str `value` as a number if possible. Return None otherwise."""
  if not value: return None
  if value.count('.') == 1:
    return float(value)
  else:
    return int(value)

def cast_value_str(value):
  "Interpret str `value` as whatever datatype makes sense"

  # first see if it's one of these constants
  hard_coded = { 'None' : None, 'True' : True, 'False' : False }
  try:
    return hard_coded[value]
  except KeyError:
    # if it's not a constant see if it's a number
    try:
      return get_as_number(value)
    except ValueError:
      # it must be a string
      return value
  

def get_argv_bindings(argv=sys.argv):
  """Parse `argv` and return dict of new bindings."""
  results = {}
  this_arg_name = None

  for arg in argv:
    #if we have the name of an argument,
    #we are waiting for a variable
    if this_arg_name:
      #if the next arg is another name, this_arg_name is a flag
      if arg.find('--') == 0:
        value = True
        name = this_arg_name
        this_arg_name = arg[2:]
      else:
        value = arg
        name = this_arg_name
        this_arg_name = None

      #make sure they haven't given the same arg twice
      if name in results:
        raise ConfigurationError("duplicate arg %s" % name)
      else:
        # store the binding
        results[name] = value
    else:
      #check to see if this option is an arg name
      if arg.find('--') == 0:
        this_arg_name = arg[2:]
        #check the next arg for the value
      else: pass
        # this is a position argument. just ignore it.

  # we looped through all the args and have one left
  # so that must be a boolean flag
  if this_arg_name:
    if this_arg_name in results:
      raise ConfigurationError("duplicate arg %s" % this_arg_name)
    else:
      results[this_arg_name] = True

  return results


def get_module_and_var_name(var_name):
  "Convert an option name to a module,variable pair."
  parts = var_name.split('.')

  module_name = ('.'.join(parts[:-1])).replace('-','_')
  var_name = parts[-1].replace('-','_')

  return module_name, var_name


def apply_binding(name, value):
  "Set module-qualified variable `name` to `value`"

  module_name, var_name = get_module_and_var_name(name)

  __import__(module_name, globals(), locals(), [], 0)
  module = sys.modules.get(module_name)

  if hasattr(module, var_name):
    setattr(module, var_name, value)
  else:
    msg = 'module %s has no value %s to confgure with value %s.'
    msg = msg % (module_name, var_name, value)
    raise ConfigurationError(msg)

