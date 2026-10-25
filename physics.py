
import numpy as np

def pendulAccel(theta, omega, params):
    gravity_torque = (
        params.mass
        * params.gravity
        * params.com_distance
        * np.sin(theta)
    )

    damping_torque = -params.damping * omega

    total_torque = gravity_torque + damping_torque

    return total_torque / params.inertia

def pendulDynms(t, state, params):
    theta, omega = state
    alpha = pendulAccel(theta, omega, params)
    return [omega, alpha]
