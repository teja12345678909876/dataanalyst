import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Define two sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Calculate the intersection of the two sets
intersection = set_a & set_b  # Equivalent to set_a.intersection(set_b)

# Print the intersection
print("Intersection of Set A and Set B:", intersection)

# Plot the Venn diagram for the two sets (showing the intersection)
venn = venn2([set_a, set_b], set_labels=('Set A', 'Set B'))

# Label the intersection with the actual common elements
venn.get_label_by_id('11').set_text(str(intersection))  # Intersection (Set A ∩ Set B)

# Show the plot
plt.title("Venn Diagram Showing the Intersection of Set A and Set B")
plt.show()

