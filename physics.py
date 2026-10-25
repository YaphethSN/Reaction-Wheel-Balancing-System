import numpy as np

def pendulAccel(theta, params):
    torque = (
        params.mass
        * params.gravity
        * params.com_distance
        * np.sin(theta)
    )

    return torque / params.inertia


def pendulDynms(t, state, params):
    theta, omega = state

    alpha = pendulAccel(theta, params)

    return [omega, alpha]