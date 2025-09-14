import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# --- Grid Setup ---
rows, cols = 20, 20
grid = np.zeros((rows, cols))  # 0 = dirty, 1 = cleaned, -1 = obstacle

# Obstacles
obstacles = [(5, y) for y in range(5, 15)] + [(15, y) for y in range(3, 18)]
for (x, y) in obstacles:
    grid[x, y] = -1  # mark as obstacle

# Robot initial position
robot_pos = [10, 10]
grid[robot_pos[0], robot_pos[1]] = 1  # cleaned

# Movement directions
directions = [(0,1),(0,-1),(1,0),(-1,0)]  # right, left, down, up
path = [tuple(robot_pos)]
coverage_history = []  # % cleaned vs steps

def step():
    """Perform one random movement step for the robot."""
    global robot_pos
    dx, dy = random.choice(directions)
    new_x = robot_pos[0] + dx
    new_y = robot_pos[1] + dy

    # Check boundaries and obstacles
    if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x, new_y] != -1:
        robot_pos = [new_x, new_y]
    grid[robot_pos[0], robot_pos[1]] = 1
    path.append(tuple(robot_pos))

    # Calculate coverage %
    cleaned = np.count_nonzero(grid == 1)
    total = np.count_nonzero(grid != -1)
    coverage = cleaned / total * 100
    coverage_history.append(coverage)
    return coverage

# --- Visualization ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,5))

def update(frame):
    coverage = step()

    # --- Left panel: room cleaning animation ---
    ax1.clear()
    ax1.imshow(grid.T, cmap="gray_r", origin="lower")
    ax1.scatter(robot_pos[0], robot_pos[1], c="red", s=100, marker="o", label="Robot")
    ax1.set_title(f"Robot Vacuum Cleaner\nStep {frame}, Coverage: {coverage:.2f}%")
    ax1.legend(loc="upper right")

    # --- Right panel: coverage plot ---
    ax2.clear()
    ax2.plot(coverage_history, color="green")
    ax2.set_title("Coverage over Time")
    ax2.set_xlabel("Steps")
    ax2.set_ylabel("Coverage (%)")
    ax2.set_ylim(0, 100)

    return ax1, ax2

ani = animation.FuncAnimation(fig, update, frames=500, interval=100, repeat=False)

plt.tight_layout()
plt.show()

# --- Save as video (optional) ---
# from matplotlib.animation import FFMpegWriter
# writer = FFMpegWriter(fps=10, bitrate=1800)
# ani.save("robot_vacuum_simulation.mp4", writer=writer)
