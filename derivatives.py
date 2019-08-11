import hypothesis as hp


def derivatives(theta0, theta1, X, y):
    dtheta0 = 0
    dtheta1 = 0
    for (xi, yi) in zip(X, y):
        deri = hp.hypothesis(theta0, theta1, xi) - yi
        dtheta0 += deri
        dtheta1 += (deri)*xi
    dtheta0 /= len(X)
    dtheta1 /= len(X)
    return dtheta0, dtheta1