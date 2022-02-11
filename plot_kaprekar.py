'''
Author: Angela Zhang
Date: Feb. 10, 2022
Purpose: A Python Program to create a graph of Kaprekar Constant Distribution
SOURCES CONSULTED:
    https://www.educative.io/edpresso/how-to-plot-graphs-using-json-files-in-python
    https://www.kite.com/python/answers/how-to-display-the-value-of-each-bar-in-a-bar-chart-using-matplotlib-in-python
    https://chartio.com/resources/tutorials/how-to-save-a-plot-to-a-file-using-matplotlib/
'''

import matplotlib.pyplot as plt
from kaprekars_constant import find_num_steps_to_kaprekar_for_all_nums

d = find_num_steps_to_kaprekar_for_all_nums()
xAxis2 = [key for key, value in d.items()]
yAxis2 = [value for key, value in d.items()]

## BAR GRAPH ##
fig = plt.figure()
plt.bar(xAxis2, yAxis2, color='maroon')
plt.title("How are the Kaprekar's Constant Numbers Distributed?")
plt.xlabel("Number of Steps to Kaprekar's Constant")
plt.ylabel('Number Value')

# ADDING NUMBERS FOR EACH BAR VALUE TO BAR GRAPH
for key in d:
    text = str(d[key])
    plt.text(key - 0.3, d[key] + 20, str(d[key]))

plt.savefig('kaprekar_distribution.png')
plt.show()