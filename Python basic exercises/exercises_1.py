for n in range(1,101):
    if n%3 == 0 and n%5 == 0:
        print('fizzbuzz')
    elif n%3 == 0:
        print('fizz')
    elif n%5 == 0:
        print('buzz')
    else:
        print(n)


start = 1
end = 100
total = 0
for n in range(start, end + 1):
    total += n
    print("The total is", total)       


def calculate_factorial(number):
    factorial = 1

    # Check if the input number is non-negative
    if number < 0:
        return "Factorial is undefined for negative numbers."

    # Calculate the factorial using a loop
    for i in range(1, number + 1):
        factorial *= i

    return factorial

# Example: Calculate the factorial of 5
#number_to_calculate_factorial = 10
number_to_calculate_factorial=int(input('What number do you want to !?'))
result = calculate_factorial(number_to_calculate_factorial)

print(f"The factorial of {number_to_calculate_factorial} is: {result}")

table = 6

for n in range(1,13):
    result = table*n 

print(result)
