import numpy as np

def pendulAccel(thetha, mass, gravity, length, inertia):
    torque = mass * gravity * length * np.sin(thetha)
    return torque / inertia

