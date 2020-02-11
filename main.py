# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:59:52 2020

@author: Chen Renhong 
e-mail: nwpucrh@163.com
"""

import dir_ui2py
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox

def main():
    def selectdir():
        sdir = filedialog.askdirectory(title='选择ui文件目录')
        print(sdir)
        v.set(sdir)

    def closeThisWindow():
        root.destroy()

    def ui2py():
        dir_ui2py.runmain(v.get())
        tkinter.messagebox.showinfo('提示','转换完成！')
    
    #初始化
    root=tk.Tk()

    #设置窗体标题
    root.title('QT UI transform to .py ')

    label1=tk.Label(root,text='请选择文件夹:')
    v=tk.StringVar()
    text1=tk.Entry(root,bg='white',width=40,textvariable=v)
    button1=tk.Button(root,text='浏览',width=8,command=selectdir)
    button2=tk.Button(root,text='处理',width=8,command=ui2py)
    button3=tk.Button(root,text='退出',width=8,command=closeThisWindow)

    t=6
    label1.grid(row=0, column=0, padx=t, pady=t)
    text1.grid(row=0, column=1, columnspan=2, padx=t, pady=t)
    button1.grid(row=0, column=3, padx=t, pady=t)
    button2.grid(row=1, column=0, columnspan=2, padx=t, pady=t)
    button3.grid(row=1, column=2, columnspan=2, padx=t, pady=t)
 
    root.mainloop() 

if __name__=="__main__":
    main()

