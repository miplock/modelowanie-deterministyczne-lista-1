import pickle


# Wczytaj dane z pliku
with open("lista_1/zadanie_1/euler_logistic_1000.pkl", "rb") as file:
    euler_logistic_1000 = pickle.load(file)

# Pomiń stan przejściowy
M = 500
euler_logistic_tail = (euler_logistic_1000[0][M + 1:], euler_logistic_1000[1][M + 1:])

# Zapisz wyniki do pliku
with open("lista_1/zadanie_1/euler_logistic_tail.pkl", "wb") as file:
    pickle.dump(euler_logistic_tail, file)