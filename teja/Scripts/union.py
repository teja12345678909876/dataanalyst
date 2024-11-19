import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Define two sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Plot the Venn diagram showing the union of the two sets
venn2([set_a, set_b], set_labels=('Set A', 'Set B'))

# Show the plot
plt.title("Venn Diagram for Union of Set A and Set B")
plt.show()
