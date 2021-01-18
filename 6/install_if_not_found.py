import sys, os, platform

_plt = platform.system().lower()
_py_path = os.path.dirname(sys.executable)+'\\'
_py_path += 'python.exe' if _plt == 'windows' else 'python'

## Adjust Below ##
_imports = ['scipy',
            'numpy',
            'matplotlib'] # name of imported module
_module_ = ['scipy',
            'numpy',
            'matplotlib'] # install name of imported module
## Adjust Above ##

print("Importing modules...")
for _, __ in zip(_imports, _module_):
  try:
    exec("import {}".format(_))
  except ImportError:
    print("Installing missing module - {}".format(__))
    if _plt == 'windows':
      os.system(_py_path + ' -m pip install ' + __)
    else:
      os.system('./' + _py_path + ' -m pip install ' + __)
    try:
      exec("import {}".format(_))
    except Exception as e:
      print(e)
      print("There are some errors in {}. Please check that manually".format(_))
      os.exit()

print('\033c') # clear entire terminal screen
