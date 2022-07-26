import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use("fivethirtyeight")

x_vals = []
y_vals = []

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)


ax1.plot(x_vals, y_vals)


index = count()


def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0, 5))

    ax1.cla()
    ax1.plot(x_vals, y_vals)


ani = FuncAnimation(fig1, animate, interval=100)
plt.show()
# ax1.tight_layout()
# ax1.show()
