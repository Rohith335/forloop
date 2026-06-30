# Write a Python function that uses a for loop to calculate the sum of all numbers in a given list.
A=[1,2,3,4,5,6,7,8]
B=0
for x in A:
    B = B + x
print("sum of all numbers: ", B)


# Create a Python program that uses a for loop to print out each character of a given string on a new line.
C=str(input("enter string: "))
for x in C:
    print(x)
# Use a for loop to iterate over a list of numbers and print out only the even numbers.
D=[1,2,3,4,5,6,7,8,9,10]
for x in D:
    if x%2==0:
        print(x)
# Write a Python function that takes a list of words as input and uses a for loop to print out the length of each word.
E=['rohith','sunny', 'nani', 'rithu']
for x in E:
    print(x,len(x))
# Use a for loop to iterate over a list of numbers and calculate the average of the numbers.
F=[1,2,3,4,5,6,7,8,9]
for x in F:
    total = sum(F)
    average = total / len(F)
print("average of numbers: ", average)