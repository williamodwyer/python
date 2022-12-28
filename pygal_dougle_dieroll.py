from random import randint
import pygal

class Die():
    #A class representing a single die (6 sides can be changed if needed)

    def __init__(self, num_sides=6):
        #Assume a 6 sided die
        self.num_sides = num_sides


    def roll(self):
        #return random value 1-5
        return randint(1, self.num_sides)

#create 6 sided die
die_1 = Die()
die_2 = Die()
#create a list to save values to
results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#print(results)
#prints results of all 1000 die throws

#analyze the results

#create new list to store number of times each value is rolled
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
#prints just the frequencies of each side rolled

##################
#Create a Histogram
##################

#visualize the results of die roll simulator above

hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times"
hist.x_labels = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')
