import random

# Generate 100 random numbers between 1 and 1000
random_numbers = [random.randint(1, 1000) for _ in range(100)]

# Print the numbers
print("Generated random numbers:")
for i, num in enumerate(random_numbers, 1):
    print(f"Number {i}: {num}")