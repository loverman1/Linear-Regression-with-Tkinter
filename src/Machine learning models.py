# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 09:54:41 2020

@author: frsiabel
"""
import pandas as pd 
from sklearn.linear_model import LinearRegression

def Linear_regression(X, Y):
    model = LinearRegression()
    model.fit(X,Y)
    return model

def predict(model, test):
    return model.predict(test)
