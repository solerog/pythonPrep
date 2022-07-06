import numpy as np

# Python lists
height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

# NumPy arrays
# Can contain only one type
np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_weight / np_height**2
print(bmi)

np_2d = np.array([[1.73, 1.68, 1.71], [65.4, 59.2, 63.6]])
print(np_2d.shape)  # (2, 3)
print(np_2d[0][2])  # 1.71
print(np_2d[0, 2])  # 1.71
print(np_2d[:, 1:3])  # [[ 1.68  1.71 ] [ 59.2  63.6 ]]
print(np_2d[1, :])  # [ 65.4  59.2  63.6 ]
