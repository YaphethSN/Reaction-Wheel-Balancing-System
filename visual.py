
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_pendulum(solution, params):
    theta = solution.y[0]
    time = solution.t
    L = params.rod_length
    
    fig, ax = plt.subplots(figsize=(6, 6))

    ax.set_xlim(-1.2 * L, 1.2 * L)
    ax.set_ylim(-1.2 * L, 1.2 * L)
    ax.set_aspect("equal")
    ax.grid(True)
    ax.set_title("circular motion")
    ax.set_xlabel("X Position (m)")
    ax.set_ylabel("Y Position (m)")

    ax.plot(0, 0, "ko", markersize=8)

    rod, = ax.plot([], [], linewidth=4)
    com, = ax.plot([], [], "o", markersize=8)

    info = ax.text(
        0.03, 0.95, "",
        transform=ax.transAxes,
        verticalalignment="top"
    )

    def update(frame):
        angle = theta[frame]

        x = L * np.sin(angle)
        y = L * np.cos(angle)

        rod.set_data([0, x], [0, y])
        com.set_data([x / 2], [y / 2])

        degrees = np.degrees(angle) % 360

        info.set_text(
            f"Time: {time[frame]:.2f} s\n"
            f"Angle: {degrees:.1f}°"
        )

        return rod, com, info

    animation = FuncAnimation(
        fig,
        update,
        frames=len(time),
        interval=1000 * (time[1] - time[0]),
        blit=False,
        repeat=True
    )

    return animation
