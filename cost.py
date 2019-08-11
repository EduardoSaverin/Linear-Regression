import hypothesis as hp

def cost(theta0, theta1, X, y):
	costValue = 0
	for (xi, yi) in zip(X, y):
		costValue += 0.5 * ((hp.hypothesis(theta0, theta1, xi) - yi)**2)
	return costValue