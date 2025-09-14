import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# --- Grid Setup ---
rows, cols = 20, 20
grid = np.zeros((rows, cols))  # 0 = dirty, 1 = cleaned

# Obstacles (optional)
obstacles = [(5, y) for y in range(5, 15)] + [(15, y) for y in range(3, 18)]
for (x, y) in obstacles:
    grid[x, y] = -1  # -1 = obstacle

# Robot start position
robot_pos = [10, 10]
grid[robot_pos[0], robot_pos[1]] = 1  # mark as cleaned

# --- Movement ---
directions = [(0,1),(0,-1),(1,0),(-1,0)]  # right, left, down, up
path = [tuple(robot_pos)]

def step():
    global robot_pos
    dx, dy = random.choice(directions)
    new_x = robot_pos[0] + dx
    new_y = robot_pos[1] + dy

    # Check boundaries & obstacles
    if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x, new_y] != -1:
        robot_pos = [new_x, new_y]
    grid[robot_pos[0], robot_pos[1]] = 1
    path.append(tuple(robot_pos))

# --- Animation ---
fig, ax = plt.subplots()

def update(frame):
    step()
    ax.clear()
    ax.imshow(grid.T, cmap="gray_r", origin="lower")
    # Draw robot
    ax.scatter(robot_pos[0], robot_pos[1], c="red", s=100, marker="o", label="Robot")
    ax.set_title(f"Robot Vacuum Cleaner Simulation (Step {frame})")
    ax.legend(loc="upper right")

ani = animation.FuncAnimation(fig, update, frames=200, interval=200, repeat=False)
plt.show()
