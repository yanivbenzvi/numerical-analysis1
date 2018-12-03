import matplotlib.pyplot as plt
import numpy as np

# Create functions and set domain length
x = np.arange(-5, 5, 0.1)
y = x-5


def PrintGraph4shiri(func):
    global y
    y= func
    # Plot functions and a point where they intersect
    plt.plot(x, y)

    # Config the graph
    plt.title('A Cool Graph')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)

    # Show the graph
    plt.show()


PrintGraph4shiri(x**5)




