from cx_Freeze import setup, Executable
import sys
import os

os.environ['APPDATA']

includes = []

# Include your files and folders
includefiles = ['src/','images/','__main__.py','bossSpy.log']

# Exclude unnecessary packages
excludes = ['cx_Freeze','pydoc_data','setuptools','distutils','tkinter']

# Dependencies are automatically detected, but some modules need help.
packages = ['src']    

base = None
shortcutName = None
shortcutDir = None
if sys.platform == "win32":
    base = 'Win32GUI'
    shortcutName= 'BossSpy'
    shortcutDir= 'DesktopFolder'

setup(
    name = 'BossSpy',
    version = '0.1',
    description = 'My boss spy is a module to spy on employees',
    author = 'Athene Mutyambizi',
    author_email = '',
    options = {
        'build_exe': {
        'includes': includes,
        'excludes': excludes,
        'packages': packages,
        'include_files': includefiles},
        'bdist_msi': {
            'initial_target_dir': 'C:\\Users\Athene\Documents\BossSpy'}
        }, 
    executables = [Executable('__main__.py', 
    shortcut_name=shortcutName,
    shortcut_dir=shortcutDir,
    base = base, # "Console", base, # None
    icon='images/bossspy.ico')]
)
