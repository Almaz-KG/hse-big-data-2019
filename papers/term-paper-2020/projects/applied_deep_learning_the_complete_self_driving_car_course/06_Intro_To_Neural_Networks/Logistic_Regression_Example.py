import numpy as np
import matplotlib.pyplot as plt


def draw(x1, x2):
    ln = plt.plot(x1, x2)
    plt.pause(0.0001)
    ln[0].remove()


def gradient_descent(line_parameters, points, y, alpha):
    for i in range(1000):
        p = sigmoid(points * line_parameters)
        m = points.shape[0]
        gradient = points.T * (p - y) * (alpha / m)
        line_parameters = line_parameters - gradient

        w1 = line_parameters.item(0)
        w2 = line_parameters.item(1)
        b = line_parameters.item(2)

        x1 = np.array([points[:, 0].min(), points[:, 0].max()])
        x2 = - (w1 * x1 + b) / w2

        draw(x1, x2)
        print(calculate_error(line_parameters, points, y))


def sigmoid(score):
    return 1 / (1 + np.exp(-score))


def calculate_error(line_parameters, points, y):
    p = sigmoid(points * line_parameters)
    m = points.shape[0]
    cross_entropy = -(1 / m) * (np.log(p).T * y + np.log(1 - p).T * (1 - y))
    return cross_entropy


n_pts = 100

bias = np.ones(n_pts)
np.random.seed(0)

random_x1_values = np.random.normal(10, 2, n_pts)
random_y1_values = np.random.normal(12, 2, n_pts)

random_x2_values = np.random.normal(5, 2, n_pts)
random_y2_values = np.random.normal(6, 2, n_pts)

top_region = np.array([random_x1_values, random_y1_values, bias]).T
bottom_region = np.array([random_x2_values, random_y2_values, bias]).T

all_points = np.vstack((top_region, bottom_region))
line_parameters = np.matrix(np.zeros(3)).T

linear_combination = all_points * line_parameters
y = np.array([np.zeros(n_pts), np.ones(n_pts)]).reshape(n_pts * 2, 1)
error = calculate_error(line_parameters, all_points, y)

line_parameters = np.matrix(np.zeros(3)).T
_, ax = plt.subplots(figsize=(4, 4))
ax.scatter(top_region[:, 0], top_region[:, 1], color="r")
ax.scatter(bottom_region[:, 0], bottom_region[:, 1], color="b")
gradient_descent(line_parameters, all_points, y, 0.06)
plt.show()
