import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


df = pd.read_csv('CarPrice.csv')
# print(df)
# target 분할
target = ['price']
feature = ['symboling', 'wheelbase', 'carlength', 'carwidth', 'carheight', 'curbweight', 'enginesize', 'boreratio', 'stroke', 'compressionratio', 'horsepower', 'peakrpm', 'citympg', 'highwaympg']
# carlength, carwidth, carheight, curbweight, enginesize, boreratio, stroke, compressionratio, horsepower, peakrpm, citympg, highwaympg'
# 'symboling, CarName, fueltype, aspiration, doornumber, carbody, drivewheel, enginelocation, wheelbase, carlength, carwidth, carheight, curbweight, enginetype, cylindernumber, enginesize, fuelsystem, boreratio, stroke, compressionratio, horsepower, peakrpm, citympg, highwaympg'
X = df[feature]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 777)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(model.score(X_train, y_train))

# X_1 = [[3, 99.8, 176.6, 66.2, 54.3, 2337, 109, 3.19, 3.4, 10, 102, 5500, 24, 30]]
# y_pred2 = model.predict(X_1)
# print(y_pred2)
pickle.dump(model, open('model.pkl','wb'))