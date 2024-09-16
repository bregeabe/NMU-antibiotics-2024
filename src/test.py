#! /usr/bin/env python3
 
import tkinter as tk
from tkinter import messagebox
from functools import partial
import sys
 
class MainWindow:
    def __init__(self, parent):
        self.parent = parent
 
        btn = tk.Button(self.parent, text='Open New Window', fg='blue', \
                        command=partial(self.open_window), anchor='w')
        btn.grid(column=0, row=0, padx=10, pady=10)
        btn2 = tk.Button(self.parent, text='Close', fg='red', command=partial(self.close), anchor='w')
        btn2.grid(column=1,row=0, padx=10, pady=10)
 
        self.parent.protocol('WM_DELETE_WINDOW', self.close)
 
    def open_window(self):
        TopWindow(self.parent)
        self.parent.withdraw()
 
    def close(self):
        msg = messagebox.askokcancel('Quit Program', 'Do you wish to quit?')
        print(msg)
        if msg == True:
            sys.exit()
 
 
class TopWindow:
    def __init__(self, parent):
        self.parent=parent
        self.window = tk.Toplevel(parent=None)
        self.window.title('Top Level Window')
        self.window.geometry('300x200+10+10')
        btn = tk.Button(self.window, text='Close Window', fg='red', \
                        command=partial(self.window_close))
        btn.pack(side='bottom', pady=20)
        self.window.protocol('WM_DELETE_WINDOW', self.callback)
 
    def window_close(self):
        self.parent.deiconify()
        self.window.destroy()
 
    def callback(self):
        self.parent.deiconify()
        self.window.destroy()
 
 
def main():
    root = tk.Tk()
    root.title('Main Window')
    root.geometry('400x300+10+10')
    MainWindow(root)
    root.mainloop()
main()