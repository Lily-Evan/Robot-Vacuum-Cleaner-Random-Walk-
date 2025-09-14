# Robot Vacuum Cleaner Simulation (Random Walk)

This project simulates a simple **robot vacuum cleaner** moving around a room using a **random walk algorithm**.  
The simulation shows how the robot gradually cleans the environment without any advanced path-planning logic.  

It demonstrates:
- Basic robot navigation concepts  
- Environment coverage estimation  
- Visualization of both robot movement and performance  

---

## 🔹 Features
- 20x20 grid environment
- Obstacles placed inside the room
- Robot moves randomly step by step
- Cleaned cells are marked and tracked
- **Dual visualization**:
  - Left panel → Robot cleaning animation
  - Right panel → Coverage percentage over time
- Optional: Save the animation as an MP4 video

---

## 🔧 Requirements
- Python 3.8+
- Libraries:
  ```bash
  pip install matplotlib numpy
▶️ Run
Execute:

bash
Αντιγραφή κώδικα
python robot_vacuum_randomwalk.py
You will see:

Left panel: Robot moves randomly, cleaning cells

White = dirty cells

Gray = cleaned cells

Black = obstacles

Red dot = robot

Right panel: Graph of cleaning coverage percentage vs steps

💾 Save as Video (Optional)
To save the animation as an MP4 file:

Install ffmpeg:

Linux: sudo apt install ffmpeg

Windows/Mac: Download here and add it to your PATH

Uncomment the following lines at the bottom of the script:

python
from matplotlib.animation import FFMpegWriter
writer = FFMpegWriter(fps=10, bitrate=1800)
ani.save("robot_vacuum_simulation.mp4", writer=writer)
