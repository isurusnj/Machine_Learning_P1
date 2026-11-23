import numpy as np

marks = np.array([
    [75, 80, 85],
    [45, 55, 60],
    [90, 95, 92],
    [35, 40, 50],
    [65, 70, 75]
])


print(marks)

print(marks.ndim)
print(marks.shape)
students = marks.shape[0]
subjects = marks.shape[1]

print("Students:", students)
print("Subjects:", subjects)

print(marks.mean(axis=0))