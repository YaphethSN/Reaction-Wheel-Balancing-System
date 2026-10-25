
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from visual import animate_pendulum
from physics import pendulDynms
from parameters import PendulumParameters

params = PendulumParameters()

theta0 = np.radians(10)
omega0 = 0

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

plt.xlabel("Time")
plt.ylabel("Angle")
plt.title("pendulum")
plt.grid(True)
plt.legend()
plt.tight_layout()

animation = animate_pendulum(solution, params)

kinetic_energy = 0.5 * params.inertia * omega**2

potential_energy = (
    params.mass
    * params.gravity
    * params.com_distance
    * np.cos(theta)
)

total_energy = kinetic_energy + potential_energy

plt.figure(figsize=(10, 5))
plt.plot(solution.t, kinetic_energy, label="KE")
plt.plot(solution.t, potential_energy, label="GPE")
plt.plot(solution.t, total_energy, label="sigmaE")

plt.xlabel("Time")
plt.ylabel("Energy")
plt.title("GPE")
plt.grid(True)
plt.legend()
plt.tight_layout()

energy_error = np.max(np.abs(total_energy - total_energy[0]))
print(f"energy drift: {energy_error:.8e} J")

plt.show()