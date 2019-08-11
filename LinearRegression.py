import numpy as np
import plotLine as plot
import updateParameters as up
import cost


# When you run this, it randomly initializes θ₁ and θ₀, and then iterates 1000 times
# to update the parameters to reduce the error. Every 100 times, it outputs what
# the line looks like to show us our progress.
# Here alpha = 0.005 is learning rate

def LinearRegression(X, y,theta0, theta1):
	for i in range(0, 1000):
		if i % 100 == 0:
			plot.plotline(theta0, theta1, X, y)
		print(cost.cost(theta0, theta1, X, y))
		theta0, theta1 = up.updateParameters(theta0, theta1, X, y, 0.005)