#Write a Python program that takes a list of integers as input and creates a tuple of the maximum and minimum values in the list.    
import random 
l = [random.randint(1, 50) for _ in range(20)]
l = sorted(l)
l2 = tuple(l)
print(l2)
print(f'Min value is {l[0]}, Max value is {l[19]}')

#Write a Python program that takes a list of integers as input and returns the sum of all the even numbers in the list.
import random

def sum_of_even_numbers(my_list):
    total_sum = 0

    for number in my_list:
        if number % 2 == 0:
            print(number)
            total_sum += number

    return total_sum

# Generate a list of 20 random integers between 1 and 50
l = [random.randint(1, 50) for _ in range(20)]

# Print the list and the sum of even numbers in the list
print("Generated list:", l)
print(f'The sum of even numbers is {sum_of_even_numbers(l)}')

#Write a Python program that takes a string as input and returns a new string that contains only the vowels from the original string.
def extract_vowels(input_string):
    vowels = 'aeiou'
    result = ''.join(char for char in input_string if char.lower() in vowels)
    return result

# Example usage:
user_input = input("Enter a string: ")
vowel_result = extract_vowels(user_input)

print(f"Vowels in the string: {vowel_result}")

#Write a Python program that takes two lists of integers as input and returns a new list that contains only the elements that appear in both of the original lists.
import random
def my_function(numbers1, numbers2):
    common = []
    for i in numbers1:
        if i in numbers2:
            if i not in common:
                common.append(i)
            print(i)
    return common

l1 = [random.randint(1, 50) for _ in range(20)]
l2 = [random.randint(1, 50) for _ in range(20)]

print(l1)
print(l2)
print(f'The common values in these two lists are {my_function(l1, l2)}')
 
