# the task: Mean-Variance-Standard Deviation Calculator
# Create a function named calculate() in mean_var_std.py that uses Numpy to output
# the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.
# The input of the function should be a list containing 9 digits.
# The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.

import numpy as np
def calculate(list):
    arr = np.array(list)
    y = arr.reshape(3,3)
    m_1, m_2, m_3 = np.mean(y, axis = 0), np.mean(y , axis = 1), np.mean(y)
    v_1, v_2, v_3 = np.var(y, axis = 0), np.var(y , axis = 1), np.var(y)
    s_1, s_2, s_3 = np.std(y, axis = 0), np.std(y , axis = 1), np.std(y)
    x_1, x_2, x_3 = np.max(y, axis = 0), np.max(y , axis = 1), np.max(y)
    min_1, min_2, min_3 = np.min(y, axis = 0), np.min(y , axis = 1), np.min(y)
    sum_1, sum_2, sum_3 = np.sum(y, axis = 0), np.sum(y , axis = 1), np.sum(y)
    calculations = {
        'mean': [m_1, m_2, m_3],
        'variance': [v_1, v_2, v_3],
        'standard deviation': [s_1, s_2, s_3],
        'max': [x_1, x_2, x_3],
        'min': [min_1, min_2, min_3],
        'sum': [sum_1, sum_2, sum_3]
    }
    return calculations

