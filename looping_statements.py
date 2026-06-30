# Write a Python program that uses a for loop to iterate over a list of numbers and calculate the sum of the squares of each number.
A=[1, 2, 3, 4, 5]
sum_of_squares = 0
for x in A:
    sum_of_squares = sum_of_squares + x**2
print("The sum of the squares is:", sum_of_squares)
# Create a Python function that takes a string as input and uses a for loop to print each character of the string on a new line.
B=str(input("enter a string: "))
for x in B:
    print(x)
# Implement a for loop in Python to find the maximum number in a given list of integers.
C=[1,2,3,4,5,6,7,8,9]
for x in C:
    max_num = max(C)
print("The maximum number is:", max_num)

# Develop a Python script that utilizes a for loop to generate and print the first 10 Fibonacci numbers.
fibonacci = [0, 1]
for i in range(8):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
print("The first 10 Fibonacci numbers are:", fibonacci)

# Use a for loop in Python to iterate over a dictionary and print each key-value pair.
D = {"a": 1, "b": 2, "c": 3}
for key, value in D.items():
    print(key, ":", value)