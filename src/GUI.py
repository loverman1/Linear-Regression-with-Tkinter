# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 10:04:46 2020

@author: frsiabel
"""
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import pandas as pd 

class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('1000x600')
        self.title('Visualization of your prediction')
        self.configure(background='cyan')
        self.resizable(width = False, height = False)
        self.path = None
        
        self.f1 = tk.Frame(self, width = 1000, height = 100, bg = "DeepSkyblue4",
                 relief = SUNKEN)
        self.f1.pack(side = TOP)
        
        self.f2 = tk.Frame(self, width = 1000, height = 500, bg = "cyan",
                 relief = SUNKEN)
        self.f2.pack(side = TOP)
        
        lb1 = tk.Label(self.f2, font=('arial',10,'bold'), text="upload the file:"
                      ,bg="cyan",fg="black")
        lb1.grid(padx=50,pady=20, row= 0,column=0)
         
        bt1 = tk.Button(self.f2,padx=50,pady=10,bg="cyan", text=" clicked ",
                        command=lambda :self.upload())
        bt1.grid(padx=50,pady=20,row=0 , column=1)
         
        bt2 = tk.Button(self.f2,padx=50,pady=10,bg="cyan", text=" clicked ",
                        command=lambda :self.features())
        bt2.grid(padx=50,pady=20,row=1 , column=0)  
        
        self.listbox_features = Listbox(self.f2)
        self.listbox_features.grid(padx = 50, pady = 20, row=1 , column=1)
        
        bt3 = tk.Button(self.f2,padx=50,pady=10,bg="cyan", text="choose algrithm ",
                        command=lambda :self.Algorithme())
        bt3.grid(padx=50,pady=20,row=2 , column=0)  
        
        self.listbox_algo = Listbox(self.f2)
        self.listbox_algo.grid(padx = 50, pady = 20, row=2 , column=1)
    
    def upload(self):
        self.path = filedialog.askopenfilename(initialdir = "/",
                                                   title = "Select file",
                      filetypes = (("jpeg files","*.csv"),("all files","*.*")))
        print(self.path)
    
    def features(self):
        columns = None
        try:
            data = pd.read_csv(str(self.path))
            columns = list(data.columns)
        except:
            print('the path is empty')
            
        for i, elm in enumerate(columns):
            self.listbox_features.insert(i, elm)
            pass
 
        
    def Algorithme(self):
        l = "LinearRegression LogisticRegression DecisionTree SVM NaiveBayes kNN K-Means RandomForest"
        for i, elm in enumerate(l.split(' ')):
            self.listbox_algo.insert(i, str(elm))
        pass

if __name__ == '__main__':
    gui = GUI().mainloop()