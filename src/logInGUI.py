# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 10:25:31 2020

@author: frsiabel
"""
from tkinter import *
import tkinter as tk
from GUI import GUI

class LogIn_GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.geometry('1000x600')
        self.title('Visualization of your prediction')
        self.configure(background='cyan')
        self.resizable(width=False,height=False)
    
        
        Label(self,font=('arial',20,'bold'), text="Username" ,
                         bg="cyan",fg="black").pack(pady = 5) 
        self.username = Entry(self)
        self.username.pack(pady = 5)
        
        Label(self,font=('arial',20,'bold'), text="Password" ,
                        bg="cyan",fg="black").pack(pady = 5) 
        self.password = Entry(self, show='*')
        self.password.pack(pady = 5)

        tk.Button(self, padx = 5 ,pady = 5 ,bg="cyan",
                              text = "connect ", 
                              command = lambda : self.long_in()).pack(pady = 5)
    def long_in(self):
        if self.username.get() == 'admin' and self.password.get() == 'admin':
            print('you have the access to the platforme')
            self.destroy()
            GUI().mainloop()
        else:
            messagebox.showerror("Error", "the username/password is incorrect")

if __name__ == '__main__':
    gui = LogIn_GUI().mainloop()