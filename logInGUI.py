# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 10:25:31 2020

@author: supernova
"""
from tkinter import *
import tkinter as tk
from GUI import GUI

class LogIn_GUI(tk.Tk):
    def __init__(self):
        #parameters
        tk.Tk.__init__(self)
        self.geometry('1000x600')
        self.title('Visualization of your prediction')
        self.configure(background='cyan')
        self.resizable(width = False, height = False)
        
        #frames
        self.f1 = tk.Frame(self, bd=10, width = 1000, height = 100, bg = "DeepSkyblue4",
                 relief = SUNKEN)
        self.f1.pack(side = TOP)
        
        self.f2 = tk.Frame(self, bd=5, width = 500, height = 500, bg = "cyan",
                 relief = RIDGE)
        self.f2.pack(side = TOP)
        
        self.f3 = tk.Frame(self.f2, bd=5, width = 500, height = 500, bg = "cyan",
                 relief = RIDGE)
        self.f3.pack(side = TOP)
        
        Label(self.f1, font=('arial', 30, 'bold'), bg = "DeepSkyblue4",
              text='Visualization of your prediction', bd = 7).pack()
        
        #buttons and Entries
        Label(self.f3,font=('arial',20,'bold'), text="Username" ,
                         bg="cyan",fg="black").pack(pady = 5) 
        
        self.username = Entry(self.f3)
        self.username.pack(pady = 5)
        
        Label(self.f3,font=('arial',20,'bold'), text="Password" ,
                        bg="cyan",fg="black").pack(pady = 5) 
        
        self.password = Entry(self.f3, show = '*')
        self.password.pack(pady = 5)

        tk.Button(self.f3, padx = 5 ,pady = 5 ,bg="cyan",
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