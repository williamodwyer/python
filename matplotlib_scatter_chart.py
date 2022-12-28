import matplotlib.pyplot as plt
# basic scatter plot graph


x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]
plt.scatter(x_values, y_values, s=100)

#set chart title and label axes
plt.title("Square Numbers",fontsize=18)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#Set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
