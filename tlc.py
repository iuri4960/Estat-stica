import scipy.stats as stats

# Definir os valores do problema
mu = 0         # Média populacional do ruído
sigma = 2      # Desvio padrão do ruído
n = 50         # Tamanho da amostra
X1, X2 = -0.5, 0.5  # Limites inferior e superior

# Calcular o desvio padrão da média amostral
sigma_X = sigma / (n ** 0.5)

# Calcular os valores padronizados Z
Z1 = (X1 - mu) / sigma_X
Z2 = (X2 - mu) / sigma_X

# Calcular a probabilidade acumulada
prob = stats.norm.cdf(Z2) - stats.norm.cdf(Z1)

print(f"Probabilidade de a média do ruído estar entre -0.5 mV e 0.5 mV: {prob:.4%}")
