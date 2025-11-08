def rhs_logistic_harvest(N: float, r: float, K: float, k: float) -> float:
    """
    Right-hand side of the logistic growth equation with proportional harvesting.

    f(N) = r * N * (1 - N / K) - k * N

    Parameters:
        N (float): Population size (must be non-negative).
        r (float): Intrinsic growth rate (must be finite).
        K (float): Carrying capacity of the environment (must be positive).
        k (float): Harvesting rate (must be non-negative and finite).

    Returns:
        float: The rate of change of the population (dN/dt).

    Raises:
        ValueError: If any parameter is nonsensical (e.g., negative capacity,
                    NaN values, or non-finite numbers).
    """
    # --- Validation ---
    import math

    if not all(isinstance(x, (int, float)) for x in (N, r, K, k)):
        raise ValueError("All parameters (N, r, K, k) must be numeric.")

    if not all(math.isfinite(x) for x in (N, r, K, k)):
        raise ValueError("All parameters must be finite numbers (no NaN or inf).")

    if N < 0:
        raise ValueError("Population size N must be non-negative.")
    if K <= 0:
        raise ValueError("Carrying capacity K must be positive.")
    if k < 0:
        raise ValueError("Harvesting rate k must be non-negative.")

    # --- Model equation ---
    return N * (r * (1 - N / K) - k)
