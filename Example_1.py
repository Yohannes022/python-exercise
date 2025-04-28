import numpy as np
import matplotlib.pyplot as plt

# Generate random age data
ages = np.random.randint(18, 81, 1000)

# Create the histogram
plt.figure(figsize=(10, 6))
plt.hist(ages, bins=10, edgecolor="black")

# Add labels and title
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Distribution of Customer Ages")

# Display the plot
plt.show()
