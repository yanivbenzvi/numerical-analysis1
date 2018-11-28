import matplotlib.pyplot as plt
import numpy as np
import cv2

# Create functions and set domain length
x = np.arange(-5, 5, 0.1)
y = 2**x

# Plot functions and a point where they intersect
plt.plot(x, y)

# Config the graph
plt.title('A Cool Graph')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

# Show the graph
plt.show()
