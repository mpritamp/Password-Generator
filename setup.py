import cx_Freeze
import sys
import os

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Python\Python 3.7\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Python\Python 3.7\tcl\tk8.6"

# Make Executable File Using .pyw extension
executables = [cx_Freeze.Executable("app.pyw", base=base, icon="Image\shield.ico")]

cx_Freeze.setup(
    name="Usecret",
    options={"build_exe": {"packages": ["tkinter", "os"],
                           "include_files": ['tcl86t.dll',
                                             'tk86t.dll',
                                             'Image']}},
    version="0.01",
    description="Password Generator",
    executables=executables
)

# Run this command : python setup.py bdist_msi
