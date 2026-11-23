import numpy as np

nums = np.array([12, 25, 38, 45, 56, 67, 78, 89])
num2 = nums.reshape(2,4)

print(nums)
print(nums[0])
print(nums[-1])
print(nums[0:4])
print(np.ndim(nums))
print(num2)
print(np.ndim(num2))
print(np.sum(nums))
print(np.mean(nums))