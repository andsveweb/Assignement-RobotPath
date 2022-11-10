
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')

# plots a 4x4 grid and clear out the x and y ticks
fig, ax = plt.subplots(4, 4, sharex='col', sharey='row')
fig.suptitle('Robot movement')
plt.setp(ax, xticks=[], yticks=[])

# plots cordinates in boxes with darkblue background that symbols obstacles
for i in range(4): 
    for j in range(4):
        ax[i, j].text(0.5, 0.5, '('+str(j)+','+str(3-i)+')',
                      ha='center', va='center', size=20, alpha=.5)
        if (i == 1 and j == 2) or (i == 2 and j == 2) or (i == 1 and j == 1):
            ax[i, j].set_facecolor('darkblue')
            ax[i, j].text(0.5, 0.5, '('+str(j)+','+str(3-i)+')',
                          ha='center', va='center', size=20, alpha=1, color='white')

# load image and set as background at (0,0)
robot = plt.imread('robot.jpg') 
ax[3, 0].imshow(robot, extent=[0, 1, 0, 1])


# moving robot from start bottom left to top left andding a pause between each step clearing the path after moving to next position
for j in range(1):
    for i in range(4):
        ax[3-i, j].imshow(robot, extent=[0, 1, 0, 1])
        plt.setp(ax, xticks=[], yticks=[])
        plt.pause(1)
       # clear robot and move to next position
        ax[3-i, j].clear()
        ax[3-i, j].set_facecolor('white')

# moving robot from top left to top right andding a pause between each step clearing the path after moving to next position
for j in range(4):
    for i in range(1):
        ax[0-i, j].imshow(robot, extent=[0, 1, 0, 1])
        plt.setp(ax, xticks=[], yticks=[])
        plt.pause(1)
       # clear robot and move to next position
        ax[0-i, j].clear()
        ax[0-i, j].set_facecolor('white')
        plt.setp(ax, xticks=[], yticks=[])

plt.show()
