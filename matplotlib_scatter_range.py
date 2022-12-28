import matplotlib.pyplot as plt

#scatter plot using range for more values

#use list range to plot 1000 numbers
x_values = list(range(1, 1001))

#list comprehension to loop through x values and squaring each number, and storing in y value

y_values = [x**2 for x in x_values]

#color red, no edgecolor, size variable selected as 40
#for color you can also use the RGB codes such as c='0, 0, 0.8'
#plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)

#This color gradient show a shift from light to dark
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

#set chart title and label axes
plt.title("Square Numbers",fontsize=18)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#set the range for each axis
plt.axis([0, 1100, 0, 1100000])

plt.show()

#Save image to file in same directory as python script
plt.savefig('squares_plot.png', bbox_inches='tight')
