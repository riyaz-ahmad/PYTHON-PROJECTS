import cx_Freeze
import sys
import os
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Riyaz Ahmad\AppData\Local\Programs\Python\Python37-32\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Riyaz Ahmad\AppData\Local\Programs\Python\Python37-32\tcl\tk8.6"

executables = [cx_Freeze.Executable("RNR.py", base=base, icon="icon1.ico")]


cx_Freeze.setup(
    name = "RNR text editor",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["icon1.ico", 'tcl86t.dll','tk86t.dll', 'icons2']}},
    version = "0.01",
    description = "Tkinter Application",
    executables = executables
    )