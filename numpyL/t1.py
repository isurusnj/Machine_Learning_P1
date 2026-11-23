import numpy as np

student1 = np.array([78, 79, 80, 81, 82])
student2 = np.array([40, 60, 80, 100, 120])

s1Avg = np.mean(student1)
s2Avg = np.mean(student2)

print(s1Avg)
print(s2Avg)

s1Std = np.std(student1)
s2Std = np.std(student2)

print(s1Std)
print(s2Std)


bothst = np.append(student1,student2)
print(bothst)

#reshaping

reShape = bothst.reshape(5,2)
print(reShape)

#filtering

s1passMarks = student1[student1 >=50]
s2passMarks = student2[student2 >=50]

print("pass ",s1passMarks)
print("pass ",s2passMarks)

