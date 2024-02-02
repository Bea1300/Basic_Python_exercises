#Write a Python program that takes a list of integers as its input and then creates a set containing only the unique elements from the list. The program should print input list and the set so as one can visually compare the two
import random 

l = sorted([random.randint(1,50) for _ in range(20)])
l2 = set(l)
print(l)
print(l2)

#Write a Python program that prompts the user to enter a number, j, and then creates a tuple containing the first n even numbers up to j and prints the tuple. For extra points, also output odd numbers as you go.
j = int(input("Enter a positive whole number: "))
list1 = []
for n in range(j + 1):
    l.append(n) if n % 2 == 0 else print(n)

tuple1 = tuple(list1)
print(tuple1) 

#Write a Python program that reads a list of strings and creates a dictionary where the keys are the strings and the values are the length of the strings. Output your dictionary’s values (string lengths) first.
import random
import string

random_strings = []
for i in range(10):
    random_string = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(20, 50)))
    random_strings.append(random_string)
print(random_strings, '\n')

d = {k : len(k) for k in random_strings}
for i in d:
    print(d[i], i)

#Write a Python program that takes a list of integers as input and creates a tuple of the maximum and minimum values in the list.    
import random 
list_1= sorted([random.randint(1,50) for _ in range(20)]) 
tuple2 = (list_1) 

    