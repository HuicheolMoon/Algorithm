import numpy as np
import matplotlib.pyplot as plt


def MC(n):
    result = 0
    x_in = []
    y_in = []
    x = np.array([np.random.random_sample() for i in range(n)])
    y = np.array([np.random.random_sample() for i in range(n)])
    for i in range(n):
        if y[i] < np.sqrt(1 - (x[i] ** 2)):
            x_in.append(x[i])
            y_in.append(y[i])
            result += 1
    result = (result / n) * 4
    error = result - np.pi
    return x_in, y_in, result, error


def plot_pi(n):
    plt.figure(figsize=(4, 4))
    x_in, y_in, result, error = MC(n)
    plt.plot(x_in, y_in, "b.")
    plt.text(0.0, 1.1, f"MC_pi = {result}, error = {error}", fontsize=8)
    plt.show()


iter = 10000
plot_pi(iter)