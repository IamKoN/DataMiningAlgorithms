#% matplotlib inline
from matplotlib import pyplot as plt
import matplotlib as mpl


def plot_coin_likelihood(rolls, thetas=None):
    # grid
    xvals = np.linspace(0.01, 0.99, 100)
    yvals = np.linspace(0.01, 0.99, 100)
    X, Y = np.meshgrid(xvals, yvals)

    # compute likelihood
    Z = []
    for i, r in enumerate(X):
        z = []
        for j, c in enumerate(r):
            z.append(coin_marginal_likelihood(rolls, c, Y[i][j]))
        Z.append(z)

    # plot
    plt.figure(figsize=(10, 8))
    C = plt.contour(X, Y, Z, 150)
    cbar = plt.colorbar(C)
    plt.title(r"Likelihood $\log p(\mathcal{X}|\theta_A,\theta_B)$", fontsize=20)
    plt.xlabel(r"$\theta_A$", fontsize=20)
    plt.ylabel(r"$\theta_B$", fontsize=20)

    # plot thetas
    if thetas is not None:
        thetas = np.array(thetas)
        plt.plot(thetas[:, 0], thetas[:, 1], '-k', lw=2.0)
        plt.plot(thetas[:, 0], thetas[:, 1], 'ok', ms=5.0)


def coin_marginal_likelihood(rolls, biasA, biasB):
    # P(X | theta)
    trials = []
    for roll in rolls:
        h = roll.count("H")
        t = roll.count("T")
        likelihoodA = coin_likelihood(roll, biasA)
        likelihoodB = coin_likelihood(roll, biasB)
        trials.append(np.log(0.5 * (likelihoodA + likelihoodB)))
    return sum(trials)


