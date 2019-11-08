import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression as lr
from sklearn.model_selection import train_test_split
from tkinter import *
import tkinter as tk
import matplotlib
matplotlib.use("TKAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure 
from tkinter import filedialog

class interface(tk.Tk):
    def __init__(self):
        """=================================================================================================================================================="""
        tk.Tk.__init__(self)
        self.geometry("1500x800")
        self.title(" machine learning regression algorthme ")
        self.configure(background='seashell4')    
        self.resizable(width=False,height=False)
        self.model=None
        """=================================================================================================================================================="""
        self.f1=tk.Frame(self,width=1600,height=600,bg='dim gray',relief=SUNKEN)
        self.f1.pack(side=TOP)
        self.f2=tk.Frame(self,width=500,height=700,bg="dim gray",relief=SUNKEN)
        self.f2.pack(side=LEFT)
        self.f3=tk.Frame(self,width=800,height=700,bg="dim gray",relief=SUNKEN)
        self.f3.pack(side=RIGHT)
        """=================================================================================================================================================="""
        self.l1=tk.Label(self.f1, font=('arial',50,'bold'),text=" Linear Regression ",fg="black",bd=10,anchor='w')
        self.l1.grid(row=0,column=0)
        """=================================================================================================================================================="""
        label=tk.Label(self.f2,font=('arial',20,'bold'), text=" upload the file :" ,bg="seashell4",fg="black")
        label.grid(padx=50,pady=20,row=0,column=0)
        button=tk.Button(self.f2,padx=50,pady=10,bg="seashell4",text=" clicked ",command=lambda :self.upload())
        button.grid(padx=50,pady=20,row=0 , column=1)
        """=================================================================================================================================================="""
        label=tk.Label(self.f2,font=('arial',20,'bold'), text=" get shape of data " ,bg="seashell4",fg="black")
        label.grid(padx=50,pady=20,row=1,column=0)
        button=tk.Button(self.f2,padx=50,pady=10,bg="seashell4",text=" clicked ",command = lambda : self.shapedata())
        button.grid(padx=50,pady=20,row=1 , column=1)
        """=================================================================================================================================================="""
        self.label1=tk.Label(self.f2,font=('arial',20,'bold'),bg="seashell4",fg="black")
        self.label1.grid(padx=50,pady=20,row=2,columnspan=4)
        """=================================================================================================================================================="""
        labe2=tk.Label(self.f2,font=('arial',20,'bold'), text=" get both coef et inercept" ,bg="seashell4",fg="black")
        labe2.grid(padx=50,pady=20,row=3,column=0)
        button=tk.Button(self.f2,padx=50,pady=10,bg="seashell4",text=" clicked ",command = lambda :self.showInterAndInter())
        button.grid(padx=50,pady=20,row=3 , column=1)
        """=================================================================================================================================================="""
        self.label2=tk.Label(self.f2,font=('arial',20,'bold'),bg="seashell4",fg="black")
        self.label2.grid(padx=50,pady=20,row=4,columnspan=4)
        """=================================================================================================================================================="""
        labe3=tk.Label(self.f2,font=('arial',20,'bold'), text=" plot data " ,bg="seashell4",fg="black")
        labe3.grid(padx=50,pady=20,row=5,column=0)
        button=tk.Button(self.f2,padx=50,pady=10,bg="seashell4",text=" clicked ",command = lambda : self.matplotCanavs(self.f3))
        button.grid(padx=50,pady=20,row=5 , column=1)
        """=================================================================================================================================================="""
        labe4=tk.Label(self.f2,font=('arial',20,'bold'), text=" show prediction " ,bg="seashell4",fg="black")
        labe4.grid(padx=50,pady=20,row=6,column=0)
        button=tk.Button(self.f2,padx=50,pady=10,bg="seashell4",text=" clicked ",command = lambda : self.matplotCanavsPrediction(self.f3))
        button.grid(padx=50,pady=20,row=6 , column=1)
        """=================================================================================================================================================="""
        
        
        
       
    def upload(self):
        self.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        df=pd.read_csv(str(self.filename))
        x=np.array(df[[str(df.columns[4])]])
        y=np.array(df[[str(df.columns[12])]])
        self.model=Regression(x,y)
        
    def matplotCanavs(self,x):
        f = Figure(figsize=(5,5) , dpi = 100)
        a = f.add_subplot(111)
        a.scatter(self.model.data,self.model.traget,color='blue')
        a.plot(self.model.xtrain,self.model.coef[0][0]*self.model.xtrain + self.model.inter[0],'r')
        canvas =FigureCanvasTkAgg(f,x)
        canvas.get_tk_widget().pack(fill=BOTH,expand=True)
    
    def shapedata(self):
        self.model.ConstructionData()
        self.label1.configure(text=str(self.model.xtrain.shape)+str(self.model.ytrain.shape)+"\n"+str(self.model.xtest.shape)+str(self.model.ytest.shape))
        self.model.regression()
        
    def showInterAndInter(self):
        self.model.coief_intercept()
        self.label2.configure(text=str(self.model.coef)+str(self.model.inter))

    def matplotCanavsPrediction(self,x):
        f = Figure(figsize=(5,5) , dpi = 100)
        a = f.add_subplot(111)
        d=self.model.prediction1()
        a.scatter(self.model.xtest,d,color='blue')
        canvas =FigureCanvasTkAgg(f,x)
        canvas.get_tk_widget().pack(fill=BOTH,expand=True)    
    
        
class Regression():
    def __init__(self,data,traget):
        self.data=data
        self.traget=traget
    
        self.modele=None
        
        self.xtest=None
        self.ytest=None
        self.xtrain=None     
        self.ytrain=None
        
        self.coef=None
        self.inter=None
        
    def ConstructionData(self):
        self.xtrain, self.xtest, self.ytrain, self.ytest = train_test_split(self.data,self.traget)
        print ('Train set:', self.xtrain.shape,  self.ytrain.shape)
        print ('Test set:', self.xtest.shape,  self.ytest.shape)
        
    def regression(self):
        self.modele=lr()
        self.modele.fit(self.xtrain,self.ytrain)
    
    def coief_intercept(self):
        self.coef=self.modele.coef_
        self.inter=self.modele.intercept_
        
    def plot(self):
        plt.plot(self.xtrain,self.coef[0][0]*self.xtrain + self.inter[0] ,'-r')
        plt.scatter(self.data,self.traget,color='blue')
        plt.show()
        
    def prediction1(self):
        d=self.modele.predict(self.xtest)
        return d
    
    def showXtest(self):
        print(self.xtest)
        
    def showYtest(self):
        print(self.ytest)
    
    
    def prediction2(self,point):
        y=point*self.coef[0][0]+self.inter[0]
        return y
    
    def error(self):
        error=np.mean(np.absolute(self.ytest-self.modele.predict(self.xtest)))
        return error

if __name__ == "__main__":
    interface().mainloop()