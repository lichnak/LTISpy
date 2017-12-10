import numpy as np

def ode45_step(f, x, t, dt, args):
    """
    One step of 4th Order Runge-Kutta method

    :param f: derivation of function
    :param x: current value (values)
    :param t: time
    :param dt: time step
    :param args:
    :return: value in given time
    """
    k = dt
    k1 = k * np.array(f(t, x, *args))
    k2 = k * np.array(f(t + 0.5 * k, x + 0.5 * k1, *args))
    k3 = k * np.array(f(t + 0.5 * k, x + 0.5 * k2, *args))
    k4 = k * np.array(f(t + dt, x + k3, *args))
    return x + 1 / 6. * (k1 + k2 + k3 + k4)


def ode45(f, t, x0, args):
    """
    4th Order Runge-Kutta method

    :param f: derivation of function
    :param t: final time
    :param x0: initial value (values)
    :param args: arguments for function
    :return: value at the end of time
    """
    n = len(t)
    x = np.zeros((n, len(x0)))
    x[0] = x0
    for i in range(n - 1):
        dt = t[i + 1] - t[i]
        x[i + 1] = ode45_step(f, x[i], t[i], dt, args)
    return x