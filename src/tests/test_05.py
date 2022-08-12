import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, axs = plt.subplots(nrows=2, ncols=2)
xdata, ydata = [], []
# (ln,) = plt.plot([], [], "ro")

lines = []

for i in range(2):
    for j in range(2):
        (this_line,) = axs[i, j].plot([], [], "ro")
        lines.append(this_line)


# def init():
for i in range(2):
    for j in range(2):
        axs[i, j].set_xlim(0, 2 * np.pi)
        axs[i, j].set_ylim(-1, 1)
    # return (ln,)


def update(frame):
    # for i in range(2):
    #     for j in range(2):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    lines[0].set_data(xdata, ydata)
    lines[1].set_data(xdata, ydata)
    lines[2].set_data(xdata, ydata)
    lines[3].set_data(xdata, ydata)
    # ln
    return lines


ani = FuncAnimation(
    fig, update, frames=np.linspace(0, 2 * np.pi, 128), blit=True, interval=10
)
plt.show()


# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# df = pd.DataFrame(np.randn(1000, 4), index=ts.index, columns=list('ABCD'))

# arr3 = [None * 4]
# print(arr3)
# arr1 = np.zeros(250)
# arr2 = np.random.rand(150)


# arr1[0] = 13

# print(arr2)

# plt.plot(arr2)

# plt.show()

# a = {"1": 1, "2": 2}

# one = a["1"]
# a["1"] = 111
# print(f'{one=} and {a["1"]=}')
# def first():
#     print("first")
#     return True


# def second():
#     print("Second")
#     return True


# if first() or second():
#     print("Both")
