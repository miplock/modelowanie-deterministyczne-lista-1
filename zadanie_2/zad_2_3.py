from zad_2_1_euler import euler_explicit_logistic


def simulate_case(r, k, K=1.0, initials=(0.01, 0.1, 0.6, 1.2, 2.0),
                  t0=0.0, t_end=30.0, dt=0.01, show_fixed_lines=True, title_suffix=""):
    plt.figure()
    for N0 in initials:
        t, N = euler_explicit_logistic(N0, r, K, k, t0, t_end, dt)
        plt.plot(t, N, label=f"N0={N0}")
    if show_fixed_lines:
        N_star2 = K * (r - k) / r
        if N_star2 > 0:
            plt.axhline(N_star2, ls="--", lw=1, label=f"N*={N_star2:.3f}")
        plt.axhline(0, ls=":", lw=1, label="N*=0")
    plt.xlabel("t")
    plt.ylabel("N(t)")
    plt.title(f"Symulacje (r={r}, k={k}, K={K}) {title_suffix}")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

# (a) r=1, k=0.5, K=1
simulate_case(r=1.0, k=0.5, K=1.0, title_suffix="– przypadek (a)")

# (b) r=1, k=1.5, K=1
simulate_case(r=1.0, k=1.5, K=1.0, title_suffix="– przypadek (b)")