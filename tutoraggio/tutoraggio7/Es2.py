from scipy.stats import pearsonr
from matplotlib import pyplot as plt

l_eta = []
l_ascolti = []

with open("ascolti.txt", "r") as file:
    for line in file.readlines():
        eta, ascolti = line.split()
        eta = int(eta)
        ascolti = int(ascolti)
        l_eta.append(eta)
        l_ascolti.append(ascolti)

plt.scatter(l_eta, l_ascolti)
plt.grid()
plt.title("Grafico ascolti")
plt.xlabel("Età")
plt.ylabel("Ascolti")
plt.show()
plt.close()

correlazione, p_value = pearsonr(l_eta, l_ascolti)
print("Correlazione: ", correlazione)
print("P-value: ", p_value)
