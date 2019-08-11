import numpy as np
import matplotlib.pyplot as plt

def plotline(theta0, theta1, X, y):
    max_x = np.max(X) + 100
    min_x = np.min(X) - 100
    xplot = np.linspace(min_x, max_x, 1000)
    yplot = theta1*xplot + theta0
    plt.plot(xplot,yplot,color='#ff0000',label='Linear Regression')
    plt.scatter(X,y)
    plt.axis([-10, 10, 0, 200])
    plt.show()
