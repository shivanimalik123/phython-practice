
# 1.
# import matplotlib.pyplot as plt
# x = [1,2,3,4,5]
# y = [2,4,6,8,10]
# plt.plot(x , y)
# plt.show() 

# 2.
# import matplotlib.pyplot as plt
# x = [1,2,3,4,5]
# y = [2,4,6,8,10]
# plt.plot(x,y)
# plt.title("Line Graph")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()

# 3.
# import matplotlib.pyplot as plt
# plt.plot([1,2,3,4,5],[2,4,6,8,10])
# plt.show()

# 4.LABELS & TITLES
# import matplotlib.pyplot as plt
# x = [1,2,3,4,5]
# y = [2,4,6,8,10]
# plt.plot(x, y)
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.title("Simple Line Plot")
# plt.show()

# 5.GRID PLOT
# import matplotlib.pyplot as plt
# x = [1,2,3,4,5]
# y = [2,4,6,8,10]
# plt.plot(x, y)
# plt.title("Line Plot With Grid")
# plt.grid(True)
# plt.show()

# 6. LEGEND
# import matplotlib.pyplot as plt
# x = [1,2,3,4,5]
# y1 = [2,4,6,8,10]
# y2 = [1,2,3,4,5]
# plt.plot(x, y1, label="Line 1")
# plt.plot(x, y2, label="Line 2")
# plt.title("Line Plot With Legend")
# plt.legend()
# plt.show()

# 7. BAR CHARTS VERTICAL
# import matplotlib.pyplot as plt
# categories = ["A","B","C","D"]
# values = [4,7,2,9]
# plt.bar(categories,values)
# plt.title("Vertical Bar Chart")
# plt.xlabel("Categories")
# plt.ylabel("Values")
# plt.show()

# 8. PIE CHARTS
# import matplotlib.pyplot as plt
# sizes = [30,20,25,25]
# labels = ["A","B","C","D"]
# plt.pie(sizes,labels=labels,autopct="%1.1f%%")
# plt.title("Pie Chart Example")
# plt.show()

# 9.BAR CHARTS (HORIZONTAL)
# import matplotlib.pyplot as plt
# categories = ["A","B","C","D"]
# values = [2,4,6,8]
# plt.barh(categories,values)
# plt.title("Horizontal Bar Chart")
# plt.xlabel("Values")
# plt.ylabel("Categories")
# plt.show()

# 10.PIE CHART
# import matplotlib.pyplot as plt
# sizes = [10,20,30,40]
# labels = ["A","B","C","D"]
# plt.pie(sizes,labels=labels,autopct="%1.1f%%")
# plt.title("Pie Chart Example")
# plt.show()

# 11.PLOT CUSTOMIZATION
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.plot(x,y,color="green",marker="o",linestyle="--",label="Line 1")
plt.title("Customized Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.legend()
plt.show()