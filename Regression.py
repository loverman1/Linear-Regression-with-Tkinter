import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np

print("***********************************************************************")
# uploading the data 
df = pd.read_csv("FuelConsumptionCo2.csv")
# take a look at the dataset
print(df.head())

print("***********************************************************************")
print(df.describe())

print("***********************************************************************")
cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
print(cdf.head(9))

print("***********************************************************************")
viz = cdf[['CYLINDERS','ENGINESIZE','CO2EMISSIONS','FUELCONSUMPTION_COMB']]
viz.hist()
plt.show()

print("***********************************************************************")
plt.scatter(cdf.FUELCONSUMPTION_COMB, cdf.CO2EMISSIONS,  color='blue')
plt.xlabel("FUELCONSUMPTION_COMB")
plt.ylabel("Emission")
plt.show()

print("***********************************************************************")
plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS,  color='yellow')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()

print("***********************************************************************")
plt.scatter(cdf.CYLINDERS,cdf.CO2EMISSIONS,color='red')
plt.xlabel("CYLINDERS")
plt.ylabel("Emission")
plt.show()

print("***********************************************************************")
# we will tchose a trainning set 
trainEngine=cdf.ENGINESIZE
trainEmission=cdf.CO2EMISSIONS
plt.scatter(trainEngine,trainEmission,color='black')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()

print("***********************************************************************")
#modele de regression linear 
from sklearn import linear_model
regr = linear_model.LinearRegression()
X = np.array(df[["ENGINESIZE"]])
Y = np.array(df[["CO2EMISSIONS"]])
regr.fit(X,Y)

# The coefficients
print ('Coefficients: ', regr.coef_)
print ('Intercept: ',regr.intercept_)

print("***********************************************************************")
plt.scatter(trainEngine, trainEmission,  color='pink')
plt.plot(trainEngine, regr.coef_[0][0]*trainEngine + regr.intercept_[0], '-r')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()


print("***********************************************************************")

prediction = regr.predict(np.array(df[["ENGINESIZE"]]))
































