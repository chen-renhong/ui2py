# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 15:03:08 2020

@author: Chen Renhong 
e-mail: nwpucrh@163.com

"""

## requirement: python.exe add to environment path###

import os
import os.path
dir=r"C:\Users\HC\Desktop\dir"

def list_ui_file(tep_dir):
    list=[]
    files=os.listdir(tep_dir)
    for filename in files:
        if os.path.splitext(filename)[1] == ".ui":
            list.append(filename)
    return list

def transpyfile(filename):
    return os.path.splitext(filename)[0] + ".py"

def runmain(tep_dir):
    list=list_ui_file(tep_dir)
    os.chdir(tep_dir)
    for uifile in list:
        pyfile = transpyfile(uifile)    
        cmd = "pyuic5 -o {pyfile} {uifile}".\
        format(pyfile=pyfile, uifile=uifile)
        os.system(cmd)
        
if __name__ =="__main__":   
    runmain(dir)