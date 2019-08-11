from sklearn.datasets import make_regression
import LinearRegression
import numpy as np
import plotLine as plot


X,y = make_regression(n_samples=10000,n_features=1,noise=0.4,bias=50)


theta0 = np.random.rand()
theta1 = np.random.rand()

plot.plotline(theta0, theta1, X, y)

LinearRegression.LinearRegression(X,y,theta0,theta1)