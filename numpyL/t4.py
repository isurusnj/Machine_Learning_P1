import numpy as np

array = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9],
                  [1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9],
                  [11,12,13],
                  ])

print(array.shape)

print(array[0:-1:3])
print("select raws")
# ':' gives the range, 'raws,column
#[0:2,0:2] raw 0 to 2 and column 0 to 2
print(array[0:2,0:2])

# [2:,2:] raw start with index 2 and all. columns start 2 an to the end
print(array[2:,2:])
