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
_abbrevs = ['sp',
            'np',
            ''] # Abbrev of imported modules, '' for no abbrevs
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
for _, __ in zip(_imports, _abbrevs):
  if __ != '':
    exec("{} = {}".format(_, __))


os.system('cls||clear') # clear entire terminal screen


## Do something below
a = np.float64(2.4)
