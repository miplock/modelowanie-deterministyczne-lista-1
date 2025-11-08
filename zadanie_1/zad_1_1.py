import numpy as np
from typing import Tuple


def euler_logistic(r: float, x0: float, h: float = 1.0, N: int = 1000) -> Tuple[np.ndarray, np.ndarray]:
    """
    Solves the logistic equation using the explicit Euler method.

    Parameters
    ----------
    r : float, optional
        Growth rate coefficient.
    x0 : float, optional
        Initial condition (initial population value).
    h : float, optional
        Time step size.
    N : int, optional
        Number of time steps.

    Returns
    -------
    t : numpy.ndarray
        Array of time values from 0 to N * h.
    x : numpy.ndarray
        Array containing the numerical solution of the logistic equation.

    Notes
    -----
    The logistic equation has the form:
        dx/dt = r * x * (1 - x)

    This implementation uses the explicit Euler integration scheme:
        x[n+1] = x[n] + h * r * x[n] * (1 - x[n])
    """
    # Initialize the result array
    x = np.zeros(N + 1)
    x[0] = x0

    # Time vector
    t = np.linspace(0, N * h, N + 1)

    # Explicit Euler scheme
    for n in range(N):
        x[n + 1] = x[n] + h * r * x[n] * (1 - x[n])

    return t, x
