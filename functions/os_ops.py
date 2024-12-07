import os
import subprocess as sp
paths={
    'notepad':"C://Windows//System32//notepad.exe",
    'calc':"C://Windows//System32//calc.exe"
}

def open_camera():
    sp.run('start microsoft.windows.camera:',shell=True)

def open_notepad():
    sp.Popen(paths['notepad'])

def open_calculator():
    sp.Popen(paths['calc'])

def open_cmd():
    os.system('start cmd')