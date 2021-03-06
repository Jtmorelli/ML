""" Using the Diabetes dataset that is in scikit-learn, answer the questions below and create a scatterplot
graph with a regression line """

from optparse import Values
import matplotlib.pylab as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import datasets
from sklearn.model_selection import train_test_split


# how many sameples and How many features?
db = datasets.load_diabetes()

print(db.data.shape)


# What does feature s6 represent?
print(db)
print(db.DESCR)
# s6 = db[DESCR]["s6"]
# print(s6)

# print out the coefficient

X_train, X_test, y_train, y_test = train_test_split(db.data, db.target)

lr = LinearRegression()

lr.fit(X=X_train, y=y_train)

print(lr.coef_)

# print out the intercept

print(lr.intercept_)

# create a scatterplot with regression line

import seaborn as sns

axes = sns.scatterplot(
    data=db, x="data", y="target", hue="target", palette="winter", legend=False
)

axes.set_ylim(10, 70)

import numpy as np

x = np.array([min(db.data), max(db.data)])
print(x)
y = np.array([min(db.target), max(db.target)])
print(y)

import matplotlib.pyplot as plt

line = plt.plot(x, y)
plt.show()


#####################################################
""" Using the Diabetes dataset that is in scikit-learn, answer the questions below and create a scatterplot
graph with a regression line """

import matplotlib.pylab as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import datasets

diabetes = datasets.load_diabetes()

# how many samples and How many features?
print(diabetes.data.shape)

print(diabetes)

# 442, 10

# What does feature s6 represent?
print(diabetes.DESCR)

# glu, blood sugar level


# print out the coefficient
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    diabetes.data, diabetes.target, random_state=11
)

linear_regression = LinearRegression()

linear_regression.fit(X=X_train, y=y_train)

print(linear_regression.coef_)
# [ -60.22189333 -266.45890749  523.0596748   310.51485159 -336.17030793
#  137.34454454 -131.1356043    -1.14855016  622.33749249   60.46751764]

# print out the intercept
print(linear_regression.intercept_)
# 152.22835839334243


# create a scatterplot with regression line
predicted = linear_regression.predict(X_test)

expected = y_test

plt.plot(expected, predicted, ".")

x = np.linspace(0, 330, 100)
y = x
plt.plot(x, y)
plt.show()
