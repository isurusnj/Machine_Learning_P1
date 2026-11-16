
import numpy as np


oneDimanstinalArray = np.array([1,2,3,4,5,6])

twoDimanstionalArray = np.array([[1,2,3],[4,5,6],[8,9,10]])

threeDimasionalArray = np.array([
                        [
                            [10,20,30],[40,50,60]
                        ],
                        [
                         [70,80,90],[100,110,120]
                        ]
                        ])

print(oneDimanstinalArray)
print(oneDimanstinalArray.ndim)

print(twoDimanstionalArray)
print(twoDimanstionalArray.ndim)
print(threeDimasionalArray)
print(threeDimasionalArray.ndim)

print("shape ",threeDimasionalArray.shape)
print("data type ",threeDimasionalArray.dtype)
print("total elements ",threeDimasionalArray.size)

zeros = np.zeros((2,3))
print(zeros)

ones = np.ones((3,2))
print(ones)

numbers = np.arange(1,12)
print(numbers)

#array insex and slicing

print(oneDimanstinalArray[1])
print(oneDimanstinalArray[5])
print(oneDimanstinalArray[-1])

print(twoDimanstionalArray[1,2])

print(threeDimasionalArray[1,1,2])



#Statistical operation

print("avareage : ",np.mean(numbers))
print("middle value : ",np.median(numbers))
print("standerd deviation : ",np.std(numbers))
print("sum of ",np.sum(numbers))
print("index of max num",np.argmax(numbers))
print("index of min num",np.argmin(numbers))
print(" max num",np.max(numbers))
print(" min num",np.min(numbers))
