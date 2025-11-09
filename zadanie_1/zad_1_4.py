import numpy as np
import plotly.express as px
import pandas as pd
import pickle


# Parametry symulacji
r_values = np.arange(0, 4, 0.005)  # zakres r
N = 1000  # liczba iteracji
M = 500   # liczba odrzuconych iteracji
x0 = 0.222  # warunek początkowy

r_list = []
x_list = []

# Główna pętla generująca dane
for r in r_values:
    x = x0
    for i in range(N):
        x = r * x * (1 - x)
        if i >= M:
            r_list.append(r)
            x_list.append(x)

# Tworzymy DataFrame do wizualizacji
df = pd.DataFrame({
    'r': r_list,
    'x': x_list
})

# Tworzymy interaktywny wykres Plotly
fig = px.scatter(
    df,
    x='r',
    y='x',
    title='Wykres bifurkacyjny równania logistycznego',
    labels={'r': 'Parametr r', 'x': 'x'},
    opacity=0.3,
)

fig.update_traces(marker=dict(size=1, color='blue'))
fig.update_layout(title={
        'text': "Wykres bifurkacyjny – równanie logistyczne (JSE, <i>h=1</i>)",
        'y': 0.9,  # wysokość (0 = dół, 1 = góra)
        'x': 0.5,  # środek w poziomie
        'xanchor': 'center',
        'yanchor': 'top'
    },
                  xaxis_title="<i>r</i>", yaxis_title="<i>x</i>")

with open("zadanie_1/wykres_bifurkacyjny.pkl", "wb") as file:
    pickle.dump(fig, file)