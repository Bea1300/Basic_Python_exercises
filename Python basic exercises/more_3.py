#Write a Python program that takes a list of integers as input and then prints the sum of all the even numbers in the list.
def sum_of_even_numbers(numbers):
    even_sum = 0

    for num in numbers:
        if num % 2 == 0:
            even_sum += num

    print("Sum of even numbers:", even_sum)

# Example usage:
input_numbers = [4, 7, 12, 5, 8, 10, 3]
sum_of_even_numbers(input_numbers)

# Write a Python program that reads a string and then prints the number of times each character appears in the string.
s = 'Now is the time to come to the aid of the party.'
d = dict()

for i in s.lower():
    if i.isalpha():  # Only consider alphabetical characters
        if i in d:
            d[i] += 1  # Increment count if the character already exists in the dictionary
        else:
            d[i] = 1  # Record we’ve seen character i for the first time (count = 1)

# Print the result
for char, count in d.items():
    print(f"{char}: {count} times")
