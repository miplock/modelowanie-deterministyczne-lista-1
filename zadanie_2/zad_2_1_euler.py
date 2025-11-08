import math
import numpy as np


def euler_explicit_logistic(
    N0: float,
    r: float,
    K: float,
    k: float,
    t0: float,
    t_end: float,
    dt: float,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Explicit (forward) Euler integrator for the logistic growth equation
    with proportional harvesting:

        dN/dt = r * N * (1 - N / K) - k * N

    Assumes the time step dt exactly partitions the interval [t0, t_end],
    i.e. (t_end - t0) / dt is an integer (within floating-point tolerance).

    Parameters
    ----------
    N0 : float
        Initial population (must be non-negative and finite).
    r : float
        Intrinsic growth rate (finite).
    K : float
        Carrying capacity (must be positive and finite).
    k : float
        Proportional harvesting rate (must be non-negative and finite).
    t0 : float
        Start time.
    t_end : float
        End time (must satisfy t_end >= t0).
    dt : float
        Time step (must be positive).

    Returns
    -------
    t : numpy.ndarray
        Time grid from t0 to t_end with uniform spacing dt.
    N : numpy.ndarray
        Numerical solution N(t) on the grid.

    Raises
    ------
    ValueError
        If any parameter is invalid or dt does not exactly partition the time interval.
    """
    # --- Parameter validation ---
    for name, val in (("N0", N0), ("r", r), ("K", K), ("k", k), ("t0", t0), ("t_end", t_end), ("dt", dt)):
        if not isinstance(val, (int, float)) or not math.isfinite(float(val)):
            raise ValueError(f"Parameter '{name}' must be a finite number (got {val!r}).")
    if N0 < 0:
        raise ValueError("Initial population N0 must be non-negative.")
    if K <= 0:
        raise ValueError("Carrying capacity K must be positive.")
    if k < 0:
        raise ValueError("Harvesting rate k must be non-negative.")
    if dt <= 0:
        raise ValueError("Time step dt must be positive.")
    if t_end < t0:
        raise ValueError("End time t_end must be >= t0.")

    # --- Check that dt exactly partitions the time interval ---
    duration = t_end - t0
    steps_float = duration / dt
    steps = int(round(steps_float))
    tol = 1e-12 * max(1.0, abs(steps_float))
    if abs(steps_float - steps) > tol:
        raise ValueError(
            f"dt must partition [t0, t_end] exactly: "
            f"(t_end - t0)/dt = {steps_float:.16g} is not an integer within tolerance."
        )

    # --- Time grid ---
    t = t0 + dt * np.arange(steps + 1, dtype=float)
    N = np.empty(steps + 1, dtype=float)
    N[0] = float(N0)

    # --- Euler iteration ---
    for n in range(steps):
        N[n + 1] = N[n] + dt * (r * N[n] * (1 - N[n] / K) - k * N[n])

    return t, N
