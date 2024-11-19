import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Define two sets (Set A and Set B)
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Define the universal set (all possible elements)
universal_set = {1, 2, 3, 4, 5, 6, 7, 8}  # For example

# Calculate the complement of Set A (everything in the universal set, except Set A)
complement_a = universal_set - set_a

# Calculate the complement of Set B (everything in the universal set, except Set B)
complement_b = universal_set - set_b

# Print the complements
print("Complement of Set A:", complement_a)
print("Complement of Set B:", complement_b)

# Plot the Venn diagram for the two sets (showing the complement as well)
venn = venn2([set_a, set_b], set_labels=('Set A', 'Set B'))

# Label the complement areas by highlighting the non-overlapping parts
venn.get_label_by_id('10').set_text(str(set_a - set_b))  # Set A only
venn.get_label_by_id('01').set_text(str(set_b - set_a))  # Set B only
venn.get_label_by_id('11').set_text(str(set_a & set_b))  # Intersection (Set A ∩ Set B)

# Show the plot
plt.title("Venn Diagram Showing the Complements of Set A and Set B")
plt.show()

# Optionally, you can visualize the complements by printing them as well
print("Complement of Set A:", complement_a)
print("Complement of Set B:", complement_b)
