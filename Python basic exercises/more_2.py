#Write a Python program that takes a list of numbers as input and prints the largest and smallest numbers in the list.
#Write a Python program that reads a list of integers and then prints the second largest number in the list (of course, assume that the list contains different values).
import random

list = [random.randint(1,50) for _ in range(20)]
print(list)

low = list[0]
high = 0

for n in list:
    if n < low: 
        low = n

    if n > high:
        high = n
print(low)
print(high)

list = sorted(list)
print(list)
new = list[-2]
print(new)

#Write a Python program that prompts the user to enter a number, and then prints all the divisors of that number.
n = int(input("Enter a number: "))

divisors = []
for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)

print(f"Number: {n}")
print("Divisors:", divisors)

#Write a Python program that takes a list of integers as input and then prints the sum of all the even numbers in the list.
list_1 = [1,2,3]

def list_of_numbers(list_1):
    if list_1 % 2 == 0:
        print(list_1)