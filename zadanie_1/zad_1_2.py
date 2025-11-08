from zad_1_1 import euler_logistic
import pickle


# Generuj dane dla N=1000
euler_logistic_1000 = euler_logistic(r=1.111, x0=0.222)

# Zapisz wyniki do pliku
with open("lista_1/zadanie_1/euler_logistic_1000.pkl", "wb") as file:
    pickle.dump(euler_logistic_1000, file)