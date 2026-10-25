
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

from physics import pendulDynms
from parameters import PendulumParameters

params = PendulumParameters()

theta0 = np.radians(10)
omega0 = 0.0

start_time = 0
end_time = 3
t = np.linspace(start_time, end_time, 300)

solution = solve_ivp(
    pendulDynms,
    (start_time, end_time),
    [theta0, omega0],
    t_eval=t,
    args=(params,),
    rtol=1e-9,
    atol=1e-11
)

if not solution.success:
    raise RuntimeError(solution.message)

theta = solution.y[0]
omega = solution.y[1]

plt.figure(figsize=(10, 5))

plt.plot(
    solution.t,
    np.degrees(theta),
    label="Pendulum angle"
)

plt.xlabel("Time (s)")
plt.ylabel("Angle from upright (degrees)")
plt.title("Uncontrolled Inverted Pendulum")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()
