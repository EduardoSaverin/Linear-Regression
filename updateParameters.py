import derivatives as dv


def updateParameters(theta0, theta1, X, y, alpha):
	dtheta0, dtheta1 = dv.derivatives(theta0, theta1, X, y)
	theta0 = theta0 - (alpha * dtheta0)
	theta1 = theta1 - (alpha * dtheta1)

	return theta0, theta1