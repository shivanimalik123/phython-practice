# phython slicing practice question
# Ques(1)
data=[[1,2,3],[4,5,6],[7,8,9]]
print(data[0] [-2:])
print(data[1] [-2:])
print(data[2] [-2:])

# Ques(2)
text="abcdefghijklmnopqrstuvwxyz"
print(text[20:4:-1])
print(text[5:21] [::-1])

# Ques(3)
nums=[5,10,15,20,25,30,35,40]
nums[2:6]=[100,200,300,400]
print(nums)

# Ques(4)
text = input("enter a string")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Q