import random

def roll_die(sides=6):
    """
    Roll a die with specified number of sides (default is 6)
    Returns a number between 1 and the number of sides
    """
    return random.randint(1, sides)

# Example usage
# Single roll
result = roll_die()
print(f"You rolled: {result}")

# Multiple rolls
num_rolls = 5
print(f"\nRolling the dia {num_rolls} times:")
for i in range(num_rolls):
    result = roll_die()
    print(f"Roll {i+1}: {result}")

# Example with different sided die (like a 20-sided die for D&D)
d20_result = roll_die(20)
print(f"\nD20 roll: {d20_result}")