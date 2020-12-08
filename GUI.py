# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 10:04:46 2020

@author: supernova
"""
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import pandas as pd 

class GUI(tk.Tk):
    def __init__(self):
        #parameters
        tk.Tk.__init__(self)
        self.geometry('1000x600')
        self.title('Visualization of your prediction')
        self.configure(background='cyan')
        self.resizable(width = False, height = False)
        self.path = None
        
        #frames
        self.f1 = tk.Frame(self, bd=10, width = 1000, height = 100, bg = "DeepSkyblue4",
                 relief = SUNKEN)
        self.f1.pack(side = TOP)
        self.f2 = tk.Frame(self, bd=5, width = 500, height = 500, bg = "cyan",
                 relief = RIDGE)
        self.f2.pack(side = RIGHT)
        self.f3 = tk.Frame(self, bd=5, width = 500, height = 500, bg = "cyan",
                 relief = RIDGE)
        self.f3.pack(side = LEFT)
        
        Label(self.f1, font=('arial', 30, 'bold'), bg = "DeepSkyblue4",
              text='Visualization of your prediction', bd = 7).pack()            
        self.my_algo = ['LinearRegression', 'LogisticRegression', 'DecisionTree',
                  'SVM', 'NaiveBayes', 'kNN', 'K-Means', 'RandomForest']
        self.listbox_algo = Listbox(self.f3)
        self.listbox_algo.grid(row=1 , column=0)
        
        for i, elm in enumerate(self.my_algo):
            self.listbox_algo.insert(i, str(elm))
            pass
        
        self.listbox_features = Listbox(self.f3)
        self.listbox_features.grid(row=1 , column=1)
        
        bt1 = tk.Button(self.f3,bg="cyan", text="select the algorithem",
                        command=lambda :self.Algorithme())
        bt1.grid(row=0 , column=0)
        
        bt2 = tk.Button(self.f3,bg="cyan", text="upload data",
                        command=lambda :self.upload())
        bt2.grid(row=0 , column=1)
        
        bt3 = tk.Button(self.f3,bg="cyan", text="choose your features",
                        command=lambda :self.features())
        bt3.grid(row=0 , column=3)
        
        bt3 = tk.Button(self.f3,bg="cyan", text="choose your features",
                        command=lambda :self.features())
        bt3.grid(row=0 , column=3) 
        
        
        
        
        
    # functions 
    def upload(self):
        self.path = filedialog.askopenfilename(initialdir = "/",
                                                   title = "Select file",
                filetypes = (("jpeg files","*.csv"),("all files","*.*")))
 
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
  
    def Algorithem(self):
        try:
            t = self.listbox_algo.curselection()
            algo = self.my_algo[t[0]]
            print(algo)
        except:
            print('selection an algorithm')
            
    def selection_features(self):
        try:
            t = self.listbox_algo.curselection()
            algo = self.my_algo[t[0]]
            print(algo)
        except:
            print('selection a feature')
        
        
        
        
        
        
        

if __name__ == '__main__':
    gui = GUI().mainloop()