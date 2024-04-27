# Write a python code to find mean and standard deviation of a given list of numbers

import statistics

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
mean = sum(numbers) / len(numbers)
std_dev = statistics.stdev(numbers)

print("Mean:", mean)
print("Standard Deviation:", std_dev)
