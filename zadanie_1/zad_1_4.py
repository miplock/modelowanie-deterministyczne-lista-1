import numpy as np
import plotly.graph_objects as go
import pickle
from zad_1_1 import euler_logistic


x0 = 0.222
dr = 0.005
M = 500

r_values = np.linspace(0.0, 4.0, 800)

R, X = [], []
for r in r_values:
    xs = euler_logistic(r, x0)[1][M:]      # bez przejściówki
    R.extend([r]*len(xs))
    X.extend(xs)

fig = go.Figure(go.Scattergl(x=R, y=X, mode="markers",
                             marker=dict(size=1, opacity=1)))
fig.update_layout(title={
        'text': "Wykres bifurkacyjny – równanie logistyczne (JSE, <i>h=1</i>)",
        'y': 0.9,  # wysokość (0 = dół, 1 = góra)
        'x': 0.5,  # środek w poziomie
        'xanchor': 'center',
        'yanchor': 'top'
    },
                  xaxis_title="<i>r</i>", yaxis_title="<i>x</i>")

with open("lista_1/zadanie_1/wykres_bifurkacyjny.pkl", "wb") as file:
    pickle.dump(fig, file)