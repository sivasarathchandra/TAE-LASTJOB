import sys
from cx_Freeze import setup, Executable

setup(
    name = "Excel compare",
    version = "0.1",
    description = "To compare 2 excels.",
    executables = [Executable("Final_Excel_main.py", base = "Win32GUI")])