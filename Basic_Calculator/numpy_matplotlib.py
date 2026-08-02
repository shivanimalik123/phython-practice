# 1.
# import numpy as np
# arr=np.arange(1,11)
# print(arr)

# 2.
# import numpy as np
# arr=np.arange(2,21,2)
# print(arr)

# 3.
# import numpy as np
# a=np.array([1,2,3,4,5])
# print(a)

# 4.
# import numpy as np
# b = np.array([1,2,3,45])
# print(b.dtype)

# 5.
# import numpy as np
# arr = np.array([3,6,9,12,15])
# print(arr.size)

# 6.
# import numpy as np
# arr = np.array([[2,4,6,8],
#                 [3,6,9,12]])
# print(arr)

# 7.
# import numpy as np
# arr = np.zeros(5)
# print(arr)

# 8.
# import numpy as np
# arr = np.array([[1,2,3],[4,5,6]])
# print(arr.shape)

# 9.
# import numpy as np
# arr = np.arange(1,13)
# arr = arr.reshape(3,4)
# print(arr)

# 10.
# import numpy as np
# arr = np.arange(1,13)
# arr = arr.reshape(2,6)
# print(arr)

# 11.
# import numpy as np
# arr = np.array([1,2,3,4,5,6,7,8])
# arr = arr.reshape(2,4)
# print(arr)

# 12.
# import numpy as np
# arr = np.arange(1,9)
# arr = arr.reshape(4,2)
# print(arr)

# JOIN & SPLIT

# 1.
# import numpy as np
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# arr = np.concatenate((arr1,arr2))
# print(arr)

# 2.
# import numpy as np
# arr1 = np.array([[1,2],[3,4]])
# arr2 = np.array([[5,6],[7,8]])
# arr = np.vstack((arr1,arr2))
# print(arr)

# 3.
# import numpy as np
# arr1 = np.array([[1,2],[3,4]])
# arr2 = np.array([[5,6],[7,8]])
# arr = np.hstack((arr1,arr2))
# print(arr)

# 4.
# import numpy as np
# arr = np.array([1,2,3,4,5,6])
# new = np.split(arr,3)
# print(new)

# 5.
# import numpy as np
# arr = np.array([1,2,3,4,5,6,7,8])
# old = np.split(arr,4)
# print(old)

# 6.
# import matplotlib.pyplot as plt
# x = [1,2,3,4,5]
# y = [2,4,6,8,10]
# plt.plot(x , y)
# plt.show() 

# 7.
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.plot(x,y)
plt.title("Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()