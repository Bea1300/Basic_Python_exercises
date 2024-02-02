def times_tables():
    for number in range(2, 10):  # Outer loop for numbers 2 to 9
        print(f"Times Table for {number}:")
        for i in range(1, 13):  # Inner loop to generate the times table
            result = i * number
            print(f"{i} x {number} = {result}")
        print()  # Add a newline for better readability between tables

# Generate times tables for numbers 2 to 9
times_tables()

for n in range(10,-6, -1):
    print(n)