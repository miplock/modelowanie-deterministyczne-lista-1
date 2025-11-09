from zad_2_1_euler import euler_explicit_logistic
import plotly.graph_objects as go
import pickle


def simulate_case(r, k, K=1.0, initials=(0.01, 0.1, 0.6, 1.2, 2.0),
                         t0=0.0, t_end=30.0, dt=0.01, show_fixed_lines=True, title_suffix=""):
    fig = go.Figure()

    # Dodaj trajektorie
    for N0 in initials:
        t, N = euler_explicit_logistic(N0, r, K, k, t0, t_end, dt)
        fig.add_trace(go.Scatter(
            x=t, y=N,
            mode='lines',
            name=f"N0={N0}"
        ))

    # Linie stałe (punkty równowagi)
    if show_fixed_lines:
        N_star2 = K * (r - k) / r
        if N_star2 > 0:
            fig.add_hline(
                y=N_star2,
                line_dash="dash",
                line_width=1,
                annotation_text=f"N*={N_star2:.3f}",
                annotation_position="top left"
            )
        fig.add_hline(
            y=0,
            line_dash="dot",
            line_width=1,
            annotation_text="N*=0",
            annotation_position="bottom left"
        )

    # Ustawienia wykresu
    fig.update_layout(
        title=f"Symulacje (r={r}, k={k}, K={K}) {title_suffix}",
        xaxis_title="czas [t]",
        yaxis_title="N(t)",
        legend_title="Warunki początkowe",
        template="plotly_white",
        hovermode="x unified"
    )

    return fig


# (a) r=1, k=0.5, K=1
fig_1 = simulate_case(r=1.0, k=0.5, K=1.0, title_suffix="– przypadek (a)")

# (b) r=1, k=1.5, K=1
fig_2 = simulate_case(r=1.0, k=1.5, K=1.0, title_suffix="– przypadek (b)")

with open("zadanie_2/zad_2_3_fig_1.pkl", "wb") as file:
    pickle.dump(fig_1, file)

with open("zadanie_2/zad_2_3_fig_2.pkl", "wb") as file:
    pickle.dump(fig_2, file)