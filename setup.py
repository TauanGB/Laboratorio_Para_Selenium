##python setup.py build

import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages":
    	["customtkinter",
        "tkinter",
        "os",
        "json",
        "sys",
        "time"],
        "include_files":[("icons", "icons")]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"
    
    

setup(
    name="Lab Selenium",
    version="1.0",
    description="Ferramenta para analise de sites utilizando selenium",
    options={"build_exe": build_exe_options},
    executables=[Executable("Lab Selenium.py", base=base,icon="icon.ico")],    
)