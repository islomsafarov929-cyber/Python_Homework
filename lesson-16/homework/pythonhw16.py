# Task 1.Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.

import numpy as np

my_list = [12.23, 13.32, 100, 36.32]

print(np.array(my_list))

# Task 2.Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

import numpy as np

num = range(2,11)

print(np.array(num).reshape(3,3))


# Task 3.Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.

import numpy as np

nulls = np.zeros(10)
nulls[5] = 11  
print(nulls)


# Task 4.Write a NumPy program to create an array with values ranging from 12 to 38.

import numpy as np 

arr = np.arange(12,39)

print(arr)


# Task 5.Write a NumPy program to convert an array to a floating type.

import numpy as np

arr_int = np.arange(1,5)

arr_float = arr_int.astype(float)

print(arr_float)


# Task 6.Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees. Centigrade values are stored in a NumPy array.

import numpy as np

fahrenheit_values = np.array([0, 12, 45.21, 34, 99.91, 32])
celsius_values = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])

# Convert Fahrenheit → Celsius
converted_celsius = np.round((fahrenheit_values - 32) * 5/9, 2)

# Convert Celsius → Fahrenheit
converted_fahrenheit = np.round(celsius_values * 9/5 + 32, 2)

print("Values in Fahrenheit degrees:", fahrenheit_values)
print("Converted to Centigrade degrees:", converted_celsius)

print("Values in Centigrade degrees:", celsius_values)
print("Converted to Fahrenheit degrees:", converted_fahrenheit)



# Task 7.Write a NumPy program to append values to the end of an array.

import numpy as np 

arr_tsk7 = np.array( [10, 20, 30])

appended_arr = np.append(arr_tsk7, [40, 50, 60, 70, 80, 90])

print(appended_arr)


# Task 8.Create a random NumPy array of 10 elements and calculate the mean, median, and standard deviation of the array.

import numpy as np

rand_arr = np.random.randint(1, 100, 10)

mean = np.mean(rand_arr)
median = np.median(rand_arr)
standard_deviation = np.std(rand_arr)

print("Original array:", rand_arr)
print("Mean of the array:", mean)
print("Median of the array:", median)
print("Standard deviation of the array:", standard_deviation)



# Task 9.Create a 10x10 array with random values and find the minimum and maximum values.

import numpy as np

arr_tsk9 = np.random.randint(1, 250, size=(10,10))
minimum = np.min(arr_tsk9)
maximum = np.max(arr_tsk9)

print("Original array:", arr_tsk9)
print("Minimum value of the array:", minimum)
print("Maximum value of the array:", maximum)


# Task 10.Create a 3x3x3 array with random values.

import numpy as np

arr_tsk10 = np.random.randn(3,3,3)

print(arr_tsk10)

